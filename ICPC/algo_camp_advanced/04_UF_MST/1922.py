# gold4-1922. 네트워크 연결

import sys
input = sys.stdin.readline

# 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용

edges = []
n = int(input()) # 컴퓨터의 수 (정점)
m = int(input()) # 연결할 수 있는 선의 수 (간선)
for _ in range(m):
    a, b, c = map(int, input().split()) # a컴퓨터와 b컴퓨터를 연결하는데 비용이 c  
    edges.append((c, a, b))
parent = [i for i in range(n + 1)]
answer = 0

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b): # 순환이 존재하지 않으면
        union_parent(a, b)
        answer += cost

print(answer)

