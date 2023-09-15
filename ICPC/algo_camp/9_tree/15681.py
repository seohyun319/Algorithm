# gold5-15681. 트리와 쿼리

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력

n, r, q = map(int, input().split()) # 트리 정점 수, 루트 번호, 쿼리의 수
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
u_list = [int(input()) for _ in range(q)]
sub_tree = [0] * (n+1)

def dfs(v):
    sub_tree[v] = 1
    for i in graph[v]:
        if not sub_tree[i]: # 방문한 적 없으면
            dfs(i)
            sub_tree[v] += sub_tree[i]

dfs(r) # 루트 기준 

for u in u_list:
    print(sub_tree[u])
