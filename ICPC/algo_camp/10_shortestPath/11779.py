# gold3-11779. 최소비용 구하기 2

import sys, heapq
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # 출발지 도시 번호, 도착지 도시 번호, 버스 비용
    graph[a].append((b, c))
start_city_num, end_city_num = map(int, input().split()) # 구하고자하는 구간 출발점의 도시 번호, 도착점의 도시 번호
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start, end):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start, [start]))
    while q:
        dist, now, path = heapq.heappop(q)
        if now == end: return dist, path # 최소비용, 경로  
        if distance[now] < dist: continue      
        for next_node, next_dist in graph[now]:            
            cost = distance[now] + next_dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node, path + [next_node]))

min_cost, city_path = dijkstra(start_city_num, end_city_num)
print(min_cost)
print(len(city_path))
print(*city_path)
