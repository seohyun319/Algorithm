#C5. DFS/BFS - 실전문제 '미로 탈출' - 2번째

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) 
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# (1, 1)에서 (n, m)으로 간다고 할 때 움직여야 할 칸의 최소 개수
# 0은 괴물, 1은 가도 됨

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 안 감
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물 있으면 안 감
            if graph[nx][ny] == 0:
                continue
            # 처음 가면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 기존거에 더해야함
                q.append((nx, ny))

bfs(0, 0)
print(graph[n-1][m-1])


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111