---
layout: default
title: AdaBoost
parent: Algorithms
grand_parent: Courses
---

# Search
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# 탐색 (Search)

</br>


# 순차 탐색 (Sequential Search)

- 데이터의 집합을 처음부터 끝까지 모든 요소를 비교해서 데이터를 찾는 알고리즘
- ‘처음부터 끝까지’ 전략으로 비효율적
- 구현이 간단하고 버그를 만들 가능성이 적어 유용하게 사용 가능

- 전진 이동법 / 전위법 / 계수법

#

## 전진 이동법

### 정의

- 항목이 한 번 탐색되면, 그 항목을 데이터 집합의 가장 앞에 위치시키는 알고리즘
</br>

### **원리**

| 5 | 3 | 7 | 1 | 2 |
| --- | --- | --- | --- | --- |

만약 7 이 탐색된다면?

| 7 | 5 | 3 | 1 | 2 |
| --- | --- | --- | --- | --- |

7이 데이터 집합의 가장 앞으로 이동된다.

찾은 데이터 값(7) **앞에 있는 값**들을 **한 칸씩 뒤로** 민다.

</br>

### **구현 방법**

- 이중 반복문으로 탐색된 값을 찾으면 맨 앞으로 옮기고 나머지 값들을 한 칸씩 옮겨주면 된다.

</br>

### **코드**

```python
def move_to_front(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            for j in range(i-1,-1,-1):  # key 값의 앞 부분만 뒤로 한 칸씩 밀리면 된다.
                arr[j+1] = arr[j]
            arr[0] = key # 맨 처음 값은 key값으로
            return i
    return False
```

</br>

### **활용 예시**

- MS 워드 - ‘최근 문서’ 기능 등

### **장점**

- **한 번 찾은 데이터**가 빈번하게 사용되는 경우 등에서 탐색 효율 증가

### **단점**

- 위의 경우 이외에는 매우 비효율적일 수 있다.

#

## 전위법

### 정의

- **탐색된 항목을 바로 이전의 항목과 교환**하는 알고리즘
- 기본적으로 전진 이동법과 같은 전략을 취함

### 원리

| 5 | 3 | 7 | 1 | 2 |
| --- | --- | --- | --- | --- |

만약 7 이 탐색된다면?

| 5 | 7 | 3 | 1 | 2 |
| --- | --- | --- | --- | --- |

7이 바로 이전의 항목인 3과 교환된다.

찾은 데이터 값(7) **바로 이전의 값**과 자리를 교환한다.

### 구현 방법

- 반복문을 통해 탐색되면 바로 이전 인덱스의 값과 교환한다.

</br>

### **코드**

```python
def transpose(array, x):
    for i in range(len(array)):
        if x == array[i]: # 탐색된 경우
            if i != 0:
                # 탐색된 값을 바로 앞 인덱스 값의 자리와 교환
                array[i], array[i-1] = array[i-1], array[i]  
            return i
    return False
```

</br>

### 장점

- 많이(자주) 탐색된 데이터를 빠르게 확인 할 수 있다.
- 최악의 경우, **전진 이동법**보다 효율이 좋다.

### 단점

- 리스트의 크기가 커질수록 효율이 감소한다.

#

## 계수법

### 정의

- 데이터 집합 내 데이터가 탐색된 횟수를 별도의 공간에 저장하고 탐색된 횟수가 높은 순으로 재배치하는 알고리즘


### 장점

- **전위법**보다 효율이 좋다.

### 단점

- 탐색된 횟수를 저장하는 별도의 공간을 마련해야함. ( 비용 소모 )

</br>

#

# 이진 탐색 (Binary Search)

### 정의

- 정렬된 리스트에서 검색 범위를 줄여 나가면서 검색 값을 찾는 알고리즘

    - 정렬된 리스트에만 사용할 수 있다는 단점
    - 검색이 반복될 때마다 검색 범위가 반으로 줄기 때문에 속도가 빠르다는 장점

### 원리

- 배열의 중간 값을 가져온다.

- 중간 값과 검색 값을 비교한다.

    - (중간 값 = 검색 값) ==> 종료
    - (중간 값 < 검색 값) ==> 중간 값 기준 오른쪽 구간 대상 탐색
    - (중간 값 > 검색 값) ==> 중간 값 기준 왼쪽 구간 대상 탐색
    
- 값을 찾거나 간격이 비어있을 때까지 반복

</br>

### 코드

