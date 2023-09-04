# silver3-2606. 바이러스

import sys
input = sys.stdin.readline

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수

computer_num = int(input())
connected_computer_num = int(input())
graph = [[] for _ in range(computer_num + 1)]
visited = [0] * (computer_num + 1) 

for _ in range(connected_computer_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = 1 # 현재 노드 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(sum(visited) - 1) # 1번 컴퓨터 제외