# silver1-1926. 그림

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

# 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
paint = 1
paint_list = []
visited = [[0]*m for _ in range(n)]

def dfs(x, y):
    global paint
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            paint += 1
            dfs(nx, ny)
    return paint

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            paint_list.append(dfs(i, j))
            paint = 1

print(len(paint_list))

if paint_list: print(max(paint_list))
else: print(0)

