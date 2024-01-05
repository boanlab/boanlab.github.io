# Tree-based regression

## 트리기반 회귀란?

- 의사결정 트리의 한 유형
- 회귀를 위한 트리를 생성하고 이를 기반으로 회귀 예측
- 리프 노드에 속한 데이터 값의 평균값을 구해 회귀 예측값을 계산

## 회귀 트리와 의사나무 결정의 차이점

| 기준 | 회귀 트리 | 의사결정 나무 |
| --- | --- | --- |
| 목적 | 예측 | 분류 |
| 나무 나누는 기준 | 잎노드의 변동(분산/표준편차) 최소화 되도록 | 최대한 동종의 클래스(homogeneous class)가 되도록 – 즉, 불순도가 낮도록 |
| 가지치기 기준 | RMSE | 일반화 오차의 추정값 기준 |

## 사이킷런의 Estimator 클래스

- 모든 트리 기반의 알고리즘은 CART 알고리즘에 기반하여 트리 생성
    - CART((Classification And Regression Trees)) : 분류뿐만 아니라 회귀도 가능하게 해주는 트리 생성 알고리즘

| 알고리즘 | 회귀 Estimator 클래스 | 분류 Estimator 클래스 |
| --- | --- | --- |
| Decision Tree | DecisionTreeRegressor | DecisionTreeClassifier |
| Gradient Boosting | GradientBoostingRegressor | GradientBoostingClassifier |
| XGBoost | XGBRegressor | XGBClassifier |
| LightGBM | LGBMRegressor | LGBMClassifier |

## 트리 기반 예측의 장단점

### 장점

- 더미변수를 만들지 않고 질적 변수를 쉽게 처리

### 단점

- 다중선형회귀보다 해석 어려움
- 다중회귀변수나 KNN분류에 비해 예측정확도가 좋지 않음
    - But 배깅, 랜덤포리스트, 부스팅과의 앙상블을 통해 예측성능을 향상 가능

## 코드 예제

- 아들 키 예측

### 데이터 로드

```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import numpy as np

train_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/regression/%E1%84%8B%E1%85%A1%E1%84%87%E1%85%A5%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%A1%E1%84%83%E1%85%B3%E1%86%AF%E1%84%8F%E1%85%B5.xlsx?raw=true', sheet_name='train')
test_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/regression/%E1%84%8B%E1%85%A1%E1%84%87%E1%85%A5%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%A1%E1%84%83%E1%85%B3%E1%86%AF%E1%84%8F%E1%85%B5.xlsx?raw=true', sheet_name='test')
```

### 데이터 전처리

```python
## 학습 데이터와 평가 데이터 나눔 (데이터 / 정답으로도 나눔)
x_train = train_df.drop(['Son'], axis=1)
x_test = test_df.drop(['Son'], axis=1)
y_train = train_df['Son']
y_test = test_df['Son']

#학습 데이터 출력 (잘 적용 됐는지 확인)
print(x_train.head())
'''
    Father
0  160.782
1  166.116
2  165.608
3  169.672
4  176.530
'''
```

### 모델 생성

```python
#회귀 트리 모델 생성
model = DecisionTreeRegressor()
'''
scikit-learn의 회귀 트리 클래스 종류
	DecisionTreeRegressor
	GradientBoostingRegressor
	XGBRegressor
	LGBMRegresso
'''
```

### 모델 학습

```python
#x_train과 y_train로 학습
model.fit(x_train, y_train)
```

### 모델 검증

```python
#모델에 train 데이터를 넣었을 때 정확도
print(model.score(x_train, y_train)) #0.37981060494153207
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.07133438875422093
```

### 모델 예측

```python
#예측할 데이터 입력
x_test = np.array([
    [164.338]
])

y_predict = model.predict(x_test) #예측된 값 저장

print(y_predict[0]) #172.55836363636365
```

### 시각화

```python
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

fig = plt.figure(figsize=(15, 10), facecolor='white') #새로운 figure를 생성
'''
figsize : 창의 크기를 지정 (가로 15 세로 10)
facecolor : 배경색 설정
'''
#plot_tree를 이용하여 트리 시각화
plot_tree(model,
          feature_names=x_train.columns, ## 박스에 변수 이름 표시
         )
'''
model : 시각화할 트리
feature_names : 변수 이름 표시 (x_train의 열들이 표시됨)
'''

plt.show()
```