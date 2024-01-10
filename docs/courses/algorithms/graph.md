---
layout: default
title: Graph
parent: Algorithms
grand_parent: Courses
---

# Graph
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# 그래프 (Graph)

### 용어
- 인접 행렬(Adjacency matrix)
  - 그래프의 노드를 2차원 배열로 만든 것이다.
  - NxN 불린 행렬(Boolean Matrix)로써 matrix[i][j]가 true라면 i에서 j로의 간선이 있다는 뜻이다.
  - 0과 1을 이용한 정수 행렬(Integer Matrix)도 사용 가능하다. 직접 연결 되어 있으면 1, 아니면 0이다.

- 다이나믹 프로그래밍(Dynamic Programming)
  - 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다.

  
## 그래프 표현
- 그래프를 구현하는 방법에는 두 가지 방식이 있다.
  - 인접행렬
  - 인접리스트

## 인접 행렬(Adjacency matrix)



### 특징
- 무방향 그래프를 인접 행렬로 표현하면, 이 행렬은 대칭 행렬(Symmetric Matrix)이 된다.

### 장점
- 두 정점에 대한 연결 정보를 조회할 때, 시간 복잡도는 O(1)이면 가능하다.
  - 2차원 배열 안에 모든 정점들의 간선 정보가 담겨있기 때문이다.
- 정점의 차수는 O(N) 안에 알 수 있다.
- 인접리스트에 비해 구현이 쉽다.

### 단점
- 모든 정점에 대한 간선 정보를 대입해야 하므로 O(N^2)의 시간복잡도를 가진다.
- 무조건 2차원 배열이 필요하기 때문에 필요 이상의 공간이 낭비된다.
- 어떤 정점에 인접한 정점을 찾기 위해서는 모든 노드를 전부 순회해야 한다.

### 예제
![인접 행렬](../data_structure/samples/graph/image/adjacency_matrix.png)

### 코드
```python
graph = [
  [0, 1, 1, 0],
  [1, 0, 1, 1],
  [1, 1, 0, 0],
  [0, 1, 0, 0]
]
```

## 인접 리스트(Adjacency list)

### 정의
- 인접 리스트는 모든 노드에 연결된 노드들의 정보를 차례대로 기록하는 방식이다.

### 특징
- 연결 리스트 자료구조를 이용한다(Python은 2차원 리스트 이용)

### 장점
- 연결된 것들만 기록하여 메모리를 효율적으로 사용한다.
- 어떤 노드의 인접한 노드들을 바로 알 수 있다.

### 단점
- 두 노드에 대한 연결 정보를 확인할 때 인접 행렬보다 느리다.

