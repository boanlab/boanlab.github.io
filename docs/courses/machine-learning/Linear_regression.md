# Linear regression

## 선형 회귀란?

- 데이터의 분포를 분석하였을 때, y=a1+a2x와 같은 선형 그래프 형태로 정의될 수 있는 문제
    - 결과값을 결정할 것이라고 추정되는 입력값 (input value)과 결과 값의 연관관계를 찾는 것

## 선형 회귀의 장단점

### 선형 회귀의 장점

- 다른 알고리즘들에 비해 비교적 간단하고 성능이 뛰어남
- 학습 속도가 빠르고 예측도 빠름
- 매우 큰 데이터셋과 희소한 데이터셋에도 잘 작동
- 예측이 어떻게 만들어지는지 수식을 통해 비교적 쉽게 이해 가능

### 선형 회귀의 단점

- 음수값이 나오면 안되는 상황에서 단순 선형 회귀 사용 불가능
- 선형관계로만 제한됨
    - 실제 모델이 선형적이지 않을 경우 결과 모델이 좋지 않음
- 이상치에 민감
- 회귀 분석에서는 사용될 수 있지만 분류에서는 실패하는 경우가 발생

## 선형 회귀의 종류

| 선형모델 종류 | 특징 |
| --- | --- |
| 선형 회귀(Linear regression) | - 변수들이 서로 선형적으로 연결되어 있는 경우 사용<br>- 머신러닝에서 가장 일반적인 회귀 분석 유형<br>- 최적적합선을 사용 |
| 로지스틱 회귀(Logistic regression) | - 종속 변수에 이산 값이 있는 경우 사용<br>- S자형 곡선을 사용하여 대상 변수와 독립 변수 사이의 관계를 표시 |
| 릿지 회귀(Ridge regression) | - 특성이 많을 때, 특성의 중요도가 전체적으로 비슷할 때 라쏘보다 성능이 좋음<br>- 독립 변수들 사이에 높은 상관 관계가 있는 경우 사용<br>- 모델의 복잡성을 줄여주는 정규화 기법<br>- 리지 회귀 패널티라는 편향을 사용하여 모델이 과대적합(overfitting)에 강하게 함 |
| 라쏘 회귀(Lasso regression) | - 특성이 많을 때, 그중 일부분만 중요할 때 릿지보다 성능이 좋음<br>- 모델의 복잡성을 줄여주는 정규화 기법<br>- 회귀 계수의 절대 사이즈를 금지함으로써 복잡성 감소<br>- 데이터 집합에서 필요한 요소들만 사용하고 나머지를 0으로 설정함으로써 과대적합을 방지 가능 |
| 다항 회귀(Polynomial regression) | - 데이터가 비선형 방식으로 존재할 때 사용<br>- 선형 모델을 사용하여 비선형 데이터 집합을 모델링<br>- 비선형 곡선을 사용 |

## 코드 예제

- 아들 키 예측

### 데이터 로드

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
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
#DataFrame을 numpy 배열 형식으로 변환
x_train = x_train.to_numpy()
x_test = x_test.to_numpy()
```

### 모델 생성

```python
#선형 회귀 모델 생성
model = LinearRegression()
```

### 모델 학습

```python
#x_train과 y_train로 학습
model.fit(x_train, y_train)
```

### 모델 검증

```python
#모델에 train 데이터를 넣었을 때 정확도
print(model.score(x_train, y_train)) #0.24967004992776765
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.25199779058466176
```

### 모델 예측

```python
#예측할 데이터 입력
x_test = np.array([
    [164.338]
])

y_predict = model.predict(x_test) #예측된 값 저장

print(y_predict[0]) #170.46931035654347
```