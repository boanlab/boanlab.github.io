---
layout: default
title: AdaBoost
parent: Algorithms
grand_parent: Courses
---

# Heap
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# 우선순위 큐와 힙 (Priority Queue and Heap)

## 우선순위 큐 (Circular Queue)

### 정의
- 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조이다.

### 특징
- 우선순위 큐는 일반적으로 힙(Heap)을 이용하여 구현한다.
  - 리스트나 연결 리스트로 구현 가능하나 시간 복잡도 측면에서 치명적인 단점이 있다.

### 예제
![image](https://user-images.githubusercontent.com/57708995/210705193-88a7084e-78cc-4d78-8312-acea28b94b61.png)

### 원리
- 우선순위 큐의 삽입
   - 삽입할 원소는 완전 이진트리를 유지하는 형태로 순차적으로 삽입된다.
   - 삽입 이후, 루트 노드까지 거슬러 올라가며 최대 힙을 구한다.
   - ![image](https://user-images.githubusercontent.com/57708995/210705221-f936513d-90f0-4564-8762-f7e67e4e0e18.png)
- 우선순위 큐의 삭제
   - 루트 노드를 삭제하고, 가장 마지막 원소를 루트 노드의 위치로 옮겨준다.
   - 삭제 후 리프 노드까지 내려가면서 최대 힙을 구성
   - ![image](https://user-images.githubusercontent.com/57708995/210705229-b5971732-2b8b-4bc6-b57e-bca897c65f57.png)

### 시간복잡도
| 구현 방법 | 삽입 | 출력 |
| --- | --- | --- |
| 배열(unsorted array) | O(1) | O(N)
| 연결 리스트(unsorted linked list) | O(1) | O(N)
| 정렬된 배열(sorted array) | O(N) | O(1)
| 정렬된 연결 리스트(sorted linked list) | O(N) | O(1)
| 힙(heap) | O(logN) | O(logN)

### 활용
- 운영체제의 작업 스케줄링
- 정렬
- 네트워크 관리
  


## 힙 (Heap)

### 정의

- 이진 힙(Binary Heap)이라고도 하며, 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전 이진트리를 기본으로 한 자료구조

## 이진 힙 (Binary Heap)

### 특징

- 완전 이진 트리(Complete Binary Tree)
- 부모 노드의 키값과 자식노드의 키값 사이에 대소관계 성립
  - 키값 대소관계는 오로지 부모자식 간에만 성립. 형제 사이에는 대소관계 정해지지 않음.
- 힙 트리에서는 중복된 값을 허용 (이진 탐색 트리에서는 중복 허용X)


![heap images](https://user-images.githubusercontent.com/113777043/209763841-54f00062-3394-4080-a2a3-017d480d987f.jpg)

## 최대/최소 힙 (Min/Max Heap)

### 특징
- 최대 힙(max heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
  - key(부모 노드) >= key(자식 노드)
  - 루트 노드가 가장 큰 값을 가진다. 따라서 값이 큰 데이터가 우선적으로 제거된다.

- 최소 힙(min heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
  - key(부모 노드) <= key(자식 노드)
  - 루트 노드가 가장 작은 값을 가진다. 따라서 값이 작은 데이터가 우선적으로 제거된다.

![image](https://user-images.githubusercontent.com/57708995/209904567-82ec2c53-4eab-4154-a3e8-10f4d1541a81.png)

## 힙 정렬 (Heap Sort)

### 정의

- 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법

### 원리

- 정렬해야 할 n개의 요소들로 최대 힙(완전 이진 트리 형태)을 만든다.
  - 내림차순을 기준으로 정렬
- 그 다음으로 한 번에 하나씩 요소를 힙에서 꺼내서 배열의 뒤부터 저장하면 된다.
- 삭제되는 요소들(최댓값부터 삭제)은 값이 감소되는 순서로 정렬되게 된다.

### 장점

- 시간 복잡도가 좋은편이다.
- 힙 정렬이 가장 유용한 경우는 전체 자료를 정렬하는 것이 아니라 가장 큰 값 몇개만 필요할 때 이다.

### 시간복잡도

- O(nlog₂n)
