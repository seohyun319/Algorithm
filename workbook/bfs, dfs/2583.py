# silver1-2583. 영역 구하기
import sys

input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())  # 세로, 가로, 직사각형 개수
array = [[0] * n for _ in range(m)]
sum_list = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())  # 왼쪽 아래 x y, 오른쪽 위 x y
    for i in range(y1, y2):
        for j in range(x1, x2):
            array[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    sum = 1
    array[x][y] = 1  # 방문 처리
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 0:  # 방문할 곳
                array[nx][ny] = 1
                q.append((nx, ny))
                sum += 1
    sum_list.append(sum)


for x in range(m):
    for y in range(n):
        if array[x][y] == 0:
            bfs(x, y)

print(len(sum_list))
print(*sorted(sum_list))