### 예제
![인접 리스트](https://user-images.githubusercontent.com/57708995/210236539-922215d1-e059-484e-803c-0f156c8a59f7.png)

### 코드
```python
graph = [[] for _ in range(4)]

# 노드 A
graph[0].append('B')
graph[0].append('C')

# 노드 B
graph[1].append('A')

...

graph = [['B', 'C'], ['A', 'C', 'D'], ['A', 'B'], ['B']]
```
---

## 그래프 순회 (Graph traversal)
- 모든 정점을 방문하는 알고리즘
- 동일한 정점이 처리되지 않도록 방문(visited) 표시 사용
- 대표적인 두 가지 방법 존재
	- 깊이 우선 탐색 (DFS)
 	- 너비 우선 탐색 (BFS)

## 깊이 우선 탐색(DFS)

### 정의

- 그래프에서 **깊이**를 우선적으로 탐색하는 알고리즘
- 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식

### 특징

- 자기 자신을 호출하는 순환 알고리즘 형태
- 스택 자료구조 사용
- 전위 순회 등 모든 트리 순회 방법은 DFS의 한 종류
- 어떤 노드를 방문했었는 지에 대한 여부 반드시 검증 필요
    - 무한 루프 가능성 방지
    

### 원리

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    - 방문처리는 visited(리스트) 등을 통해 구현한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다.
    
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    
3. 2번의 과정을 수행할 수 없을 때까지 반복한다.


<img src = "https://user-images.githubusercontent.com/88774925/209828825-d6370854-6881-4490-a0fe-264418ee4326.jpg" width = "670" height = "350" />

- 방문 처리된 노드 : 주황색
- 현재 처리하는 스택의 최상단 노드 : 파란색
- 먼저, 시작 노드인 1을 스택에 삽입하고 방문처리를 한다.
    - 스택 : [1]
- 스택 최상단 노드인 1에 방문하지 않은 인접노드는 2,3,8 번 노드이다. 그 중에서 **가장 작은** 2번 노드를 스택에 넣고 방문처리를 한다.
    - 스택 : [1,2]

<img src = "https://user-images.githubusercontent.com/88774925/209829183-ba8b565b-c3c1-427a-ab41-358416a01925.jpg" width = "630" height = "310" />



- 스택의 최상단 노드인 2번 노드에 방문하지 않은 7번 노드를 스택에 넣고 방문처리를 한다.
    - 스택 : [1,2,7]
- 스택의 최상단 노드인 7번 노드에 방문하지 않은 인접 노드인 6번을 스택에 넣는다. (작은 값을 먼저 넣음)
    - 스택 : [1,2,7,6]


<img src = "https://user-images.githubusercontent.com/88774925/209829227-d87ae810-eb10-493c-b9b2-0c77d1890455.jpg" width = "630" height = "310" />


- 스택의 최상단 노드인 6번 노드에 방문하지 않은 인접노드가 없으므로 **스택에서 6번 노드를 꺼낸다.**
    - 스택 : [ 1,2,7 ]
- 최상단 노드인 7번 노드에 방문하지 않은 인접노드인 8번 노드를 스택에 넣고 방문처리를 한다.
    - 스택 : [1,2,7,8]

이 과정을 반복하면 BFS 결과값은 1→2→7→6→8→3→4→5 이다.

### DFS vs BFS

**DFS**

- 루트노드에서 시작해 다음 분기로 넘어가기 전 모든 분기 탐색 (깊이 우선)
- 스택 자료구조 이용
- 재귀함수 사용
- BFS 보다는 간단하나 속도만 보면 느림
- 검색 대상의 **규모가 클 때**, 경로의 **특징을 저장**해야 할 때
    - 각각 경로의 특징을 저장 가능

**BFS**

- 루트노드에서 인접한 노드부터 탐색(너비 우선)
- 큐 자료구조 이용
- 검색 대상의 **규모가 크지 않고** **최단 거리**를 구해야 할 때 이용
    - 검색 시작 지점으로부터 검색 대상이 멀지 않을 때
    - 각각 경로의 특징 저장 불가능

### 코드(Stack)

```python
def dfs_iteration(graph, root):
    # visited = 방문한 노드 기록 리스트
    visited = []
    # stack 자료구조 이용
    stack = [root]
    
    while(stack): #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # node : 현재 방문하고 있는 노드
        
        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited
```

### 코드(Recursive)

```python
def dfs(graph, v, visited):     # v: 시작 노드를 매개변수로 입력 받는다. visited : 방문 처리 리스트

    visited[v] = True # 방문처리
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited) # 재귀호출을 이용하여 현재 노드와 연결된 다른 노드를 재귀적으로 방문
```

- 방문하지 않은 노드가 있다면 재귀적으로 가장 깊숙한 곳까지 방문했다가 다시 돌아와서
    
    다른 방향으로 깊이 방문하게 되는 방법
    

### 활용

- 순열과 조합 구현 시

## 너비 우선 탐색(BFS)

### 정의
- 시작 정점을 방문한 후 시작 정점에 인접한 모든 정점들을 우선 방문하는 알고리즘

### 특징
- **재귀적으로 동작하지 않는다**.
- 그래프 탐색의 경우 어떤 노드를 방문했는지 여부를 반드시 검사해야 한다.
  - 검사하지 않을 경우, 무한루프에 빠질 위험이 있다.
- BFS는 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용한다.
  - **선입선출(FIFO)** 원칙으로 탐색

### 원리
1. 루트에서 시작한다.
2. 루트 정점과 인접하고 방문된 적 없으며, 큐에 저장되지 않은 정점을 Queue에 넣는다.
3. 그러한 Queue에서 dequeue하여  가장 먼저 큐에 저장한 정점을 방문한다.

![너비 우선 탐색](sample/graph/image/bfs.png)

- **(1)~(5)**
  - 시작 정점을 방문한다.
  - 방문한 정점 체크를 위해 Queue에 방문된 정점을 삽입(enqueue)한다.
  - 초기 상태의 Queue에는 시작 정점만이 저장되므로 시작 정점의 이웃 노드를 모두 방문한다.
- **(6)**
  - Queue에서 꺼낸 정점과 인접한 정점들을 모두 차례로 방문한다.
  - 만약 인접한 정점이 없다면 한 번 더 dequeue한다.
  - Queue에 방문한 정점을 삽입(enqueue)한다.
- **(7)~(10)**
  - Queue가 소진될 때까지 계속한다.

### 코드
```python
# deque 라이브러리 불러오기
from collections import deque

# BFS 메서드 정의
def bfs (graph, vertex, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([vertex])
    # 현재 노드를 방문 처리
    visited[vertex] = True
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        value = queue.popleft()
        print(value, end = ' ')
        
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[value]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
```

### 활용
- 최단 경로 탐색

---
## 위상 정렬(Topological sort)

- 그래프 관련 알고리즘
- 정렬 알고리즘의 일종
- 순서가 정해져 있는 일련의 작업을 차례대로 수행할 때 사용할 수 있는 알고리즘
    - 커리큘럼(선후관계)
    

### 원리

1. 진입차수(indegree)가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때 까지 아래 과정을 반복한다.
    1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    2. 새롭게 진입차수가 0이된 노드를 큐에 넣는다.
    
    
<img src = "https://user-images.githubusercontent.com/88774925/209552066-bf57249f-bfa0-4a70-9ef1-88c82b29cba2.jpg" width="450" height="300"/>

| 노드 | 1  | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0 | 1 | 1 | 2 | 1 | 2 | 1 |

큐 : 1번 노드

- 진입차수가 0인 1번 노드를 처음으로 큐에 넣는다. (1번 과정)


<img src = "https://user-images.githubusercontent.com/88774925/209552880-609db32e-54ee-4324-9bff-04f5c0cef305.jpg" width="450" height="300"/>

| 노드 | 1  | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 진입차수 | 0 | 0 | 1 | 2 | 0 | 2 | 1 |

큐 : 노드 2 , 노드 5

- 큐에서 1번 노드를 꺼내고, 1번 노드에서 출발하는 간선을 그래프에서 제거한다.
- 새롭게 진입차수가 0이 된 노드를 큐에 넣는다. (2번 과정)
- 이 과정을 반복한다.
- **큐에서 빠져나간 노드**를 순서대로 출력한 것이 위상 정렬을 수행한 결과이다.
- 단, 위 처럼 한 단계에서 큐에 들어가는 원소가 2개 이상인 경우 위상 정렬의 답이 여러개 일 수 있다.
  - ex) 1→2→5 ..
  - ex) 1→5→2 ..

