---
layout: default
title: PCA
parent: Machine-Learning
grand_parent: Courses
---

# PCA
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# Principal Components Analysis

## PCA란?

- 차원 축소의 가장 대표적인 알고리즘
- 기존 데이터의 분포를 최대한 보존하면서 고차원 공간의 데이터들을 저차원 공간으로 변환
- 여러 변수 간에 존재하는 상관관계를 이용해 이를 대표하는 주성분을 추출해 차원을 축소하는 기법
    - 데이터를 축에 사영했을 때 가장 높은 분산을 가지는 데이터의 축을 찾아 그 축으로 차원을 축소하는 것 (이 축이 주성분)
        - 높은 분산을 가지는 축을 찾는 이유 : 정보의 손실을 최소화하기 위해서
        - 높은 분산 : 원래 데이터의 분포를 잘 설명할 수 있음을 의미

## PCA의 장단점

### PCA의 장점

- 데이터 분석에 대한 특별한 목적이 없는 경우에 합리적
- 고차원의 데이터를 손실을 최소화하여 효율적으로 축소가능

### PCA의 단점

- PCA는 비지도 학습이기 때문에 지도학습이 목적인 경우, 분류의 핵심정보 손실이 발생할 수 있음
- 비선형구조를 반영하지 못함

## PCA의 목적

- 데이터를 대표하는 주성분(Principal Components)을 찾아 변수의 차원(개수)을 줄이는 목적
- 변수에 의한 데이터의 overlap을 감소시키는 목적
- 데이터의 고유정보를 최대한 유지

## PCA와 선형회귀의 차이점

| 선형회귀 | PCA |
| --- | --- |
| 각 데이터점과 prediction line 간의 squared error (vertical distance)를 최소화 | 각 데이터점과 projection line간의 shortest distance (or orthogonal distance)를 최소화 |
| 피처 x가 주어진 경우 변수 y의 값을 예측 | 레이블 y는 없고 모든 피처를 동일하게 취급 |
| 점과 직선 사이의 오차 제곱을 최소화 | 점과 직선 사이의 직교하는 선분을 최소화 |

## 코드 예제

### 데이터 로드

```python
import pandas as pd
from sklearn.decomposition import PCA

#hour, attendance, score
#데이터프레임 생성
df = pd.DataFrame([
    [2, 1, 3],
    [3, 2, 5],
    [3, 4, 7],
    [5, 5, 10],
    [7, 5, 12],
    [2, 5, 7],
    [8, 9, 13],
    [9, 10, 13],
    [6, 12, 12],
    [9, 2, 13],
    [6, 10, 12],
    [2, 4, 6]
], columns=['hour', 'attendance', 'score'])
```

### 데이터 전처리

```python
#학습 데이터와 정답 지정 (학습 데이터 : x_data, 정답 : y_data)
x_data = df.drop(['score'], axis=1) 
y_data = df['score']

#PCA를 사용하여 차원축소
transformer = PCA(n_components=1)
'''
n_components : 주성분의 개수 설정
'''
transformer.fit(x_data) #PCA 학습
x_data = transformer.transform(x_data) #학습된 PCA에 대입하여 x_data 변환

print(x_data) #변환된 값 확인
'''
[[-5.69589581]
 [-4.33090748]
 [-2.59604503]
 [-0.7334996 ]
 [ 0.2616146 ]
 [-2.2261709 ]
 [ 4.2288966 ]
 [ 5.59388493]
 [ 5.83607608]
 [-1.34556488]
 [ 4.10121363]
 [-3.09360213]]
```