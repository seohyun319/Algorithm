# C9. 최단 경로 - 실전문제 '미래 도시'

import sys
put = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 회사간 1만큼 시간으로 연결된 도로 통해 이동 가능
# 방문판매원이 1번 회사에서 k번 회사를 거쳐 x번 회사로 가는 최소 이동 시간

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, put().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로(양방향 가능) 가는 비용은 1이라고 설정. 
    a, b = map(int, input().split())
    graph[a][b] = 1    
    graph[b][a] = 1    

# 최종 목적지 x와 거쳐갈 회사 k
x, k = map(int, put().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
answer = graph[1][k] + graph[k][x]

if answer >= INF:
    print(-1)
else: print(answer)