### 시간복잡도

- O(V+E)
    - 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거



---

# 최소 신장 트리

최소 신장 트리 구현 방법 

1. 크루스칼 알고리즘
2. 프림 알고리즘


### Union Find Algorithm (서로소 알고리즘)

- 크루스칼 알고리즘에 사용되는 알고리즘, 핵심 자료구조
- 서로소 집합 : 공통원소가 없는 두 집합
- union / find 연산으로 이루어진 알고리즘

  
<br/>   

### 1. **초기 상태**
- 각각의 노드들은 연결된 것이 없으므로 각각의 부모 노드는 자기 자신이다.
- 아래는 노드 3개의 부모테이블이다. 

| 1 | 2 | 3 |
| --- | --- | --- |
| 1 | 2 | 3 |

### 2. **노드를 연결하는 경우 (union) - 1번 노드 와 2번 노드**
- 1번 노드와 2번 노드를 연결한다. 그러면 부모테이블은 아래와 같아진다.

| 1 | 2 | 3 |
| --- | --- | --- |
| 1 | 1 | 3 |
- 보통 이처럼 부모노드는 수가 작은 쪽의 노드를 수가 큰 쪽의 부모노드에 넣는다.

### 3. **노드를 연결하는 경우 - 2번 노드와 3번 노드**

2번 노드와 3번 노드를 연결하면 아래처럼 될 것 같지만,
| 1 | 2 | 3 |
| --- | --- | --- |
| 1 | 1 | 2 |

틀린 부모테이블이다.

이 경우 노드의 트리 구조는 다음과 같다.  


<img src = "https://user-images.githubusercontent.com/88774925/209554730-7075720d-a7cc-4c0d-b8fb-c949faa0f48c.jpg" width="270" height="250"/>


하지만, **2번 노드의 루트 노드는 1번 노드**이므로 3번의 부모 노드도 1번 노드이어야 한다.

서로소 알고리즘에서 **재귀 호출**을 사용하는 이유가 여기서 나타난다.

즉, 3번은 부모노드인 2번을 호출

2번은 부모노드인 1번을 호출

1번은 부모노드인 1번을 호출하여 return 하게 된다. 즉 3번의 부모 노드도 1번으로 바뀐다.

따라서 올바른 부모 테이블과 트리 구조는 다음과 같다.

| 1 | 2 | 3 |
| --- | --- | --- |
| 1 | 2 | 1 |