```c

#include <stdio.h>


// data : 탐색할 오름차순으로 정렬된 정수 배열
// n : 정수 배열의 크기
// key : 찾고자하는 값

int binsearch (int data[], int n, int key) {

    int low, high;
    int mid;
 
    low = 0;
    high = n - 1;

    while (low <= high) {

        mid = (low + high) / 2;

        if (key == data[mid]) {            //탐색 성공

            return mid;        

        }
        else if (key < data[mid]) {        //탐색 범위를 밑으로

            high = mid - 1;

        }
        else if (key > data[mid]) {        //탐색 범위를 위로

            low = mid + 1;
            
        }
    }

    return -1;                            //탐색 실패
}
```

</br>

### 장점
- O(logn)으로 빠르게 탐색 가능

### 단점
- 자료가 정렬이 된 상태여야 한다는 점

### 시간 복잡도

- O(logn)
    - 자료를 반으로 계속 줄여가면서 탐색, O(n)에 비해 훨씬 빠른 속도




---
## 이진 탐색 트리 (Binary Search Tree)

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/204446617-6e41aa1c-399c-4b0c-ab69-74cd20d201b6.png" width="70%"></p>

### 정의
-  이진 트리에서 어떠한 규칙에 따라 나열한 트리이다. 

    -  이 규칙은 모든 노드에 대해서 **왼쪽 노드보다 오른쪽 노드가 더 크게 나열**하는 것이다.

### 특징

- 이진 탐색에 트리의 개념이 더해진 것으로 특정 값을 탐색하는 것에 빠른 성능을 보여준다.

- 이진 탐색 트리는 아래와 조건을 만족한다.

    1. 각 노드에 **중복되지 않는 키(key)** 가 있다.
    2. 루트노드의 왼쪽 서브 트리는 해당 노드의 키보다 작은 키를 갖는 노드들로 이루어져 있다.
    3. 루트노드의 오른쪽 서브 트리는 해당 노드의 키보다 큰 키를 갖는 노드들로 이루어져 있다.
    4. 좌우 서브 트리도 모두 이진 탐색 트리여야 한다. 

### 원리

- 탐색

    1. 루트 노드의 키와 찾고자 하는 값을 비교한다. 찾고자 하는 값이라면 탐색을 종료한다.
    2. 찾고자 하는 값이 루트 노드의 키보다 작다면 왼쪽 서브 트리로 탐색을 진행한다.
    3. 찾고자 하는 값이 루트노드의 키보다 크다면 오른쪽 서브트리로 탐색을 진행한다.

- 삽입(탐색과 과정 비슷)

    1. 삽입할 값을 루트 노드와 비교해 같다면 오류를 발생한다(중복 값 허용 X)
    2. 삽입할 값이 루트 노드의 키보다 작다면 왼쪽 서브 트리를 탐색해서 비어있다면 추가하고, 비어있지 않다면 다시 값을 비교한다.
    3. 삽입할 값이 루트노드의 키보다 크다면 오른쪽 서브트리를 탐색해서 비어있다면 추가하고, 비어있지 않다면 다시 값을 비교한다.

- 삭제

    1. 삭제하려는 노드가 단말 노드(leaf node, 자식이 없는 노드) 일 경우
        - 삭제할 노드의 부모 노드가 있다면 부모 노드의 자식 노드를 NULL로 만들고, 삭제할 노드를 삭제(메모리 해제) 해주면 된다.
    2. 삭제하려는 노드의 서브 트리가 하나인 경우(왼쪽 혹은 오른쪽 서브 트리)
        - 삭제할 노드의 자식노드를 삭제할 노드의 부모노드가 가리키게 하고 해당 노드를 삭제하면 된다. 
    3. 삭제하려는 노드의 서브 트리가 두 개인 경우
    	- 삭제할 노드 왼쪽 서브 트리의 가장 큰 자손과
        - 삭제할 노드 오른쪽 서브 트리의 가장 작은 자손을 비교하여 
        - 삭제할 노드와 가장 근사한 값을 가진 노드를 올려준다.

### 코드

- 삽입

```python

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root # current_node를 루트 노드로 초기화 시킨다.
        while True:
            if value < self.current_node.value: # 삽입하고자 하는 값이 current_node의 값보다 작을 때
                if self.current_node.left != None: # 현재 노드의 왼쪽 자식 노드가 있는지 확인한다.
                    self.current_node = self.current_node.left # 있으면 current_node를 갱신한다.
                else:
                    self.current_node.left = Node(value) # 없을 경우에는 current_node의 왼쪽 자식 노드에 삽입하고자 하는 노드를 삽입한다.
                    break
            else: # 삽입하고자 하는 값이 current_node의 값보다 클 때. 작을 때의 경우의 반대로 구현한다.
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
                    
```

