# gold4-11404. 플로이드

import sys
input = sys.stdin.readline

# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값
# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0 

for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
    # 더 적은 비용으로 갱신 (노선이 하나가 아닐 수 있어서)
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# ’A에서 B로 가는 최소 비용’과 ‘A에서 K를 거쳐 B로 가는 비용을 비교하여 더 작은 값으로 갱신하겠다
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF: 
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()