<img src = "https://user-images.githubusercontent.com/88774925/209555457-6a2415c3-9cef-4998-80ee-86ca35973340.jpg" width="270" height="250"/>


<br/>    


### 서로소 알고리즘 코드

```python

# 특정 원소가 속한 집합을 찾는 Find
def findParent(parent,x):
	
	# 루트 노드가 아니면, 루트 노드를 찾아야 한다. (재귀호출 사용)
	if parent[x] != x:
			parent[x] = findParent(parent,parent[x]
	return parent[x]

# 두 원소가 속한 집합을 합치는 Union
def unionParent(parent,a,b):
	a = findParent(parent,a)
	b = findParent(parent,b)
	
	if a<b: # 값이 작은 노드를 큰 값의 부모 노드로 설정
		parent[b] = a

	else:
		parent[a] = b

```
  
<br/>   


## Kruskal Algorithm(크루스칼 알고리즘)

- 크루스칼 알고리즘은 최소 신장 트리를 구하는 방법이다.
- **가장 적은 비용으로 모든 노드를 연결하는 것**이 핵심 목표 이다.
- 그리디 알고리즘의 한 종류이다.

### 원리

1. 간선 값을 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 사이클을 발생시키는 지 확인한다.
    1. **사이클이 발생하지 않는 경우**엔 최소 신장 트리에 포함시킨다.
    2. **사이클이 발생하는 경우** 포함시키지 않는다.
3. 모든 간선에 대하여 2번 과정을 반복한다.

이 과정을 위해 앞서 언급한 서로소 알고리즘이 사용된다.

**find 함수** : 사이클이 발생하는 지 판단 

- 두 노드의 루트 노드가 같다면 사이클을 발생시키므로 집합에 포함시키지 않아야 한다.

**union 함수** : 두 노드가 속한 집합을 합치는 연산 수행


### 시간 복잡도

- 간선의 개수가 E개 일 때 O(ElogE) 의 시간복잡도를 가진다.
    - 간선을 정렬하는 작업 때문이다.
    - E개의 데이터를 정렬할 때의 시간 복잡도 : O(ElogE)


<br/>

## 프림 알고리즘(Prim)

### 정의

- 크루스칼과 마찬가지로 최소 비용 신장 트리를 구하는 알고리즘
- 임의의 시작 정점을 기준으로 가장 작은 간선과 연결된 정점을 선택하며 확장시키는 알고리즘

### 크루스칼 vs 프림

**크루스칼**

- 간선 위주의 알고리즘
- 간선을 오름차순으로 정렬해두고 시작
- 간선을 차례로 대입하면서 트리를 구성하므로, 사이클이 이루어지는 지 항상 확인 필요
    - 서로소 알고리즘을 통해 수시로 사이클 체크

**프림**

- 정점 위주의 알고리즘
- 임의이 시작점에서 가까운 정점을 선택하면서 트리를 구성하므로 사이클을 이루지 않음

간선 수가 적은 희소 그래프 : 크루스칼 알고리즘이 적합

간선이 많은 밀집 그래프 : 프림 알고리즘이 적합

### 원리

1. 임의의 시작 노드를 선택한다. 이 노드를 visited 리스트에 담는다.(방문표시)
2. 방문한 노드(visited 리스트에 있는) 와 방문하지 않은 노드 사이의 간선 중 최소인 간선을 찾는다.
3. 그 간선이 연결하는 두 노드 중, visited 리스트에 없는 노드를 visited에 넣는다.
4. 모든 노드가 visited에  포함될 때 까지 2,3 과정을 반복한다.

참고 : visited는 보통 boolean 배열로 구현

즉, 방문한 노드 중에서 방문하지 않은 노드로 잇는 최소의 간선을 찾고 잇는다.

때문에 사이클을 별도로 체크할 필요가 없어진다.

<img src = "https://user-images.githubusercontent.com/88774925/209829972-2911176f-9296-43c0-8529-1779f0870af4.jpg" width = "600" height = "350" />

- 임의로 1번 노드를 시작노드로 가정했을 때, 1번으로 부터 최소 간선인 2번 노드로 가는 간선을 선택
    - visited = [1] → [1,2] 으로 업데이트
- visited에 있는 노드를 잇는 간선 중 최소 간선인 2-6 간선을 선택
    - visited = [1,2] → [1,2,6] 으로 업데이트
    - 
<img src =  "https://user-images.githubusercontent.com/88774925/209830230-7b108ddb-08af-4042-8432-e7053fb6390d.jpg" width = "600" height = "350" />


- 다음 간선은 6-4(23) 선택
    - visited = [1,2,6] → [1,2,4,6] 으로 업데이트
