---
layout: default
title: K-means_clustering
parent: Machine-Learning
grand_parent: Courses
---

# K-means_clustering
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# K-means Clustering

## **K-평균 클러스터링**이란?

- 비슷한 특성을 지닌 데이터들끼리 묶어 K개의 군집으로 군집화하는 대표적인 군집화 알고리즘
    - K : 묶을 군집의 개수
    - means : 평균(=각 군집의 중심)
    - 군집(cluster) : 비슷한 특성을 지닌 데이터들을 모아놓은 그룹(Group)
- 군집 내 유사성은 높게, 군집 간 유사성은 낮게 하는 것이 좋은 분류

## **K-평균 클러스터링의 장단점**

### **K-평균 클러스터링의 장점**

- 많은 양의 데이터를 빠르게 분류 가능
    - 알고리즘이 간단
    - 탐색적 방법으로 대용량 데이터에 적합
- 데이터에 대한 사전 정보가 없어도 분석 가능
    - 비지도학습

### **K-평균 클러스터링의 단점**

- 이상치의 영향을 많이 받음
- 결과 해석이 어려움
    - 데이터를 거리로만 판단하기 때문
- 초기 군집의 수 결정하는데 어려움
    - 초기 군집 수가 적합하지 않을 시, 결과가 안 좋음
- 가중치와 거리 정의가 필요
    - 데이터들 사이의 거리와 각 변수에 대한 가중치 결정이 어려움

## **K-평균 클러스터링의 활용 예시**

1. 데이터 분류, 클러스터링 방법
2. 성향이 불분명한 시장 분석
3. 명확하지 못한 기준 분석 (ex. 트랜드)
4. 패턴인식, 음성인식의 기본 기술
5. 관련성을 알 수 없는 데이터 초기 분류

## 코드 예제

- 붓꽃 종류 군집화

### 데이터 로드

```python
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/cranberryai/todak_todak_python/master/machine_learning/multiple_classification/Iris.csv')
```

### 데이터 전처리

```python
#학습 데이터와 정답 지정 (학습 데이터 : x_data, 정답 : y_data)
x_data = df.drop(['Id', 'Species'], axis=1) #Id, Species 열을 제외한 데이터프레임
y_data = df['Species'] #Species 열만 있는 데이터프레임
```

### 모델 생성

```python
#K-means 모델 생성
model = KMeans(n_clusters=3)
'''
n_clusters :
	클러스터의 개수
'''
```

### 모델 학습

```python
#x_data로 학습
model.fit(x_data)
```

### 모델 검증

```python
'''
Inertia value는 군집화가된 후에, 
각 중심점에서 군집의 데이타간의 거리를 합산한것이으로 
군집의 응집도를 나타내는 값

=> model.inertia_로 확인 가능
'''
print(model.inertia_) #78.94084142614601
```

### 모델 예측

```python
#각 데이터가 어떤 클러스터에 속하는지 그 결과 0,1,2로 표현
print(model.labels_) #[1 1 1 2 2 1 0 0 0 2 0 1]

#x_data에 해당한 예측값
#model.labels_과 동일
y_predict = model.predict(x_data)

print(y_predict) #[0 0 0 2 2 0 1 1 1]

#출력된 예측값을 시각화
plt.scatter(x_data['SepalLengthCm'], x_data['SepalWidthCm'], c=model.labels_)
plt.title('distribution')
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.show()

'''
scatter 그래프로 설정. 
    x축과 y축은 각각 'SepalLengthCm'열과 'SepalWidthCm'열
    c : 마커의 색상 변경

title : 그래프의 제목
xlabel : 그래프의 x축 이름
ylabel : 그래프의 y축 이름
'''
```