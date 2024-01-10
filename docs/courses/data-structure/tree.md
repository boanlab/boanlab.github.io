---
layout: default
title: Tree
parent: Data-Structure
grand_parent: Courses
---

# Tree
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# 트리

### 정의

- 데이터 사이의 **계층 관계**를 나타내는 자료구조

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/204141631-cda1b857-0927-44a7-b296-effb5d628d70.jpg" width="80%"></p>

### 특징

- 노드가 N개인 트리는 항상 N-1 개의 간선(edge) 를 가진다.
- 루트에서 어떤 노드로 가는 경로는 유일하다.
- 루트 노드는 단 1개 뿐이다.
- 모든 자식 노드는 한 개의 부모 노드만을 가진다.

### 용어

- 루트(root)

  - 트리의 가장 윗부분에 위치하는 노드
  - 하나의 트리에는 하나의 루트 노드만 존재

- 리프(leaf)

  - 트리의 가장 아랫부분에 위치하는 노드(더 이상 뻗어나갈 수 없는)

- 자식(child)

  - 어떤 노드로부터 아래로 연결된 노드
  - 노드는 여러 개의 자식 노드를 가질 수 있다.

- 부모(parent)

  - 어떤 노드로부터 위로 연결된 노드
  - 노드는 단 1개의 부모 노드를 가진다.

- 형제(sibling)

  - 같은 부모를 가지는 노드

- 조상(ancestor)

  - 어떤 노드에 위쪽으로 연결된 모든 노드

- 자손(descendant)

  - 어떤 노드에 아래쪽으로 연결된 모든 노드

- 레벨(level)

  - 루트로부터 얼마나 떨어져 있는 지에 대한 값
  - 루트의 레벨은 0 , 하나씩 뻗어나갈 때 마다 1씩 증가

- 차수(degree)
  - 노드가 갖는 자식의 수
  - 모든 노드의 차수가 n이하인 트리를 n진 트리라고 정의한다.
  - ex) 2진 트리 -> 차수가 2 이하인 트리

## LCRS 트리 (Left Child, Right Siblings)

### 정의

- 왼쪽에는 자식이 붙고, 오른쪽에는 형제 노드만 붙는 형태의 트리

### 특징

- 노드의 데이터 & 왼쪽 자식에 대한 포인터 & 오른쪽 형제에 대한 포인터만 필요

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210493898-b69d4259-c035-467d-a690-1be4587ffa9e.png" width = "50%" ></p>
  
# 이진 트리

### 정의

- 이진트리는 각 노드가 최대 두 개의 자식을 갖는 트리를 뜻한다.
- 각 노드는 자식이 ( 0 ~ 2 ) 개만을 갖는 것이다.

## 포화 이진 트리

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/204441634-c646caa7-c0e1-40c8-a541-4dfc14cd9281.png" width="40%"></p>

### 정의

- 모든 레벨이 노드로 꽉 차 있는 트리를 뜻한다.

### 특징

- **완전 이진트리의 성질**도 만족해야 한다.
- 모든 말단 노드가 동일한 깊이 또는 레벨을 갖는다.
- k를 트리의 높이라 하면, 트리의 **노드 개수**가 정확히 **2^k**개여야 한다.

</br>

## 완전 이진 트리

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/204446560-db0abad9-4ad7-471c-b5ee-9f3a87601542.png" width="70%"></p>

### 특징

- 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 노드는 왼쪽에서 오른쪽으로 채워져야 한다.
- 마지막 레벨 h에서 1부터 2^h-1 개의 노드를 가질 수 있다.

</br>

## 경사트리

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/204537118-c2767d79-2af0-49f5-b6da-fc2694332031.jpg" width="60%"></p>

- 한 쪽으로 치우친 트리
- 경사 이진 트리일 경우 노드 수를 n개라고 할 때 트리의 높이가 n과 같게 된다.
  - 시간복잡도 O(n) (이진 트리 중 효율 최악)
