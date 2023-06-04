#gold2-10423. 전기가 부족해

import sys
input = sys.stdin.readline

# 모든 도시에 전기가 공급될 수 있도록 하는 케이블 설치 최소 비용 구하기
# 케이블이 연결돼있는 도시에는 발전소가 하나만 존재해야

n, m, k = map(int, input().split()) # 도시 개수, 설치 가능한 케이블 수, 발전소 개수
power = list(map(int, input().split())) # 발전소 설치된 도시 번호 (전기 공급처)
parent = [i for i in range(n+1)]
edges = []

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b: parent[b] = a
    else: parent[a] = b

for _ in range(m):
    u, v, w = map(int, input().split()) # u 도시와 v 도시를 연결하는 케이블 설치 시 w의 비용 발생
    edges.append((w, u, v))
    
edges.sort()

for i in range(k-1): # 발전소끼리 연결해줌
    union_parent(power[i], power[i+1], parent)
    
cost_sum = 0
for cost, a, b in edges:
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(a, b, parent)
        cost_sum += cost

print(cost_sum)
