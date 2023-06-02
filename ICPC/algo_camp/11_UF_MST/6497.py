#gold4-6497. 전력난

import sys
input = sys.stdin.readline

# 두 집 쌍에 대해 불이 켜질 수 있도록 하면서 최대로 불 꺼야 함 - 절약할 수 있는 최대 액수

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b: parent[b] = a
    else: parent[a] = b

while True:
    m, n = map(int, input().split()) # 집의 수, 길의 수
    if m == 0 and n == 0: break
    parent = [i for i in range(m)]
    edges = []
    max_cost = 0 # 절약할 수 있는 최대 비용
    for _ in range(n):
        x, y, z = map(int, input().split()) # x번 y번 집 사이 도로가 있음, 그 거리 z미터
        edges.append((z, x, y)) # 첫 번째를 비용으로: 비용순 정렬 위함
    
    edges.sort()

    for cost, a, b in edges:
        if find_parent(a, parent) != find_parent(b, parent):
            union_parent(a, b, parent)
        else: # 불 꺼도 됨 -> 절약한 비용 발생
            max_cost += cost

    print(max_cost)        
