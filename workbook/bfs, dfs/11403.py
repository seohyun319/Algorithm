# silver1 경로 찾기
import sys 
input = sys.stdin.readline

n = int(input())
visited = [0]*n
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(v):
    for i in range(n): # 한줄마다 봄
        if not visited[i] and graph[v][i] == 1:
            visited[i] = 1 # 현재 노드 방문 처리
            dfs(i)

for i in range(n):
    dfs(i)
    print(*visited)
    visited = [0]*n # 초기화