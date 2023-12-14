# silver2 유기농 배추
import sys

input = sys.stdin.readline
from collections import deque

# 배추 있는 곳에 배추흰지렁이 배치해야, 인접(상하좌우 기준)한 배추끼리는 이동 가능
# 배추 묶음에 배추흰지렁이 한 마리는 꼭 있어야 함
# 필요한 최소의 배추흰지렁이 개수 구하기

# m이 보통 세로 n이 보통 가로.

t = int(input())  # 테스트 케이스 개수
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    array[x][y] = 0  # 방문 처리
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 1:  # 방문할 곳
                array[nx][ny] = 0
                q.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 개수
    array = [[0] * n for _ in range(m)]
    sum = 0
    for _ in range(k):
        x, y = map(int, input().split())  # 배추 위치 좌표
        array[x][y] = 1
    for x in range(m):
        for y in range(n):
            if array[x][y] == 1:
                bfs(x, y)
                sum += 1
    print(sum)
