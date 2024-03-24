# gold4-1197. 최소 스패닝 트리

import sys
input = sys.stdin.readline

# 최소 스패닝 트리 구하기

v, e = map(int, input().split())
edges = []
result = 0
parent = [x for x in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split()) # A번 정점과 B번 정점이 가중치 C인 간선으로 연결 (C는 음수일 수도)
    edges.append((c, a, b))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()

for cost, x, y in edges:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost

print(result)    
