---
layout: default
title: K-NN
parent: Machine-Learning
grand_parent: Courses
---

# K-NN
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# K-NN

## K-NN이란?

- 데이터들 사이의 **거리를 측정하여 어떤 데이터가 가까운지 파악하고 새로운 데이터를 분류**
- 분류를 원하는 새로운 데이터와 가장 가까운 데이터가 A라면 새로운 데이터를 A로 분류
    - ⇒ 기존 데이터의 정답을 알고 있어야 하기 때문에 지도학습

## K-NN 장점과 단점

### K-NN의 장점

- 알고리즘이 간단하고 구현이 쉬움
- 수치형 데이터를 분류하는 작업에 적용하기 좋음
    - 거리를 계산하여 분류하기 때문

### K-NN의 단점

- 데이터가 크면 계산이 느림
    - 새로운 데이터가 들어오면 기존 데이터의 거리를 모두 계산한 후 분류하기 때문

## K-NN의 과정

- K : 가장 가까운 **데이터를 몇 개 까지 찾아보고 결정**할지 정하는 숫자
    - K가 만약 1이라면 가장 가까운 데이터 하나만 찾고 K가 4이라면 가장 가까운 순서대로 4개 까지 데이터를 확인
- 여러 개의 데이터를 확인하면 **데이터들이 많이 가진 정답으로 분류**

- K의 크기
    - K가 **너무 작은 경우**에는 지엽적으로 판단하여 잘못 분류될 수 있음
    - K가 **너무 크면** 여러 분류의 데이터들을 모두 포함해 버려서 정확도가 떨어질 수 있음
    - ⇒ **적당한 크기의 K를 사용해야함.**
        - 그리드 서치를 활용하여 적당한 크기의 K를 찾을 수 있음

## 코드 예제

- 타이타닉 승객 생존 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.neighbors import KNeighborsClassifier
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
#K-NN 모델 생성
model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2, weights='uniform')

'''
n_neighobrs : 
    분류시 고려할 인접 샘플 수
    K의 값을 지정함

metric : 
    거리 측정 방식 설정
    default : minkowsi 

p : 
    minkowsi의 매개변수

weights : 
    예측에 사용하는 가중치
    uniform : 각 이웃에 동일한 가중치
    default : uniform 
    
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
print(model.score(x_train, y_train)) #0.773972602739726
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