- 탐색

```python

def search(self, value):
    self.current_node = self.root
    while self.current_node:
        if self.current_node.value == value:
            return True # current_node의 값이 찾고자 하는 값일 경우 True를 리턴한다.
        elif self.current_node.value > value: # current_node의 값이 찾고자 하는 값보다 더 클 경우
            self.current_node = self.current_node.left # 찾고자 하는 값은 현재 노드의 왼쪽 노드에 있는 것이므로 current_node를 왼쪽 자식 노드인 current_node.left로 갱신해준다.
        else:
            self.current_node = self.current_node.right # 반대의 경우는 current_node.right로 갱신한다.
    return False #  못 찾을 경우 마지막 current_node에는 None값이 들어가므로 while문을 빠져나오게 된다. 그리고 False를 리턴한다.
    
```

- 삭제

```python

def delete(self, value):
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
        is_search = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if is_search == False:
            return False
		
        # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right                

        # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
                
            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True
        
```

### 장점

- 배열보다 속도가 빠르다.
- 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다.

### 단점

- 최악의 경우 한쪽으로 편향된 트리가 될 수 있고, 시간복잡도가 O(n)에 가까워진다.
    - AVL 트리, 레드-블랙 트리로 해결 가능하다.

### 시간복잡도

- O(logN)

#

## 레드 블랙 트리(Red-Black Tree)

### 정의

- 자가 균형 이진 탐색 트리

    - 이진 탐색 트리는 균형을 맞추기 위해 여러 자료구조를 사용하는 데, 그 중 하나다.

### 특징

- 삽입,삭제 동안 트리의 모양이 **균형이 잡히도록 유지**한다.

    - worst case 에서도 모두 시간복잡도  O(log n) 이 보장되는 자료구조이다.

- 레드 블랙 트리는 아래의 조건을 만족한다.

    1. 모든 노드는 **빨간색** 혹은 **검은색**이다.
    2. **루트 노드**는 **검은색**이다.
    3. 모든 **리프노드**(NIL)들은 **검은색**이다.   (NIL : null  leaf , 자료를 갖지 않고 트리의 끝을 나타내는 노드)
    4. **빨간색 노드의 자식**은 **검은색**이다.
        - No Double Red (빨간색 노드가 연속적일 수 없다.)
    5. 모든 **리프 노드**에서의 **Black Depth**는 같다.
        - 리프 노드에서 루트 노드까지 가는 경로에서 만나는 검은색 노드의 개수는 같다.
    6. 삽입 하는 **새로운 노드**는 항상 **빨간색**이다.
    
    <p align="center"><img src="https://user-images.githubusercontent.com/113777043/210685885-c952cd4b-6316-44b4-a995-63f4a6d27bac.png" width = "70%"></p>
    

### 노드 종류

모두 N 노드 기준에서 바라본 노드임을 유의해야 한다.

- 삽입할 노드 : N
- 부모 노드 : P (N의 부모)
- 조상 노드 : G (N의 조상)
- 삼촌 노드 : U (N의 삼촌)

### 핵심 원리

- **Double Red** 를 피해야 한다. (빨간색 노드가 연속으로 2번 나타나는 것)

- Double Red 를 피하기 위한 전략 두 가지

    - **Restructing** : 삼촌 노드가 검은색인 경우
        1. 새로운 노드(N), 부모 노드(P), 조상 노드(G)를 오름차순으로 정렬
        2. 셋 중 중간 값을 부모 노드로, 나머지 둘을 자식 노드로 재배치
        3. 새로 부모가 된 노드를 검은색, 나머지 자식들을 빨간색으로 
        
    - **Recoloring** : 삼촌 노드가 빨간색인 경우
    
        1. 새로운 노드(N)의 부모(P)와 삼촌(U)을 검은색, 조상(G)을 빨간색으로 바꿈
            
            a.1 조상(G)이 루트 노드라면 검은색
            
            a.2 조상(G)을 빨간색을 바꿨을 때 또 Double Red가 발생한다면 다시 두 전략을 진행
            
            문제가 생기지 않을 때까지 반복
            

### 예제

- Double Red 가 발생하는 경우

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/209565551-1e5c6d0d-fa60-41b0-b697-a191e30388c4.jpg" width="80%"></p>

- 3을 삽입했더니, 2와 3부분에 Double Red 가 발생하였다.

### 1. Restructing

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/209565720-aa5241d3-69b0-4e8a-b31a-d911914222a6.jpg" width="80%"></p>

