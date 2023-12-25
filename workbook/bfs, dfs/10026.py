# gold5 적록색약
import sys 
input = sys.stdin.readline
from collections import deque

n = int(input())
array = [list(input().rstrip()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
sum_x, sum_o = 0, 0 # 적록색약 아닌, 맞는 사람

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 색이 동일하고 방문한 적 없으면
                if array[nx][ny] == array[a][b] and visit[nx][ny] == 0: 
                    q.append((nx, ny))
                    visit[nx][ny] = 1 # 방문 처리

# 적록색약 아닌 사람
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            sum_x += 1

visit = [[0]*n for _ in range(n)] # 다시 초기화

for i in range(n):
    for j in range(n):
        # 빨간색일 경우 초록색으로 바꿔줌 (둘이 차이 없게 하려고)
        if array[i][j] == 'R':
            array[i][j] = 'G'

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            sum_o += 1

print(sum_x, sum_o)
