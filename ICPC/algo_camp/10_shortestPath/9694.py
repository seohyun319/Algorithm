# gold3-9694. 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
# 입력값을 단방향 그래프로만 생각해서 틀림 + print 띄어쓰기 문제

import sys, heapq
input = sys.stdin.readline

# 최고의원을 만나기까지의 친밀도의 합 중에서 가장 작은 값을 구하기

t = int(input())
for i in range(t): 
    n, m = map(int, input().split()) # 관계의 개수, 정치인의 수
    graph = [[] for _ in range(m+1)]
    for _ in range(n):
        # 정치인, 그의 친구, 두 사람의 친밀도 
        # 친밀도: (최측근 [1] / 측근 [2] / 비즈니스관계 [3] / 지인 [4])
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
    INF = int(1e9)

    def dijkstra(start):
        q = []
        distance = [INF]*(m+1)
        distance[start] = 0
        heapq.heappush(q, (0, start, [start]))
        while q:
            dist, now, path = heapq.heappop(q)
            if now == m-1: return path
            if distance[now] < dist: continue
            for next_node, next_dist in graph[now]:
                cost = distance[now] + next_dist
                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node, path + [next_node]))
    
    met_order = dijkstra(0)
    if not met_order: met_order = [-1]
    print(f'Case #{i + 1}:', *met_order)     
    