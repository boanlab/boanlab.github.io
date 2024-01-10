

def dfs(graph, v, visited):     # v: 시작 노드를 매개변수로 입력 받는다. visited : 방문 처리 리스트

    visited[v] = True # 방문처리
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited) # 재귀호출을 이용하여 현재 노드와 연결된 다른 노드를 재귀적으로 방문



graph = [
    [], # 보통 1번 노드부터 시작하므로 비워둠
    [2,3,8],
    [1,7]
    [1,4,5]
    [3,5]
    [3,4]
    [7],
    [2,6,8]
    [1,7]
]

visited = [False] * 9 # 방문 표시할 리스트

dfs(graph,1,visited) # 시작 노드를 1로 지정하고 dfs 함수 호출

    
