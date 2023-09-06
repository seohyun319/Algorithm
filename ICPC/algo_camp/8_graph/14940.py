# silver1-14940. 쉬운 최단거리

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n세로 m가로
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):    
        if graph[i][j] == 0: print(0, end=' ')
        else: print(graph[i][j] - 2, end=' ') 
    print()