- 이진 탐색 트리의 효율을 높이기 위해서는 가능한 트리를 좌우로 균형있게 설계해야 한다.

</br>

## 트리 순회

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/204142990-68222c25-c333-4222-8ca1-15067a5d239e.jpg" width="80%"></p>

- 전위 순회(Preorder Traversal)

  - 루트 노드를 시작으로 왼쪽 서브 트리 -> 오른쪽 서브 트리 순으로 순회
  - 현재 노드 -> 노드 방문 > 오른쪽 자식
  - 예시 : A-B-D-H-E-I-J-C-F-G-K

- 중위 순회(Inorder Traversal)

  - 왼쪽 최하위 노드를 시작으로 왼쪽 서브 트리 -> 루트 노드 -> 오른쪽 서브 트리 순으로 순회
  - 왼쪽 자식 -> 노드 방문 -> 오른쪽 자식
  - 예시 : H-D-B-I-E-J-A-F-C-G-K

- 후위 순회(Postorder Traversal)

  - 왼쪽 최하위 노드를 시작으로 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트 노드 순으로 순회
  - 왼쪽 자식 -> 오른쪽 자식 -> 노드 방문
  - 예시 : H-D-I-J-E-B-F-K-G-C-A

- [참고] 이진 트리의 level order traversal
  - 이진 트리 순회 방법으로, 트리의 레벨 순서대로 순회하는 방법이다.
  - BFS 알고리즘과 동일하다고 봐도 된다. (단지 이진 트리에서 사용할 뿐)
  - 루트 노드 -> 루트 노드의 Left Child -> 루트 노드의 Right Child
    </br>

## 수식트리

### 정의

- 이진 트리의 일종으로 수식을 트리 형태로 만든것

### 특징

- 하나의 연산자가 두 개의 피연산자를 취한다는 가정
  - 피연산자는 잎 노드
  - 연산자는 루트 노드 or 가지 노드

### 원리

- 컴퓨터는 중위 표기식을 처리하기 적합하지 않기에 입력받은 수식을 후위 표기식으로 변환 후 트리를 구성한다

  - ex) ( 1 + 2 ) _ 7 => 1 2 + 7 _

- **스택**을 사용
- 후위 표기법의 수식을 앞에서부터 차례대로 참조

- 피연산자를 만나면 무조건 스택으로 옮긴다.
- 연산자를 만나면 스택에서 두 개의 피연산자를 꺼내어 자식 노드로 연결한다.
- 자식 노드로 연결해서 만들어진 트리는 다시 스택으로 옮긴다.

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210470202-a590529a-a6ad-44f7-b62e-eea100f06bdf.png" width="80%"></p>

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210470376-f0aad781-47a6-4cfe-8fa4-158f52d3bedb.png" width="80%"></p>

### 장점

- 순회를 통해 다양한 표기법으로 수식 표현 가능

</br>

## AVL 트리

### 정의

- 스스로 균형을 잡는 데이터 구조
- 자가 균형 이진 탐색 트리

### 특징

- **이진 탐색 트리**의 속성을 가진다.
- 왼쪽, 오른쪽 서브 트리의 높이 차이가 **최대 1**이다.
- 높이 차이가 1보다 커지면 **회전**을 통해 균형을 맞춘다.

### 원리

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210480864-39d5da68-b927-476b-8f82-75569a23d2dd.png" width="50%"></p>

#### 용어

- 균형 인수 (Balance Factor (BF))
  - 왼쪽 서브트리의 높이 - 오른쪽 서브트리의 높이
- 회전 (Rotation)

  - 노드 삽입이나 삭제 시 불균형 상태 (BF != -1,0,1) 인 경우 불균형 노드를 기준으로 서브트리의 위치 변경

- 불균형 Case
  - LL (Left Left)
  - RR (Right Right)
  - LR (Left Right)
  - RL (Right Left)

**LL (Left Left)**

