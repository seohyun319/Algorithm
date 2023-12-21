# silver1 나이트의 이동
import sys 
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs():
    q = deque()
    q.append((now_x, now_y))
    array[now_x][now_y] = 1 # 방문 처리
    while q:
        x, y = q.popleft()
        if x == next_x and y == next_y:
            print(array[x][y] - 1)
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and array[nx][ny] == 0: # 방문할 곳
                q.append((nx, ny))
                array[nx][ny] = array[x][y] + 1

t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    l = int(input()) # 체스판 한 변의 길이
    now_x, now_y = map(int, input().split()) # 나이트가 현재 있는 칸
    next_x, next_y = map(int, input().split()) # 나이트가 이동하려고 하는 칸
    array = [[0]*l for _ in range(l)]
    bfs()
