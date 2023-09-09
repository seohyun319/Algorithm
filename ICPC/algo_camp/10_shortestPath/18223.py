# gold4-18223. 민준이와 마산 그리고 건우
# 단방향 그래프로 입력받아서 틀렸음. 양방향 그래프로 고침
# 건우를 구해주고, 마저 마산까지 가야되는데 건우를 구해주는 거리랑 최단거리랑 같은지만 비교함. 구해주고 마저 가는 거를 생각 못함. 

import sys, heapq
input = sys.stdin.readline

v, e, p = map(int, input().split()) # 정점 개수, 간선 개수, 건우가 위치한 정점
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split()) # a번 정점과 b번 정점 사이의 거리가 c
    # 양방향 그래프
    graph[a].append((b, c))
    graph[b].append((a, c))
INF = int(1e9)

# 마산(도착지, v번 정점)이 더 가까우면 그냥 마산으로, 최단 경로에 건우가 있으면 겸사겸사 구해줌
# 민준이가 찾은 최단 경로 위에 건우가 있다면 "SAVE HIM" 을 아니면 "GOOD BYE" 를 출력

def dijkstra(start, end):
    distance = [INF]*(v+1)
    q = []
    heapq.heappush(q, (0, start)) # 시작점: 거리 0, 시작노드
    distance[start] = 0 # 자기자신 방문한 거리는 0
    while q:
        dist, now = heapq.heappop(q) # 최단 거리, 최단 거리의 노드
        # 이번에 볼 거리인 dist가 지금까지 갱신된 최단거리인 distance[now]보다 작으면 이미 본 거니까 더 볼 가치가 없음.
        if distance[now] < dist: continue 
        for next, next_dist in graph[now]:
            cost = dist + next_dist # 비용: 지금 노드까지의 거리 + 다음 노드까지의 거리
            # 이번 노드에서 다음 노드까지 거쳐 가는 게 이번 노드 없이 건너뛰어서 다음 노드까지 가는 거리보다 더 짧으면
            if cost < distance[next]: 
                distance[next] = cost # 더 짧은 거리(이번 노드 거쳐가는 거리)로 갱신해줌
                heapq.heappush(q, (cost, next)) # 여기도 갱신
    return distance[end] # 목표 지점까지의 최단 거리

if dijkstra(1, p) + dijkstra(p, v) <= dijkstra(1, v): # 건우 구해주는 경로 길이가 마산까지 가는 최단경로보다 짧거나 최단경로에 있으면
    print("SAVE HIM") # 겸사겸사 구해줌
else: # 마산이 더 가까워서 건우 버림
    print("GOOD BYE")