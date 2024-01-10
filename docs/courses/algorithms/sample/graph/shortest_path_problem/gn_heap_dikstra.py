import heapq

n, m = map(int, input().split())    # n: 노드의 개수, m: 간선의 개수
start_node = int(input())           # 시작할 노드
INF = 1e8                           

graph = [[] for _ in range(n+1)]    # 주어진 그래프 정보 담는 그래프 리스트. 1부터 시작하므로 n+1만큼 반복
distance = [INF] * (n+1)            # 최단 거리 테이블 distance  

for _ in range(m):
    depart, arrive, weight = map(int, input().split())  # depart: 출발노드, arrive: 도착노드, weight: 연결된 간선의 가중치
    graph[depart].append((arrive, weight))              # 거리 정보와 도착노드 저장

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