- 다음 간선은 4-3(7) 선택
    - visited = [1,2,4,6] → [1,2,3,4,6] 으로 업데이트

<img src = "https://user-images.githubusercontent.com/88774925/209830290-3252a6ed-91d6-464c-a051-46a9f8aac153.jpg" width = "600" height = "350" />

- 다음 간선은 4-7(13)을 선택
    - visited = [1,2,3,4,6] → [1,2,3,4,6,7] 으로 업데이트
- 그 다음 간선은 6-7[(25)를 선택하려 했으나 **모두 visited에 있는 노드(방문한 노드)**
    
    따라서, **선택할 수 없다**. (2-3도 마찬가지)
    
    - 크루스칼 처럼 사이클을 계산할 필요 없음
- 따라서, **6-5(53) 간선을 선택**해야 함
    - visited = [1,2,3,4,6] → [1,2,3,4,5,6,7]

<img src = "https://user-images.githubusercontent.com/88774925/209830342-61a2d80b-4bc0-4aed-929d-caff19fda98d.jpg" width = "600" height = "350" />

- 모든 노드가 visited에 들어갔으므로 과정 종료
- 크루스칼 알고리즘 결과와 동일함

### 구현 관점

- 구현 관점에선 다음과 같다.(우선순위 큐 사용)

<img src = "https://user-images.githubusercontent.com/88774925/209830460-88e4db3a-0a05-48c1-84f2-7f4a50584c3e.jpg" width = "470" height = "477" />



- graph : 정점과 간선의 정보를 담은 리스트
    - 크루스칼은 간선 수만큼만 저장했지만 프림에선 모든 정점에 대해서 각각 저장
- priority queue : 우선순위 큐를 사용하여 cost , w 를 저장
- visited : 방문 판단 리스트로 여기서는 0으로 false, 1로 true를 나타냄

### 코드

```python
def prim(graph, start_node):
    visited[start_node] = 1 # 방문한 노드는 1로 방문 표시
    candidate = graph[start_node] # 인접 간선을 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst = [] # mst(결과)
    total_cost = 0 # 전체 가중치

    while candidate: # 인접 간선에 대해 반복
        cost, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
        if visited[v] == 0: # 방문하지 않았다면
            visited[v] = 1 # 방문 갱신
            mst.append((u,v)) # mst 삽입
            total_cost += cost # 전체 가중치 갱신

            for edge in graph[v]: # 다음 인접 간선 탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (사이클 방지)
                    heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입

    return total_cost
```

### 시간복잡도

- O(n2)




---

# 최단 경로 탐색

## 다익스트라(Dijkstra) 알고리즘

### 정의 

- 다이나믹 프로그래밍을 이용한 최단 경로 찾기 알고리즘이다. 
- 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단경로를 알려준다.
  - 단, 음의 간선이 있을 경우 사용할 수 없는 알고리즘이다.

### 원리
1. 출발 노드 설정
   - 최단 거리 테이블을 초기화
2. 출발 노드를 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중에서 가장 비용이 적게 드는 노드 선택
4. 해당 노드를 거쳐 특정한 노드로 가는 간선 비용을 계산하여 더 적은 비용이 든다면 최소 비용 갱신
   - 최단 거리 테이블 업데이트
5. 3, 4번 과정 반복

### 예제
1. 출발 노드 설정

![다익스트라_1](sample/graph/image/dikstra_1.png)

| 노드 번호 | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- |---| --- | --- | --- | --- |
| 거리 | 0 | INF | INF | INF | INF | INF |

- 시작 노드를 1번 노드로 가정한다.
- 1번 노드로부터 각 노드들 간의 거리를 테이블로 나타냈다.
- 1번 노드로의 거리는 0이기 때문에 0으로 업데이트 해주고, 나머지 값은 무한(INF)로 초기화시켜준다.

2. 출발 노드를 기준으로 각 노드의 최소 비용 저장

![다익스트라_2](sample/graph/image/dikstra_2.png)

| 노드 번호 | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- |---| --- | --- | --- | --- |
| 거리 | 0 | 2 | 5 | 1 | INF | INF |

- 시작 노드(1번 노드)로부터 도달할 수 있는 인접 노드들의 거리를 테이블에 갱신시켜준다.

3. 방문하지 않은 노드 중에서 가장 비용이 적게 드는 노드 선택

![다익스트라_3](sample/graph/image/dikstra_3.png)

- 시작 노드(1번 노드)와 가장 최단 거리인 4번 노드를 다음에 탐색할 노드로 선택한다.
  - 위 그림에서 회색 노드는 방문한 노드, 점선으로 된 간선은 이미 처리한 간선이다.

4. 해당 노드를 거쳐 특정한 노드로 가는 간선 비용을 계산하여 더 적은 비용이 든다면 최소 비용 갱신

| 노드 번호 | 1 | 2 | 3              | 4 | 5                | 6  |
| --- | --- |---|----------------| --- |------------------| --- |
| 거리 | 0 | 2 | **min(5,1+3)** | 1 | **min(INF,1+1)** | INF |

- 앞 단계에서 4번 노드를 선택했다. 이 때 4번 노드는 3, 5 노드와 간선으로 연결되어 있다.
  - 3번 노드까지 가는 비용은 시작 노드에서 직행으로 갈 때는 5
  - 4번 노드를 거쳐 간다면, 1번 노드에서 4번 노드로 가는 비용 1에 4번 노드에서 3번 노드로 가는 비용 3이 든다. 즉, 1+3만큼 든다.
  - 이 중 최소비용 경로를 찾기 위해 **min(5,1+3)**을 해준다.
  - 5번 노드도 3번 노드와 같은 방법을 거친다.

| 노드 번호 | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- |---|---| --- |---| --- |
| 거리 | 0 | 2 | 4 | 1 | 2 | INF |

- 위 방식을 거친 후 나온 최소 경로로 테이블을 갱신해준다.
  - 3번 노드로 가는 최소 비용 경로는 **1 -> 4 -> 3**으로 4(1+3)이다.
  - 5번 노드로 가는 최소 비용 경로는 **1 -> 4 -> 5**으로 2(1+1)이다.
- 4번 노드 탐색이 끝난 후 다음에 탐색할 노드를 선정한다.
  - 가장 마지막으로 갱신된 거리 테이블 기준으로 방문하지 않은 노드들 중 비용이 적은 노드로 선정한다.
  - 이 예제에서는 2와 5번 노드가 동일한데, 이 때는 노드 번호가 작은 순서를 먼저 탐색하는 걸로 한다.

5. 3, 4번 과정 반복

![다익스트라_4](sample/graph/image/dikstra_4.png)

| 노드 번호 | 1 | 2 | 3              | 4               | 5                | 6  |
| --- | --- |---|----------------|-----------------|------------------| --- |
| 거리 | 0 | 2 | **min(4,2+3)** | **min(1, 2+2)** | 2 | INF |

| 노드 번호 | 1 | 2 | 3 | 4 | 5 | 6  |
| --- | --- |---|---| --- |---| --- |
| 거리 | 0 | 2 | 4 | 1 | 2 | INF |

- 3번과 4번 과정을 거쳐 2번 노드를 거쳐가는 간선 비용을 계산하고, 테이블을 갱신해준다.


### 코드

- 두 구현 방식에 동일하게 필요한 입력값

```python
import heapq                        # 최소힙을 이용한 구현에 필요한 패키지

n, m = map(int, input().split())    # n: 노드의 개수, m: 간선의 개수
start_node = int(input())           # 시작할 노드
INF = 1e8                           

graph = [[] for _ in range(n+1)]    # 주어진 그래프 정보 담는 그래프 리스트. 1부터 시작하므로 n+1만큼 반복
distance = [INF] * (n+1)            # 최단 거리 테이블 distance  
visited = [False] * (n+1)           # 방문 체크를 위한 리스트 vistied. 순차탐색을 이용한 구현에 필요

for _ in range(m):
    depart, arrive, weight = map(int, input().split())  # depart: 출발노드, arrive: 도착노드, weight: 연결된 간선의 가중치
    graph[depart].append((arrive, weight))              # 거리 정보와 도착노드 저장
```


- 순차탐색을 이용한 구현

```python
# 해당 노드에서 최단 거리의 노드를 찾는 메소드
def get_smallest_node():
    min_value = INF
    idx = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    
    return idx

# 순차 탐색을 이용한 다익스트라 알고리즘 구현
def dijkstra(start):
    distance[start] = 0     # 시작 노드는 0으로 초기화
    visited[start] = True   # 시작 노드 방문 체크

    for i in graph[start]:  # 시작 노드와 연결된 노드들의 거리 입력
        distance[i[0]] = i[1]
    
    for j in range(n-1):
        now = get_smallest_node()   # 거리가 구해진 노드 중 최단 거리인 노드 찾기
        visited[now] = True         # 방문 체크
    
        for k in graph[now]:
            if distance[now] + k[1] < distance[k[0]]:   # 기존 테이블의 값보다 더 작은 거리가 나온 경우
                distance[k[0]] = distance[now] + k[1]   # 최단 거리 테이블을 갱신

```

- 최소힙을 이용한 구현

```python
# 최소힙을 이용한 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []                        
    heapq.heappush(q, (0, start))   # 우선순위, 값 형태로 들어간다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)    # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if distance[now] < dist:    # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue                # 다음으로 넘어감
    
        for i in graph[now]:                # 반복문을 통해 연결된 모든 노드 탐색
            if dist+i[1] < distance[i[0]]:  # 기존에 입력된 거리보다 큰 경우
                distance[i[0]] = dist+i[1]  # 최단 거리 테이블을 갱신
                heapq.heappush(q, (dist+i[1], i[0]))
```

### 시간복잡도
- 순차탐색을 이용한 구현: O(n^2)
- 최소힙을 이용한 구현: O(N * logN)

### 활용
- GPS
___

## 벨만-포드 알고리즘(Bellman-Ford)

### 정의

- 한 노드에서 다른 노드까지의 최단 거리를 구하는 알고리즘
- 간선의 가중치가 **음수**일 때도 최단 거리를 구할 수 있음
- 음수 간선이 포함된 상황이라면 다익스트라가 아닌 벨만-포드를 사용해야 한다.

### 다익스트라 vs 벨만-포드

<img src = "https://user-images.githubusercontent.com/88774925/209627939-2a619387-d5db-4d09-ab22-c755bd400380.jpg" width = "600" height = "300" />

**음수 간선의 순환**

- 다익스트라 , 벨만-포드 차이점을 알기 위해 필요한 개념
- 음수 간선이 포함되었을 때 두 가지 경우가 있다.
    - 음수 간선은 있지만 음수 간선 순환은 존재하지 않는 경우
    - **음수 간선 순환**도 존재하는 경우
- 위 그림에서 파란색으로 표시된 2,3,5번 노드에서 음의 간선을 포함한 **사이클**이 발생(**음수 간선 순환 발생**)
    - 이 사이클 때문에 1번 노드(시작노드)를 제외한 **모든 노드의 최소 비용이 -∞** 이다.

**다익스트라**

- 매번 **방문하지 않은 노드 중**에서 최단 거리의 노드를 선택, **한 단계씩** 구해나감
- 음수 간선이 존재하는 경우 최단 경로를 구할 수 없음
- 시간복잡도가 빠름 OElogV (우선순위 큐 사용 시)

**벨만-포드**

- **매 단계마다 모든 간선**을 확인하면서 최단 거리를 구해나감
- **음수 간선**이 존재해도 최단 경로를 구할 수 있음
    - 음수 간선 순환도 탐지 가능(음수 간선에 의한 사이클 발생)
- 시간복잡도가 상대적으로 느림 O(VE)

### 원리
- 기본 원리는 다익스트라 알고리즘과 같으나, 모든 간선을 체크한다는 것만 다르다.
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 다음 과정을 N-1 번 반복한다.
    1. 전체 간선 E개를 하나씩 확인한다.
    2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.

- 3번 과정을 한 번 더 수행하면, 음수 간선 순환 발생 체크도 가능하다.
    - 이때 최단 거리 테이블이 갱신되면 음수 간선 순환이 존재하는 것이다.
    

### 코드

```python
def bf(start):

    dist[start] = 0            

    # 전체 n번의 라운드 반복
    for i in range(n):
        # 매 반복마다 모든 간선 확인
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[cur] + cost < dist[next_node]
                dist[next_node] = dist[cur] + cost

                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == n-1:
                    return True
    return False

```

- dist : 최단 거리 테이블(리스트)
- INF : 무한
- edges : 모든 간선에 대한 정보를 담은 리스트
    - 2차원 배열로 ((a,b,c)) 형태로 저장됨
    - a번 노드에서 b번 노드로 가는 비용이 c 임을 의미


---

# 네트워크 유량(Network Flow)

### 정의
- 그래프에서 두 정점 사이에 얼마나 많은 유량(Flow)을 보낼 수 있는지 계산하는 알고리즘

### 용어
- 용량(Capacity)
  - **c(u, v)**: 정점 u에서 v로 전송할 수 있는 최대 용량
- 유량(Flow)
  - **f(u, v)**: 정점 u에서 v로 실제 흐르고 있는 유량
- 잔여 용량(Residual Capacity)
  - **r(u, v)** = c(u, v) - f(u, v)
  - 간선의 용량과 실제로 흐르는 유량의 차이
- 소스(Source)
  - **s**: 모든 유량이 시작되는 정점
- 싱크(Sink)
  - **t**: 모든 유량이 도착하는 정점
- 증가 경로
  - 소스에서 싱크로 유량을 보낼 수 있는 경로

### 특징(기본 속성)
- **용량 제한 속성**
  - f(u, v) <= c(u, v)
  - 유량은 용량보다 작거나 같다.
- **유량의 대칭성**
  - f(u, v) = -f(u, v)
  - u에서 v로 유량이 흐르면, v에서 u로 음수의 유량이 흐르는 것과 동일하다.
- **유량의 보존성**
  - 각 정점에 들어오는 유량과 나가는 유량은 같다.

### 유량 상쇄

**정의**
- 모든 경로에 존재하는 기존의 간선들과 반대되는 방향의 간선을 추가한 뒤, 각 간선으로 흘려보낸 반대 방향의 간선으로도 음의 유량을 흘려보냄으로써 유량을 상쇄시키는 것 

**특징**
- 실제로는 불가능하지만, 음의 유량을 기록함으로써 잔여 용량을 남겨 추가적인 경로를 탐색하도록 하기 위한 작업이다.
- 두 정점이 서로에게 유량을 보내주는 것은 의미가 없기 때문에 성립 가능하다.
- 소스에서 링크로 가는 총 유량도 변하지 않는다.

## 포드-폴커슨(Ford-Fullkerson) 알고리즘

### 정의
- DFS를 이용하는 최초의 네트워크 유량 알고리즘으로 원리와 구현이 간단하다.

### 원리
1. 네트워크에 존재하는 모든 간선의 유량을 0으로 초기화하고, 역방향 간선의 유량도 0으로 초기화한다.
2. 소스에서 싱크로 갈 수 있는 잔여 용량이 남은 경로를 DFS로 탐색한다.
3. 해당 경로에 존재하는 간선들의 잔여 용량 중 가장 작은 값을 유량으로 흘려보낸다.
4. 해당 유량에 음수값을 취해, 역방향 간선에도 흘려보낸다.(유량 상쇄)
5. 더 이상 잔여 용량이 남은 경로가 존재하지 않을 때까지 반복

### 예제

1. 네트워크에 존재하는 모든 간선의 유량을 0으로 초기화하고, 역방향 간선의 유량도 0으로 초기화한다.

![포드-폴커슨_1](sample/graph/image/ford_fullkerson_1.png)

- 1번 노드를 소스, 4번 노드를 싱크라 가정한다.

2. 소스에서 싱크로 갈 수 있는 잔여 용량이 남은 경로를 **DFS**로 탐색한다.
- **DFS**를 사용해, 소스에서 싱크로 갈 수 있는 경로 중 하나인 **1 - 2 - 3 - 4**가 증가 경로로 먼저 탐색된다 가정하자.
  - r(1, 2) = c(1, 2) - f(1, 2) = 1 - 0 = 1
  - r(2, 3) = c(2, 3) - f(2, 3) = 1 - 0 = 1
  - r(3, 4) = c(3, 4) - f(3, 4) = 2 - 0 = 2

3. 해당 경로에 존재하는 간선들의 잔여 용량 중 가장 작은 값을 유량으로 흘려보낸다.

![포드-폴커슨_2](sample/graph/image/ford_fullkerson_2.png)

- 2번에서 찾은 경로에 존재하는 간선들에 최소 유량을 흘려보낸 상황이다.

4. 해당 유량에 음수값을 취해, 역방향 간선에도 흘려보낸다.(유량 상쇄)

- 만약 유량 상쇄를 하지 않는다면, 어떠한 문제가 일어나는지 확인해보자.

![포드-폴커슨_3](sample/graph/image/ford_fullkerson_3.png)

- 1 - 2 - 3 - 4 경로를 증가경로로 유량을 흘려보낸 후, 다음 증가 경로로 1 - 3 - 4로 결정하고 유량을 흘려 보낸 상황이다.
  - r(1, 3) = c(1, 3) - f(1, 3) = 3 - 0 = 3
  - r(3, 4) = c(3, 4) - f(3, 4) = 2 - 1 = 1
- 유량 상쇄가 없기 때문에 1 - 3과 2 - 4 간선에 잔여 용량이 있지만, 더 이상 탐색할 수 없다.
  - 따라서 이러한 문제를 해결하기 위해 유량 상쇄가 필요하다.

5. 더 이상 잔여 용량이 남은 경로가 존재하지 않을 때까지 반복

![포드-폴커슨_4](sample/graph/image/ford_fullkerson_4.png)

- 다음과 유량 상쇄를 적용하면, 남은 경로가 존재하지 않을 때까지 반복할 수 있다.
