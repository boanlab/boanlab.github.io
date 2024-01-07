---
layout: default
title: SVM
parent: Machine-Learning
grand_parent: Courses
---

# SVM
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# Support Vector Machine

## SVM 란?

- Support Vector와 Hyperplane(초평면)을 이용해서 분류를 수행하게 되는 알고리즘
    - = 모든 샘플들의 집합을 올바르게 분류한다는 가정하에 최대 마진을 갖는  초평면을 찾는 알고리즘
- **어느 한 쪽에 치우치지 않게 분류**하고 빈 공간은 **양쪽 데이터와 균등한 위치에 분류 기준**을 세워야함.

## SVM의 장단점

### SVM의 장점

- 오류 데이터 영향이 적음
- 과적합 되는 경우가 적음
- 신경망보다 사용하기 용이

### SVM의 단점

- 여러 개의 조합 테스트 필요
- 학습 속도가 느림
- 해석이 어렵고 복잡

## SVM의 분류 방법

- 최고의 마진을 가져가는 방법으로 분류 기준을 세워야함.
- 비어있는 마진이 많아야 분류가 잘됨

⇒ 마진을 최대로 할수록 새로운 데이터에 대한 분류가 정확해짐

### SVM 최적화

1. 마진을 최대로 / 오류 일부 발생
    - 일부 오류가 발생
    - 새로 들어오는 데이터에는 마진이 넓어 잘 분류될 가능성 ↑
2. 오류를 최소화 / 오류 발생 X
    - 오류 발생 가능성↓
    - 새로 들어오는 데이터는 마진이 좁아 분류가 잘못될 가능성 ↑

## 코드 예제

- 타이타닉 승객 생존 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.svm import SVC
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
#SVM 모델 생성
model = SVC(kernel='rbf', C=1.0, gamma='auto', probability=True)
'''
kernel : 
	어떤 커널함수를 사용할지
	'linear', 'sigmoid', 'rbf', 'poly'

C : 
	어느 정도의 오차를 허용할지

gamma : 
	곡률 경계에 대한 파라미터
	'rbf', 'poly', 'sigmoid'일 때 튜닝하는 값

probability :
	SVM의 점수에 로지스틱 회귀를 훈련시켜 확률 계산할지 여부
	default : False

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
print(model.score(x_train, y_train)) #0.8808219178082192
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.6837060702875399
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