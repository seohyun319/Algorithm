# gold5-18405. 경쟁적 전염

import sys
from collections import deque
input = sys.stdin.readline

# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
# 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력

n, k = map(int, input().split()) # NxN 크기의 시험관, 1번부터 K번까지의 바이러스 종류
graph = [[0]*(n + 1)] 
for _ in range(n):
    infos = [0] + list(map(int, input().split()))
    graph.append(infos)

s, x, y = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
virus_positions = []

def bfs():
    while virus_positions:
        v, a, b, t = virus_positions.popleft()
        if t == s: return
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 < nx <= n and 0 < ny <= n and graph[nx][ny] == 0:
                graph[nx][ny] = v
                virus_positions.append((v, nx, ny, t + 1))            

for i in range(1, n + 1):
    for j in range(1, n + 1):        
        if graph[i][j] != 0:
            virus_positions.append([graph[i][j], i, j, 0]) # virus_num, x, y, time

# 안에 내용이 0이 아닌 것을 넣고 시작
virus_positions.sort()
virus_positions = deque(virus_positions)

bfs()

print(graph[x][y])