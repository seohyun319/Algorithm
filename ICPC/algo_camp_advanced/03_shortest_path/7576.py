# gold5-7576. 토마토

import sys 
from collections import deque
input = sys.stdin.readline

# 토마토가 모두 익는 데 걸리는 최소 일수 (익은 토마토와 인접하면 1일 후 익음)
# 토마토의 상태: 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

m, n = map(int, input().split()) # 가로 세로
array = [list(map(int, input().split())) for _ in range(n)] # 상자에 담긴 토마토
day = 0 # 걸리는 최소 일자
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

for x in range(n):
    for y in range(m):
        # 익은 토마토
        if array[x][y] == 1:
            q.append((x, y))

def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 빈 곳 방문
                if array[nx][ny] == 0:
                    array[nx][ny] = array[a][b] + 1
                    q.append((nx, ny))

bfs()

for x in range(n):
    for y in range(m):
        # 다 돌렸는데도 안 익은 게 남아있음
        if array[x][y] == 0:
            print(-1)
            exit()
    # 한 줄 기준 최대값과 그동안의 최대값 비교해 갱신
    day = max(day, max(array[x]))        

# 토마토 시작점이 1이었으니 다시 빼줌
print(day - 1)