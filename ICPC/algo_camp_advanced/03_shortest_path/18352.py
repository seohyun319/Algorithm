# silver2-18352. 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

# 도시 방향 그래프 (가중치 없음)
# 특정 도시 X에서 출발해 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시의 번호 출력

n, m, k, x = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [0] * (n+1) # 걸리는 거리
has_city = False # 최단 거리가 정확히 K인 도시가 있는지

for _ in range(m):					
    a, b = map(int, input().split())		
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                distance[next] = distance[now] + 1
                q.append(next)

bfs(x)

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        has_city = True

# 최단 거리가 정확히 K인 도시가 없음
if not has_city:
    print(-1)
