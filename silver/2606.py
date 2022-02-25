# silver3 그래프 탐색 - 바이러스

import sys
put = sys.stdin.readline
computer = int(put())
conn = int(put()) #connected computer
pair = [[]*computer for _ in range(computer+1)] #컴퓨터 개수만큼 생성한 배열을 pair 리스트에 담음

for i in range(conn):
    x, y = map(int, put().split())
    # 서로 연결된 쌍이니까 
    pair[x].append(y)
    pair[y].append(x)

count = 0
visited = [False]*(computer+1)

# 깊이 우선 탐색 - 인접 노드 방문
def dfs(start, visited): 
    global count #global로 전역변수 선언
    visited[start]=True #시작 노드 방문 true
    for i in pair[start]:
        if not visited[i]:
            count += 1
            dfs(i, visited)
            # 디버깅) dfs(start, visited)로 했더니 RecursionError: maximum recursion depth exceeded 오류 발생!
            # 시작점을 바꿔줘야 함.

dfs(1, visited)
print(count)
