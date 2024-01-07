---
layout: default
title: DecisionTree
parent: Machine-Learning
grand_parent: Courses
---

# DecisionTree
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# DecisionTree

## 의사 결정 나무란?

- 지도학습의 일종으로 데이터에 있는 패턴을 찾아내고 **조건을 통해 데이터를 분할**
하며 예측하는 모델
- **조건에 해당되는 데이터는 좌측으로 해당하지 않는 데이터는 우측으로 분류**
- 조건을 통해 데이터를 분리하여 **데이터를 나눌 수 있는 기준이 확립되면** 새로운 데이터가 들어왔을 때도 조건을 활용해 데이터를 예측할 수 있음

## 의사 결정 나무의 장단점

### 의사 결정 나무의 장점

- 규칙이 쉽고 간단한 모형일 때, 해석이 쉬움
- 특성의 중요성 비교 가능
    - 조건마다 하나의 특성을 기준으로 구분하기 때문에 결과를 예측할 때 어떤 특성이 중요하게 영향을 미치는지 파악 가능

### 의사 결정 나무의 단점

- 모형이 복잡하면 성능이 떨어지고 해석이 어려움
- 데이터 변형에 민감
    - 학습에 활용된 데이터들을 기준으로 세부적으로 나누기 때문에 다른 데이터를 활용했을 경우 성능이 크게 떨어지는 경우가 많음

        

## 의사 결정 나무의 용어

- **뿌리마디** :
    - 나무구조가 시작되는 마디
    - 그림에서 1번에 해당
    - 모든 데이터를 담고 있음
- **부모마디** :
    - 자식마디를 가지고 있는 마디
    - 그림에서 1번 마디는 2,3번의 부모마디
- **자식마디** :
    - 부모마디에서 갈라져 나온 마디.
    - 그림에서 2,3번은 1번 마디의 자식마디
- **끝마디** :
    - 각 나무줄기에서 마지막에 위치하는 마디
    - 그림에서 6,7,8,9 마디가 끝 마디
    - 끝 마디의 개수만큼 규칙이 생성됨
- **중간마디** :
    - 뿌리 마디와 끝마디가 아닌 마디
- **깊이** :
    - 뿌리마디를 제외하고 끝마디까지 연결된 마디의 개수
    - 그림에서의 깊이는 3
    

## 코드 예제

- 타이타닉 승객 생존 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.tree import DecisionTreeClassifier
import numpy as np

train_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%90%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A1%E1%84%82%E1%85%B5%E1%86%A8_b0fdSDZ.xlsx?raw=true', sheet_name='train')
test_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%90%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A1%E1%84%82%E1%85%B5%E1%86%A8_b0fdSDZ.xlsx?raw=true', sheet_name='test')

labels = ['사망', '생존'] #정답 라벨
```

### 데이터 전처리

```python
## 학습 데이터와 평가 데이터 나눔 (데이터 / 정답으로도 나눔)
x_train = train_df.drop(['name', 'ticket', 'survival'], axis=1)
x_test = test_df.drop(['name', 'ticket', 'survival'], axis=1)
y_train = train_df['survival']
y_test = test_df['survival']

#학습 데이터 출력 (잘 적용 됐는지 확인)
print(x_train.head()) 
'''
   pclass     sex  age  sibsp  parch    fare embarked
0       2  Female   21      0      1   21.00        S
1       3    Male   35      0      0    7.05        S
2       1    Male   45      1      1  134.50        C
3       2    Male   40      0      0   16.00        S
4       1  Female   55      2      0   25.70        S
'''
#학습에 사용할 속성 확인
print(x_train.columns) #Index(['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked'], dtype='object')

#치환기 생성
transformer = make_column_transformer(
    (OneHotEncoder(), ['pclass', 'sex', 'embarked']),
    remainder='passthrough')
'''
원-핫-인코딩
: 범주형 변수를 표현하는 데 가장 널리 쓰이는 방법

make_column_transformer : 
    더미변수 치환기
    이름을 자동으로 붙여주는 함수

적은 행(['pclass', 'sex', 'embarked'])을 더미 변수로 전환
remainder='passthrough'
    튜플에서 정의하지 않은 열들을 변환하지 않고 출력
'''

transformer.fit(x_train) #치환기 학습
x_train = transformer.transform(x_train) #치환기에 대입하여 x_train 변환
x_test = transformer.transform(x_test) #치환기에 대입하여 x_test 변환
```

### 모델 생성

```python
#DT 모델 생성
model = DecisionTreeClassifier(criterion='gini', max_depth=None, max_leaf_nodes=None, min_samples_split=2, min_samples_leaf=1, max_features=None)
'''
criterion :
	노드 분리기준
	'gini'와 'entropy'를 사용

max_depth :
	트리의 최대 깊이
	default : None

max_leaf_nodes :
	리프노드의 최대 개수

min_samples_split :
	노드를 분할하기 위한 최소한의 샘플 데이터수 → 과적합을 제어하는데 사용
	default : 2

min_samples_leaf :
	리프노드가 되기 위해 필요한 최소한의 샘플 데이터수

max_features :
	최적의 분할을 위해 고려할 최대 feature 개수
	default : None
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
print(model.score(x_train, y_train)) #0.9821917808219178
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.7028753993610224
```

### 모델 예측

```python
#예측할 데이터 입력 (데이터프레임화 -> 치환기에 대입하여 변환)
x_test = [
    [2, 'Female', 21, 0, 1, 21.00, 'S']
]
x_test = pd.DataFrame(x_test, columns=['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked'])
x_test = transformer.transform(x_test)

#입력 데이터에 해당한 예측값
y_predict = model.predict(x_test) #예측된 클래스값 반환
label = labels[y_predict[0]] #정수의 예측값을 해당하는 label로 변환
y_predict = model.predict_proba(x_test) #클래스에 대한 확률값 반환
confidence = y_predict[0][y_predict[0].argmax()] #가장 높은 확률값 저장 (가장 높은 확률값으로 클래스를 유추했을 것이므로)

print(label, confidence) #정답 라벨과 해당 라벨일 확률 출력
```