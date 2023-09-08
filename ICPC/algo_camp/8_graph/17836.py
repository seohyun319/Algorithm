# gold5-17836. 공주님을 구해라!

import sys
from collections import deque
input = sys.stdin.readline

# 공주에게 도달할 수 있는 최단 시간을 출력
# 그람(전설의 명검)이 있는 곳에 도착하면 바로 사용할 수 있다. 그람이 부술 수 있는 벽의 개수는 제한이 없다.

n, m, t = map(int, input().split())
graph = [[0]*(m + 1)]
for _ in range(n):
    castle = [0] + list(map(int, input().split())) # 0은 빈 공간, 1은 마법의 벽, 2는 그람
    graph.append(castle)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 최단경로 구하기
# 검 있는 케이스, 없는 케이스 중 최단 고르기

def bfs(x, y):
    min_time = t + 1 # min_time은 목표 시간 + 1보다 무조건 작아야 함
    q = deque()
    q.append((x, y, 0))
    graph[x][y] = 1
    while q:
        a, b, time = q.popleft()        
        if a == n and b == m: # 공주한테 도착
            min_time = min(min_time, time)
            continue
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, time + 1)) 
                    graph[nx][ny] = 1
                if graph[nx][ny] == 2:
                    min_time = min(min_time, time + 1 + (n - nx) + (m - ny))
    return min_time

answer = bfs(1, 1)

if answer <= t: print(answer)
else: print("Fail")
