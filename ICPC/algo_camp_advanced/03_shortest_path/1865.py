# gold3-1865. 웜홀

import sys
input = sys.stdin.readline

# 한 지점에서 출발해 시간여행 후 다시 출발 위치로 돌아왔을 때
# 출발 때보다 시간이 되돌아간 경우가 가능한지
# 벨만포드 안 if문에서 distance[node] != INF 조건도 넣어줬었는데 그거땜에 틀림

def bellmanford(start):
    distance[start] = 0
    for i in range(n):
        for node, next_node, cost in edges:
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[next_node] > distance[node] + cost:
                distance[next_node] = distance[node] + cost
                # n번 돌렸는데도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1: 
                    return True
    return False


INF = int(1e9)
tc = int(input()) # 테스트 케이스
for _ in range(tc):
    n, m, w = map(int, input().split()) # 지점 수, 도로 개수, 웜홀 개수
    edges = [] # 모든 간선에 대한 정보를 담는 리스트 생성
    distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화
    for _ in range(m):
        s, e, t = map(int, input().split()) # S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split()) # S는 시작 지점, E는 도착 지점, T는 줄어드는 시간
        edges.append((s, e, -t))

    negative_cycle = bellmanford(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
