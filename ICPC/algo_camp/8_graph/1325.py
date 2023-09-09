# silver1-1325. 효율적인 해킹
# 메모리 초과, 시간 초과 해결

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
hackable_com_nums = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) # b 해킹 시 a도 해킹 가능

def bfs(v):
    visited = [0 for _ in range(n + 1)]
    hackable_com_num = 0
    q = deque()
    q.append(v)
    visited[v] = 1 # 입력 노드 체크
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                hackable_com_num += 1
                q.append(i)
                visited[i] = 1 # 시간초과 해결: 큐 안에서 자식 노드 체크
    return hackable_com_num

for i in range(1, n + 1):
    hackable_com_nums[i] = bfs(i)
    
    # 초기화
    # ==> 메모리 초과라서 visited를 전역으로 하지 않고 bfs 함수 안에서 선언해줌
    # hackable_com_num = 0
    # visited = [0 for _ in range(n + 1)]

max_num = max(hackable_com_nums)
for i in range(1, n + 1):
    if hackable_com_nums[i] == max_num:
        print(i, end=' ')
