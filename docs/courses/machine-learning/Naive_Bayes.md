# Naive Bayes

## 나이브 베이즈란?

- 데이터가 각 클래스에 속할 특징 확률을 계산하는 조건부 확률 기반의 분류 방법
- Naive :
    - 예측한 특징이 상호 독립적이라는 가정하에 확률 계산을 단순화
    - 모든 변수(특징)들이 동등하다는 것을 의미
- Bayes :
    - 입력 특징이 클래스 전체의 확률 분포 대비 특정 클래스에 속할 확률을 베이즈 정리 기반으로 계산
- 베이즈 정리 :
    - 사건 B가 발생함으로써(사건 B가 진실이라는 것을 알게 됨으로써, 즉 사건 B의 확률 P(B)=1이라는 것을 알게 됨으로써) 사건 A의 확률이 어떻게 변화하는지를 표현한 정리

## 나이브 베이즈의 장단점

### 나이브 베이즈의 장점

- 간단하고 빠른 효율적인 알고리즘
- 노이즈와 누락 데이터를 잘 처리함
- 학습할 때 데이터의 크기에 상관없이 작동
- 예측을 위한 추정 확률 얻기 용이

### 나이브 베이즈의 단점

- 모든 특징이 동등하게 중요하고 독립이라는 가정이 잘못된 경우가 있음
- 수치 특징이 많은 데이터셋에는 이상적X
- 추정된 확률이 예측된 클래스보다 신뢰X

## 나이브 베이즈의 활용 방안

텍스트 분류에 사용됨으로서 문서를 여러 범주 (예: 스팸, 스포츠, 정치) 중 하나로 판단하는 문제에 대해 대중적으로 사용됨.

- 스팸 필터링
    - 대중적인 활용 방안.
    - 이진분류 (스팸인지 / 아닌지)
- 비정상적인 상황 감지
    - 이진분류
- 의학적 질병 진단
    - 암 여부 진단 등 질병 진단
    - 이진분류
- 문서 분류
    - 해당 문서가 스포츠, 정치, 연예 등 어떤 카테고리에 해당하는지 분류
    - 다중 분류
    

## 코드 예제

- 타이타닉 승객 생존 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.naive_bayes import GaussianNB
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
#Naive Bayes 모델 생성
model = BernoulliNB()
'''
BernoulliNB : 
	이진 데이터에 적용
MultinomialNB : 
	카운트 데이터(ex 문장에 나타난 단어의 횟수)에 적용
GaussianNB : 
	연속적인 데이터에 적용
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
print(model.score(x_train, y_train)) #0.7684931506849315
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.7763578274760383
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