# silver1-1743. 음식물 피하기
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 세로 가로 음식물 쓰레기 개수
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
sum = 0
size = []
for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global sum
    visited[x][y] = 1
    sum += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:  # 방문할 곳
                dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            size.append(sum)
            sum = 0

print(max(size))
