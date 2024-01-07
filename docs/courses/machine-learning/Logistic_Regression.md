---
layout: default
title: Logistic_Regression
parent: Machine-Learning
grand_parent: Courses
---

# Logistic_Regression
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# Logistic Regression

## 로지스틱 회귀란?

- 데이터가 어떤 범주에 속할 확률을 0에서 1 사이의 값으로 예측하고 그 확률에 따라 가능성이 더 높은 범주에 속하는 것으로 **분류해주는 지도 학습 알고리즘**
    - 설명변수(독립변수, X)와 범주형 목표변수(종속변수, Y) 간의 관계를 모형화하여 목표변수를 분석하거나 분류하는 통계적 방법론

## 로지스틱 회귀의 장단점

### 로지스틱 회귀의 장점

- 회귀 계수의 해석이 가능
- 클래스에 속할 확률 추정함
    - 확률 자체에 관심이 있는 위험도 분석과 같은 분야에서 용이
- 저차원에서 과적합 가능성이 적음
    - 저차원 자료에서 데이터 샘플수가 충분하면 과적합이 덜 일어남
- 분류 문제에서 베이스 모형으로 활용 가능
    - 특정 분류 모형의 성능을 비교 평가하고 싶을 때 비교 모형으로 사용 가능

### 로지스틱 회귀의 단점

- 분류 경계가 선형
- 이상치에 민감

## **모델 탐색방법**

- [시그모이드(Sigmoid) 함수](https://icim.nims.re.kr/post/easyMath/64)
    - 바이너리 로지스틱 회귀에 주로 사용.
    - 시그모이드 함수는 결과 값을 0,1로 반환
        - ⇒ 두 가지로 분류할 때 유용
- [소프트맥스(Softmax) 함수](https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221021710286&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
    - softmax 함수 또한 활성화 함수
    - 여러개를 분류하는데 특화
    - softmax는 출력값들이 정규화가 되어있기 때문에 결과값들의 합은 1을 나타넴
        - ex) A 0.2 / B 0.2 / C 0.6 -> C가 될 확률이 60%
- 최대 우도 추정법
    - 시그모이드 함수를 최적화 가능
    - 어떤 확률변수에서 표집한 값들을 토대로 그 확률변수의 모수를 구하는 방법
    - 어떤 모수가 주어졌을 때, 원하는 값들이 나올 가능도를 최대로 만드는 모수를 선택하는 방법

## 로지스틱 회귀 주요 용어

- 오즈 (odds) : ‘실패’(0)에 대한 ‘성공’(1)의 비율
- 로짓 (logit) : ±∞의 범위에서 어떤 클래스에 속할 확률을 결정하는 함수
- 로그 오즈 (log odds) : 변환 모델(선형)의 종속 변수, 이 값을 통해 확률을 구함

## 코드 예제

- 당뇨병 발병 여부 분류

### 데이터 로드

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

train_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='train')
test_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='test')

labels = ['정상', '당뇨'] #정답 라벨
```

### 데이터 전처리

```python
## 학습 데이터와 평가 데이터 나눔 (데이터 / 정답으로도 나눔)
x_train = train_df.drop(['ID', '당뇨여부'], axis=1)
x_test = test_df.drop(['ID', '당뇨여부'], axis=1)
y_train = train_df['당뇨여부']
y_test = test_df['당뇨여부']

#학습 데이터 출력 (잘 적용 됐는지 확인)
print(x_train.head())
'''
   임신  글루코스(탄수화물 화합물)  혈압  피부두께  인슐린   BMI    가족력  나이
0   1              85  66    29    0  26.6  0.351  31
1   3              78  50    32   88  31.0  0.248  26
2   1             189  60    23  846  30.1  0.398  59
3   0             118  84    47  230  45.8  0.551  31
4   1             103  30    38   83  43.3  0.183  33
```

### 모델 생성

```python
#로지스틱 회귀 모델 생성
model = LogisticRegression()
```

### 모델 학습

```python
#x_train과 y_train로 학습
model.fit(x_train, y_train)
```

### 모델 검증

```python
#모델에 train 데이터를 넣었을 때 정확도
print(model.score(x_train, y_train)) #0.7579787234042553
#모델에 test 데이터를 넣었을 때 정확도
print(model.score(x_test, y_test)) #0.7577639751552795
```

### 모델 예측

```python
#예측할 데이터 입력
x_test = np.array([
    [3, 78, 50, 32, 88, 31, 0.2, 26]
])

#입력 데이터에 해당한 예측값
y_predict = model.predict(x_test) #예측된 클래스값 반환
label = labels[y_predict[0]] #정수의 예측값을 해당하는 label로 변환
y_predict = model.predict_proba(x_test) #클래스에 대한 확률값 반환
confidence = y_predict[0][y_predict[0].argmax()] #가장 높은 확률값 저장 (가장 높은 확률값으로 클래스를 유추했을 것이므로)

print(label, confidence) #정답 라벨과 해당 라벨일 확률 출력
```