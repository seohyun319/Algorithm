# gold3-2206. 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline

# 최단경로 - 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited_used_item = [[0]*m for _ in range(n)]
visited_unused_item = [[0]*m for _ in range(n)]
visited_used_item[0][0] = 1
visited_unused_item[0][0] = 1
min_dist = -1

def bfs():
    global min_dist
    q = deque()
    q.append((0, 0, 1, 0)) # 시작하는 칸도 포함해서 세야 해서 거리는 1부터 시작
    while q:
        a, b, dist, used_item = q.popleft()
        if a == n - 1 and b == m - 1: # 도착
            if min_dist == -1: min_dist = dist
            else: min_dist = min(min_dist, dist)
            continue
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0': # 벽 없음
                if used_item == 1 and not visited_used_item[nx][ny]: # 아이템 쓴 적 있음
                    q.append((nx, ny, dist + 1, 1))                
                    visited_used_item[nx][ny] = 1
                elif used_item == 0 and not visited_unused_item[nx][ny]: # 아이템 쓴 적 없음
                    q.append((nx, ny, dist + 1, 0))                
                    visited_unused_item[nx][ny] = 1
            elif 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1': # 벽 있음
                if used_item == 0 and not visited_unused_item[nx][ny]: # 뚫어야 함: 이전에 뚫은 적이 없어야 함
                    q.append((nx, ny, dist + 1, 1)) # 이번에 아이템 씀                
                    visited_unused_item[nx][ny] = 1                                  
    return min_dist

print(bfs())
