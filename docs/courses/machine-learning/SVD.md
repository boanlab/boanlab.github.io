---
layout: default
title: SVD
parent: Machine-Learning
grand_parent: Courses
---

# SVD
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# Singular Value Decomposition

## SVD란?

- 행렬 분해(matrix factorizaition) 방식 중하나
    - 행렬을 회전과 확대축소로 분해하는 방법
- 고유값 분해(eigendecomposition)처럼 행렬을 대각화하는 한 방법


- A가 m x n 행렬일 때, 3개의 행렬의 곱으로 분해(decomposition)하는 것
    - SVD를 이용해 임의의 행렬 A를 정보량에 따라 여러 layer로 쪼개서 생각할 수 있게 해줌
    - mxn행렬에 임의의 행렬 A의 연산을 취했을 때, 벡터의 방향만 변하고 길이는 절대 변하지 X


- *U* : *m*차원 회전행렬 (정규직교행렬)
    - 입력 차원인 R***m* 공간에서의 회전
- Σ : *n*차원 확대축소 (확대축소 크기에 따른 정렬 형태)
    - 입력 차원인 R***m* 공간에 대해 축방향으로의 확대축소한 후, R*n*→R*m* 으로 차원 변환
- *V* : *n*차원 회전행렬(정규직교행렬)
    - 입력 차원인 R***n*공간에서의 회전

- 행렬 U와 V에 속한 열벡터 : **특이벡터(singular vector)**
    - 모든 특이벡터는 서로 직교하는 성질을 지님

## SVD의 특징

- 특이값 분해가 유용한 이유는 행렬이 정방행렬이든 아니든 관계없이 모든 m x n 행렬에 대해 적용 가능하기 때문
    - 고유값 분해(EVD)는 정방 행렬에만 적용 가능한데 반해, 특이값 분해(SVD)는 직사각 행렬에도 적용가능
    - ⇒ 정방행렬이 아닐 때도 사용 가능
- 데이터 압축, 노이즈 제거, 추천 시스템 등 머신러닝과 관련된 다양한 분야에서 응용

## SVD의 종류

### thin SVD

![http://i.imgur.com/NU5w7Uy.png](http://i.imgur.com/NU5w7Uy.png)

- Σ 행렬의 아랫부분(비대각 파트, 모두 0)과 U에서 이에 해당하는 부분을 모두 제거한 것
- U와 Σ를 줄여도 A 원복 가능

### compact SVD

![http://i.imgur.com/2AXD5Fw.png](http://i.imgur.com/2AXD5Fw.png)

- Σ 행렬에서 비대각파트뿐 아니라 대각원소(특이값)가 0인 부분도 모두 제거한 것. 이에 해당하는 U와 V의 요소 또한 제거
    - = 특이값이 양수인 부분만 골라냄
- U와 Σ, V를 줄여도 A 원복 가능

### truncated SVD

![http://i.imgur.com/CHLt0DM.png](http://i.imgur.com/CHLt0DM.png)

- Σ 행렬의 대각원소(특이값) 가운데 상위 t개만 골라낸 것
- 행렬 A를 원복 불가능
    - 행렬 A를 근사는 가능

## 코드 예제


[머신러닝 - 20. 특이값 분해(SVD)](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-20-%ED%8A%B9%EC%9D%B4%EA%B0%92-%EB%B6%84%ED%95%B4Singular-Value-Decomposition)

### 데이터 로드

```python
import numpy as np
from numpy.linalg import svd

# 4X4 Random 행렬 a 생성 
np.random.seed(121)
a = np.random.randn(4,4)
print(np.round(a, 3))

'''
[[-0.212 -0.285 -0.574 -0.44 ]
 [-0.33   1.184  1.615  0.367]
 [-0.014  0.63   1.71  -1.327]
 [ 0.402 -0.191  1.404 -1.969]]
```

### 데이터 전처리

```python
#SVD 적용
U, Sigma, Vt = svd(a)
#각 행렬의 크기 출력
print(U.shape, Sigma.shape, Vt.shape) #(4, 4) (4,) (4, 4)

#각 행렬 출력
print('U matrix:\n',np.round(U, 3))
'''
U matrix:
 [[-0.079 -0.318  0.867  0.376]
 [ 0.383  0.787  0.12   0.469]
 [ 0.656  0.022  0.357 -0.664]
 [ 0.645 -0.529 -0.328  0.444]]
'''
print('Sigma Value:\n',np.round(Sigma, 3))
'''
Sigma Value:
 [3.423 2.023 0.463 0.079]
'''
print('V transpose matrix:\n',np.round(Vt, 3))
'''
V transpose matrix:
 [[ 0.041  0.224  0.786 -0.574]
 [-0.2    0.562  0.37   0.712]
 [-0.778  0.395 -0.333 -0.357]
 [-0.593 -0.692  0.366  0.189]]
'''

print()
print()

#SVD 복원
# Sima를 다시 0 을 포함한 대칭행렬로 변환
Sigma_mat = np.diag(Sigma)
#U, Sigma, Vt 행렬들을 곱함
a_ = np.dot(np.dot(U, Sigma_mat), Vt)
print(np.round(a_, 3))

'''
[[-0.212 -0.285 -0.574 -0.44 ]
 [-0.33   1.184  1.615  0.367]
 [-0.014  0.63   1.71  -1.327]
 [ 0.402 -0.191  1.404 -1.969]]
'''
```