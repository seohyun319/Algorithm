# silver2 연결 요소의 개수
import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split()) # 정점 간선 개수
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
sum = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = 1 # 현재 노드 방문
    # 현재 노드와 관련된 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        sum += 1

print(sum)