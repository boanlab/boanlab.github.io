---
layout: default
title: List
parent: Data-Structure
grand_parent: Courses
---

# List

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

- TOC
  {:toc}

---

# 리스트

## 리스트

### 정의

- 순열(Sequence)이라고도 불리며, 순서를 가지고 일렬로 나열한 원소들의 모임으로 정의한 자료구조이다.
- 데이터를 순차적으로 저장하기 때문에 선형 구조를 띄며 값이 중복될 수 있다.

### 리스트의 연산

- 빈 리스트를 만드는 연산(Constructor, 생성자)
- 리스트가 비어있는지 확인하는 연산
- 리스트에 원소를 삽입하는 연산(Add)
- 리스트의 원소를 찾는 연산(Peek)

### 리스트의 종류

- 순차 리스트
- 연결 리스트
  1. 단일 연결 리스트
  2. 이중 연결 리스트
  3. 환형 연결 리스트(원형 연결 리스트)

### 순차 리스트와 연결 리스트 비교

**데이터의 삽입 & 삭제 측면**

- 순차 리스트는 데이터의 삽입이나 삭제 후 연속적인 물리적 위치를 유지하기 위해 원소를 옮기는 추가 작업이 필요하다.
- 연결 리스트는 특정 노드를 삽입하거나 삭제할 때 노드의 링크 필드만 수정하면 되므로 순차 리스트에 비해 연산 속도가 빠르다.

**데이터의 탐색 측면**

- 순차 리스트는 배열로 구현하기 때문에 인덱스를 통해 원소를 탐색할 수 있다.
- 연결 리스트는 이전 노드를 통해서만 다음 노드를 참조할 수 있다는 특성 때문에 리스트의 처음부터 다음 노드들을 탐색해야 한다.
- 따라서 순차 리스트가 연결 리스트에 비해 탐색 속도가 빠르다.

---

## 연결 리스트

### 정의

- 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조이다.
- 노드의 포인터가 다음이나 이전의 노드와의 연결을 담당하게 된다.

### 연결 리스트의 종류

- 단일 연결 리스트
- 이중 연결 리스트
- 환형 연결 리스트(원형 연결 리스트)

---

## 단일 연결 리스트

### 정의

- 단일 연결 리스트는 각 노드에 자료 공간과 한 개의 포인터 공간(링크 필드)이 있고, 각 노드의 포인터는 다음 노드를 가리킨다.

### 특징

- 하나의 링크 필드를 사용한다.
- 마지막 노드의 링크 필드 값은 Null이다.
- Head 노드를 참조하는 주소를 잃어버릴 경우, 데이터 전체를 못 쓰게 되는 단점이 있다.
- 다음 노드를 참조하는 주소 중 하나가 잘못되면, 링크 체인이 끊어져 끊어진 뒤쪽 데이터들을 유실하게 된다.
  - 안정적인 자료구조는 아니다.

---

## 이중 연결 리스트

![image](https://user-images.githubusercontent.com/113777043/204078252-5804e394-5921-4bfc-a25c-c89456c1a7bf.png)

- Node

  ```
   - *Llink // 이전 노드를 가리키는 포인터
   -  Data  // 데이터를 담을 변수
   - *Rlink // 다음 노드를 가리키는 포인터
  ```

- Node 추가

  ![image](https://user-images.githubusercontent.com/113777043/204078990-c0a340f7-0fd1-4941-96b9-a61b781034d5.png)

  - newnode와 선행노드 연결

    ```
    - tail -> llink -> rlink = new     // new 노드의 선행노드의 rlink = new, 선행노드부터 연결시킴
    - new -> llink = tail -> llink     // new 노드의 llink = 후행노드의 llink
    ```

  - newnode와 후행노드 연결

    ```
    - tail -> llink = new              // 후행노드의 llink = new
    - new -> rlink = tail              // new 노드의 rlink = tail
    ```

- Node 삭제

  ![image](https://user-images.githubusercontent.com/113777043/204079011-a935fbe2-6758-4e3d-8dba-db390e3cafda.png)

  ```
  - // 선행노드와의 연결부터 끊어준다
  - del -> llink -> rlink = del -> rlink // 삭제할 노드의 llink의 rlink = 삭제할노드의 rlink
  - del -> rlink -> llink = del -> llink
  ```

---

## 환형 연결 리스트(원형 연결 리스트)

![2-3-1](https://user-images.githubusercontent.com/57708995/204690252-68bb3a17-e739-4926-a392-e1b3fc17a54b.JPG)

- Node

  ```
   -  head // 마지막 노드를 가리키는 포인터
   -  item  // 데이터를 담을 변수
   -  head->link // 첫 번째 노드를 가리키는 포인터
  ```

- Node 추가

  ![image](https://user-images.githubusercontent.com/57708995/204696674-fd5c00c3-3a65-4f37-85be-6f74dcddae66.png)
  ![image](https://user-images.githubusercontent.com/57708995/204696817-c8d61be5-5170-49a2-ac4e-8a4b7108f3d3.png)

  - 첫 번째 노드 생성

    ```
    - head =  node
    - node->link = head
    ```

  - 앞부분 삽입(두 번째 이후의 노드일 때 삽입)

    ```
    - node->link = head->link    // node의 link를 head의 link로 할당
    - head->link = node          // head의 link를 node로 할당
    ```

  - 뒷부분 삽입(두 번째 이후의 노드일 때 삽입)

    ```
    - node->link = head->link    // node의 link를 head의 link로 할당
    - head->link = node;	     // head의 link를 node로 할당
    - head = node;	             // head를 node로 할당
    ```

- Node 삭제

  ```
  Node* rpos = cur;         //소멸 대상의 주소 값을 rpos에 저장
  LData rdata = rpos->data; //삭제할 데이터 임시 저장
  before->link = cur->link; //소멸 대상을 리스트에서 제거
  cur = before;             //cur이 가리키는 위치를 재조정
  delete(rpos);
  numOfData--;
  return rdata;             //삭제된 데이터의 반환
  ```
