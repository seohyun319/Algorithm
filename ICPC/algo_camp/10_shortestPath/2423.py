# gold1-2423. 전구를 켜라

import sys, heapq
input = sys.stdin.readline
INF = int(1e9) # 무한

# 전원은 왼쪽 위 모서리에 연결되어 있고, 전구는 오른쪽 아래 모서리에 연결
# 전구는 전원에서 전구로 가는 경로가 있을 때만 불이 켜짐
# 전구에 불을 켜기 위해 돌려야 하는 칸의 개수의 최솟값
# 문제에서 주어진 경로가 0 뒤집은 경로가 1로 하면 그거로 거리 구할 수 있음. 

n, m = map(int, input().split()) # N × M 직사각형 크기의 전자 회로
graph = [[[] for _ in range(m+1)] for _ in range(n+1)]
distance = [[INF] * (m+1) for _ in range(n + 1)]

for i in range(n):
    row = input()
    for j in range(m):
        # 주어진 대로 이동하면 비용 0, 뒤집으면 비용 1
        if row[j] == '/':
            top = 0 # 오른쪽 위로 향하는 대각선 -> 본인 비용 0
            bottom = 1 # 왼쪽 아래로 향하는 대각선 -> 뒤집어야 하니까 비용 1
        else: # "\"
            top = 1 # 위로 향하는 대각선 -> 뒤집어야 해서 비용 1
            bottom = 0
        graph[i][j].append((i+1, j+1, bottom)) # \
        graph[i+1][j+1].append((i, j, bottom))
        graph[i+1][j].append((i, j+1, top)) # /
        graph[i][j+1].append((i+1, j, top))        

def dijkstra():
    distance[0][0] = 0
    q = [(0, 0, 0)]
    while q:
        dist, i, j = heapq.heappop(q)
        if distance[i][j] != dist: continue
        for new_i, new_j, new_dist in graph[i][j]:
            if distance[new_i][new_j] > dist + new_dist:
                distance[new_i][new_j] = dist + new_dist
                heapq.heappush(q, (dist + new_dist, new_i, new_j))

if (n + m) % 2 == 1:
    print("NO SOLUTION")
else: 
    dijkstra()
    print(distance[-1][-1])