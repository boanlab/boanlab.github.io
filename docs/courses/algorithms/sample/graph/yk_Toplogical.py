
from collections import deque


# 위상정렬 함수
def topologySort():
    result = [] # 결과 담을 리스트
    q = deque() # 덱 라이브러리 사용

    for i in range(1,v+1): # v : 노드의 수 , 1부터 시작한다고 가정
        if indegree[i] == 0:
            q.append(i)

    while q:

        current = q.popleft() # 큐에서 원소를 하나 꺼냄
        result.append(current)

        for i in graph[current]: # graph : 간선 정보를 담은 리스트
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


    for i in result:
        print(i, end =' ')


# 입력문
v,e = map(int, input().split())     # v: 노드 수 / e : 간선 수
indegree = [0] * (v+1) # 진입 차수 0으로 초기화 (노드는 1부터 시작한다고 가정)

graph = [[] for i in range(v+1)] # 각 노드 마다 연결된 간선 정보를 담는 리스트(2차원 배열로 구현)

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)   # 정점 a에서 b로 이동 가능 의미
    indegree[b] += 1     # 때문의 b의 진입차수를 1증가 시킨다.


topologySort()

'''test
7 8 (노드 수 / 간선 수)
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
1 2 5 3 6 4 7 
'''
