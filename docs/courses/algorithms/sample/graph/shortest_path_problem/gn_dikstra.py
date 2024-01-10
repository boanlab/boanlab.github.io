n, m = map(int, input().split())    # n: 노드의 개수, m: 간선의 개수
start_node = int(input())           # 시작할 노드
INF = 1e8                           

graph = [[] for _ in range(n+1)]    # 주어진 그래프 정보 담는 그래프 리스트. 1부터 시작하므로 n+1만큼 반복
distance = [INF] * (n+1)            # 최단 거리 테이블 distance
visited = [False] * (n+1)           # 방문 체크를 위한 리스트 vistied            

for _ in range(m):
    depart, arrive, weight = map(int, input().split())  # depart: 출발노드, arrive: 도착노드, weight: 연결된 간선의 가중치
    graph[depart].append((arrive, weight))              # 거리 정보와 도착노드 저장

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

# 테스트
'''
input
5 6
1
5 1 1
1 2 1
1 3 3
2 3 1
2 4 5
3 4 2
'''
dijkstra(start_node)
print(distance) # expected output: [100000000.0, 0, 1, 2, 4, 100000000.0]