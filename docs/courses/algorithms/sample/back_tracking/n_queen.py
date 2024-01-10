n = int(input())
result = 0

# 퀸을 놓은 후, 그 이후 줄에 대해서 불가능한 칸 체크를 위한 메소드
def visit(x, y, in_visited):
    temp_visited = [visited[:] for visited in in_visited]

    for i in range(1, n-x):
        temp_visited[x+i][y] = True         # 아래 방향 체크

        if 0 <= y-i < n:
            temp_visited[x+i][y-i] = True   # 왼쪽 아래 대각선 체크
        if 0 <= y+i < n:
            temp_visited[x+i][y-i] = True   # 오른쪽 아래 대각선 체크
    
    return temp_visited

# q번째 줄에 퀸을 둘 수 있는 경우들을 확인하는 재귀함수
def recursion(q, _visited):
    global result

    for idx in range(q, n):
        # 한 줄 전체가 불가능한 경우, n개의 퀸을 모두 놓을 수 없으므로 재귀 종료
        if sum(_visited[idx]) == n:
            return 0
    
    # 마지막 줄에 도달한 경우
    if q == (n-1):
        result += n - sum(_visited[q])
        return 0
    
    # for문을 이용해 퀸을 둘 수 있는 모든 경우 완전 탐색
    for i in range(n):
        if not _visited[q][i]:              # 퀸을 둘 수 있는 경우
            temp = visit(q, i, _visited)    # 퀸을 뒸을 때 불가능한 칸들 체크
            recursion(q+1, temp)            # 재귀 호출

# 테스트
visited = [[False for _ in range(n)] for _ in range(n)]
recursion(0, visited)   # 0번째 줄부터 탐색 시작
# input: 8
print(result)           # expected output: 181
