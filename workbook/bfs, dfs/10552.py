# silver2 DOM
import sys 
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, p = map(int, input().split()) # 노인 수, 채널 수, 초기
graph = [[] for _ in range(m+1)]
visited = [0] * (m+1)
sum = 0
for _ in range(n):
    a, b = map(int, input().split()) # 선호/비선호
    graph[b].append(a) # 비선호시 바꿀 선호 채널

def dfs(v):
    global sum
    if visited[v] == 1: # 다시 방문한 상황: 사이클임
        print(-1)
        exit(0) # -1 프린트하고 바로 끝내야 함
    else: 
        visited[v] = 1 # 현재 노드 방문
    # 현재 채널을 싫어하는 사람이 있으면 채널 바꾸기
    if len(graph[v]) > 0:
        dfs(graph[v][0])
        sum += 1

dfs(p)

print(sum)