- Right Rotation 수행
  - y 노드의 오른쪽 자식 노드를 z 노드로 변경
  - z 노드 왼쪽 자식 노드를 y 노드 오른쪽 서브트리(T2)로 변경
  - y가 루트 노드

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210481586-fb2b0172-a75a-4148-894e-2bfbec20718b.png"></p>

```c
struct node *rightRotate (struct node *z) {

  struct node *y = z->left;
  struct node *T2 = y->right;

// right 회전 수행
  y->right = z;
  z->left = T2;

// 노드 높이 갱신
  z->height = 1 + max(z->left->height, z->right->height);
  y->height = 1 + max(y->left->height, y->right->height);

// 새로운 루트 노드 y를 반환
  return y;

}
```

**RR (Right Right)**

- Left Rotation 수행
  - y 노드의 왼쪽 자식 노드를 z 노드로 변경
  - z 노드의 오른쪽 자식 노드를 y 노드 왼쪽 서브트리(T2)로 변경
  - y가 루트 노드

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210482373-3efeb6fe-d29e-422a-adb5-6a57fd348ece.png"></p>

```c
struct node *leftRotate (struct node *z) {

  struct node *y = z->right;
  struct node *T2 = y->left;

// left 회전 수행
  y->left = z;
  z->right = T2;

// 노드 높이 갱신
  z->height = 1 + max(z->left->height, z->right->height);
  y->height = 1 + max(y->left->height, y->right->height);

// 새로운 루트 노드 y를 반환
  return y;

}
```

**LR (Left Right)**

- Left Rotation 수행
- Right Rotation 수행

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210482688-37589db0-d72a-4328-97f0-5f38fbde7285.png"></p>

```c
y = z->left;
y = leftRotate(y);
z = rightRotate(z);
```

**RL (Right Left)**

- Right Rotation 수행
- Left Rotation 수행

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210482749-9668e7d3-983a-4cd5-b960-b2b6d354ddb5.png"></p>

```C
y = z->right;
y = rightRotate(y);
z = leftRotate(z);
```

### 시간복잡도

- O(logn) (n : 노드의 개수)

## 분리 집합

### 정의

- 교집합이 존재하지 않는 2개 이상의 집합

### 특징

- 구분해야 하는 데이터 집합들을 다루는 알고리즘에서 사용
- 보통 특정 집합의 대표 노드(루트)를 자식노드가 가리킴

### 원리

#### 연산

- **Find**
- - 노드 x가 어느 집합에 포함되어 있는지 찾는 메소드
  - 한 노드에 대해 Find 연산을 할 때마다 그 노드의 부모노드를 항상 root로 만들어준다.

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210489854-993f552c-6738-4cb9-9609-215f7df4e1b1.png" width = "80%"></p>

```c
int find_root(int x) {

    //x가 root이면, 그대로 반환
    if (x == parent[x]) return x;

    //x가 자식 노드일 경우, 부모 노드에 대해 재귀 실행
    //parent[x]를 최종적으로 찾을 root 노드로 갱신
    return parent[x] = find_root(parent[x]);

}

```

- **Union (합집합)**

  - 각 두 집합의 대표 노드(루트)를 찾고 한 집합의 대표노드의 부모를 다른 집합의 대표노드로 설정

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210486367-66f8e341-5596-4570-8194-c8adf81c784c.png"></p>

```c
void union_root(int x, int y) {

    //x, y 정점의 최상위 정점을 각각 찾음 (속한 트리의 루트 노드를 찾음)
    x = find_root(x);
    y = find_root(y);

    if (x != y) {
        //서로 다른 트리에 속한다면, 한 쪽의 트리를 다른 쪽에 붙임
        //항상 높이가 낮은 트리를 높이가 높은 트리에 붙임
        //합친 높이가 낮아야 시간복잡도를 줄일 수 있음
        if (node_height[x] < node_height[y]) parent[x] = y;
        else parent[y] = x;

        //만약 합친 두 트리의 높이가 같다면, 합친 후 트리의 높이를 1 증가
        if (node_height[x] == node_height[y]) {
            parent[x] = y;
            node_rank[x]++;
        }
    }
}
```
