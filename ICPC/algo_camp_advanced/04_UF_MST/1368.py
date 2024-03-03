# gold2-1368. 물대기

import sys
input = sys.stdin.readline

# 논에 물 대는 법: 직접 논에 우물 파기 / 이미 물 대고 있는 다른 논으로부터 물 끌어오기
# 최소의 비용으로 모든 논에 물을 대기

n = int(input())
edges = []
# 우물 파는 비용: 0부터 해당 우물까지
for i in range(1, n + 1):
    making_cost = int(input())
    edges.append((making_cost, 0, i))
# i 우물과 j 우물을 연결하는 비용
for i in range(1, n + 1):
    connecting_cost = [0] + list(map(int, input().split()))
    for j in range(i, n + 1):
        edges.append((connecting_cost[j], i, j))
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
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

print(answer)
