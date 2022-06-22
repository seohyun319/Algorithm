# C13. DFS/BFS - 기출 문제 '특정 거리의 도시 찾기'

import sys
from collections import deque
input = sys.stdin.readline

# 도시 방향 그래프 (가중치 없음)
# 특정 도시 X에서 출발해 도달할 수 있는 모든 도시 중 최단 거리가 정확히 K인 모든 도시의 번호 출력

n, m, k, x = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [0] * (n+1) # 걸리는 거리

for _ in range(m):					
    a, b = map(int, input().split())		
    graph[a].append(b)

def bfs(start):    
    q = deque([start])
    # 시작점도 방문처리 해줘야함!!!!!!
    visited[start] = 1
    while q:
        now = q.popleft()
        # 연관된 노드 방문
        for next in graph[now]:
            if visited[next] == 0: # 방문하지 않았다면
                visited[next] = 1 # 방문 처리
                # distance[next] += 1로 했더니 계속 제대로 안 됐음. 거리 갱신은 현재 노드 기준으로 해줘야.
                distance[next] = distance[now] + 1
                q.append(next)

bfs(x)

for i in range(n+1):
    # 거리가 원하는 최단 거리인 k와 같다면
    if distance[i] == k:
        print(i)

# 도달할 수 있는 도시 중 최단 거리가 k인 도시가 하나도 없을 경우
if k not in distance:
    print(-1)
