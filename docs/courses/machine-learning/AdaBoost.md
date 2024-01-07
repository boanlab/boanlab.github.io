---
layout: default
title: AdaBoost
parent: Machine-Learning
grand_parent: Courses
---

# AdaBoost
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# AdaBoost

## AdaBoost 란?

- 초기 모델을 약한 모델로 설정하여 매 스텝마다 가중치를 이용해 이전 모형의 약점을 보완하는 새로운 모델을 순차적으로 적합함. 그 후 최종적으로 순차적으로 적합한 모델을 선형 결합하여 얻어진 모델을 생성하는 알고리즘
    - 가중치를 부여한 약 분류기(Weak Classifier)를 모아서 최종적인 강 분류기(Strong Classifier)를 생성하는 기법
- Boosting 알고리즘의 한 종류
- Adaptive Boosting 의 약자
- 분류 문제, 회귀 문제 모두에 적용 가능

## AdaBoost의 장단점

### AdaBoost의 장점

- 과적합의 영향을 덜 받음
- 구현이 쉬움
- 유연함
    - 손실 함수를 여러가지 사용할 수 있고, 다양한 모델을 사용 가능 (ex. DT, 로지스틱 회귀, 선형 회귀 등)
- RF와 비교했을 때, 비교적 속도가 더 빠르고 결과가 좋게 나옴

### AdaBoost의 단점

- 이상치에 민감
- 해석이 어려움
- 조정해야 하는 hyperparameter의 개수 증가

### Bagging

- boostrap aggregating의 약어
- 샘플을 여러 번 뽑아 각 모델을 학습시켜 결과물을 집계하는 방법
- 독립적인 데이터 셋으로 독립된 모델을 만듦
- 알고리즘의 안정성이 주 목적
- 대표적인 알고리즘 : Random Forest

### Boosting

- 가중치를 활용하여 약 분류기를 강 분류기로 만드는 방법
- 처음 모델이 예측을 하면 그 예측 결과에 따라 데이터에 가중치가 부여되고, 부여된 가중치가 다음 모델에 영향 줌
- 정확성 향상이 주 목적
- 대표적인 알고리즘 : AdaBoost, XGBoost

## 코드 예제

- 타이타닉 승객 생존 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.ensemble import AdaBoostClassifier
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

#DataFrame을 numpy 배열 형식으로 변환
y_train = y_train.to_numpy()
y_test = y_test.to_numpy()
```

### 모델 생성

```python
#AdaBoost로 모델 생성
model = AdaBoostClassifier(n_estimators=100, random_state=0)
'''
n_estimators :
	생성할 약한 학습기의 갯수를 지정
	default : 50

random_state : 
	random 함수의 seed값
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
print(model.score(x_train, y_train)) #0.826027397260274
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.7987220447284346
```

### 모델 예측

```python
#입력할 데이터 설정 (데이터프레임화 -> 치환기에 대입하여 변환)
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