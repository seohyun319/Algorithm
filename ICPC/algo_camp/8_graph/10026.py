# gold5-10026. 적록색약

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
see_rg, not_see_rg = 0, 0

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == graph[x][y]: # graph[x][y]는 이번에 찾는 연결된 영역에 해당하는 알파벳
                dfs(nx, ny)

# 비색약인
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            see_rg += 1 # 연결된 영역 하나 다 방문하고 옴

# 적록색약용 세팅: 초록을 빨강으로
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R" 

visited = [[0]*n for _ in range(n)] # 다시 초기화

# 색약인
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            not_see_rg += 1

print(see_rg, not_see_rg)
