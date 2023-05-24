# gold4-11657. 타임머신

import sys
input = sys.stdin.readline

# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하기
# 이동시간이 양수면 그만큼 이동, 0이면 순간이동, 음수면 타임머신으로 시간 되돌아감 

n, m = map(int, input().split()) # 도시 개수, 버스 노선 개수
edges = []
for _ in range(m):
    a, b, c = map(int, input().split()) # 버스 노선 정보(시작 도시, 도착 도시, 이동시간)
    edges.append((a, b, c))
INF = int(1e9)
distance = [INF] * (n+1)

def bellmanford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            node, next_node, cost = edges[j][0], edges[j][1], edges[j][2]
            if distance[node] != INF and distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node] + cost
                if i == n - 1: return True # 마지막까지 값이 갱신된다면 음수 순환 존재
    return False # 음수 순환 미존재

if bellmanford(1): # 음수 순환 존재하면 (시간을 무한히 되돌릴 수 있다면)
    print(-1)
else: 
    for i in range(2, n + 1): # 1번째 제외하고(1번 도시에서 출발) 다른 도시로 가기 위한 가장 빠른 시간 출력
        if distance[i] == INF:
            print(-1)
        else: print(distance[i])
