# silver1-2583. 영역 구하기

import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n세로 m가로
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
area = 1
area_list = []

def dfs(x, y):
    global area
    graph[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            area += 1
            dfs(nx, ny)
    return area

def bfs(x, y):
    global area
    q = deque()
    q.append((x, y))
    graph[y][x] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((nx, ny))
                area += 1
    return area

for i in range(m):
    for j in range(n):
        if graph[j][i] == 0:
            # area_list.append(dfs(i, j))
            area_list.append(bfs(i, j))
            area = 1

print(len(area_list))
print(*sorted(area_list))