- 새로 삽입한 3의(N)의 삼촌 노드(U)가 검은색이므로 Restructing 전략을 수행한다.

1. 새로운 노드(N), 부모 노드(P), 조상 노드(G)를 오름차순으로 정렬

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/209565779-4608f8e0-7912-4c61-b0a8-12802755e46f.jpg" width="80%"></p>
    
2. 셋 중 중간 값을 부모 노드로 바꾼다. (3번 노드를 부모 노드로 재배치)
3. 새로 부모가 된 노드를 검은색으로 , 나머지를 빨간색으로 변경

Double Red 가 모두 해결되었다.

### 2. Recoloring

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/209565817-096dd8b8-6d65-4949-8d1b-f77cc693614f.jpg" width="80%"></p>

- 새로 삽입한 3번 노드(N)의 삼촌 노드가 빨간색이므로 Recoloring 전략을 수행한다.

1. 새로운 노드(N)의 부모(P)와 삼촌(U)을 검은색으로 변경, 조상(G)를 빨간색으로 변경

<p align="center"><img src="https://user-images.githubusercontent.com/88774925/209565825-abf9b81d-e07d-4ae4-b080-4ff2bd65ecfe.jpg" width="50%"></p>

2. 조상(G)가 루트 노드이므로 다시 검은색으로 변경
    - 만약, 이 때 Double Red가 발생한다면 상황에 맞게 두 전략을 사용해 반복한다.

### 장점

- 현재 고안된 이진 탐색 트리 중 가장 성능이 좋음

### 단점

- 구현의 복잡성

### 시간복잡도

- O(log n)

## 트라이(Trie)

### 정의

- **동적 집합**이나 **연관 배열**을 저장하는 데 사용되는 트리 자료 구조이다.

    - 주로 **문자열**을 저장하고 효율적으로 탐색하기 위한 검색 트리의 일종으로 사용된다.

### 특징

- 집합에 포함된 문자의 접두사들에 대응되는 노드들이 서로 연결된 트리이다.
- 주로 **문자열**이 키인 경우가 많다.
- 트리의 어떤 노드도 그 노드 자체와 연관된 키는 저장하지 않는다.
    - 대신 노드가 트리에서 차지하는 위치가 연관된 키를 정의한다.
- 노드의 모든 자손은 노드에 연관된 문자열의 공통 접두사를 공유한다.
- 루트 노드는 빈 문자열에 연관된다.

### 핵심 원리

1. 주어진 문자열에서 현재 문자를 가져온다.
2. 현재 문자로 이루어진 노드가 존재한다면, 그 노드의 자식 노드에서 다음 문자열을 탐색한다.
3. 현재 문자로 이루어진 노드가 없다면, 노드를 새로 할당 받은 후 그 노드를 통해 다음 문자열을 탐색한다.
4. 문자열의 마지막이 될 때까지 위의 과정을 반복한다.

### 예제

- 루트 노드는 빈 문자열에 연관되므로 비어있다.
- 주황색으로 된 노드들이 입력된 문자열이다.
- [be, bee, can, cat, cd]가 들어가 있다.

**"sscannbebee"**

<p align="center"><img src="https://user-images.githubusercontent.com/113777043/210564889-b59a3f23-10e6-4531-b424-3f6be39db3e0.png" width="60%"></p>

### 장점

- 문자열을 빠르게 찾을 수 있다.
- 문자열을 삽입하는 경우, 문자열의 길이만큼 노드를 따라가거나 추가하면 되기 때문에 효율적이다.
- 삽입 시, 자동으로 정렬된 효과를 볼 수 있다.

### 단점

- 필요한 메모리의 크기가 너무 크다.

    - **map**이나 **vector**를 이용하여 필요한 노드만 메모리를 할당하는 방식으로 해결할 수 있다.

### 시간복잡도

- 제일 긴 문자열의 길이를 **L** 총 문자열들의 수를 **M**이라 하자.
- 생성 시 시간복잡도: **O(M*L)**
    - 모든 문자열들을 넣어야하니 M개에 대해서 트라이 자료구조에 추가하는 것은 가장 긴 문자열 길이만큼 걸린다.
    - 삽입 자체의 시간 복잡도는 **O(L)** 이다.
- 탐색 시 시간복잡도: **O(L)**
    - 트리를 타고 들어갈 때, 가장 긴 문자열의 길이만큼만 탐색하기 때문이다.

### 활용

- 검색어 자동완성
- 사전 검색
- 문자열 검사


