# silver1-2178. 미로 탐색
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())  # 세로, 가로
array = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:  # 방문할 곳
                array[nx][ny] = array[a][b] + 1
                q.append((nx, ny))


bfs(0, 0)

print(array[n - 1][m - 1])  # 도착 위치
