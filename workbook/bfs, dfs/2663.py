# silver1 단지번호 붙이기
import sys 
input = sys.stdin.readline
from collections import deque

n = int(input()) # 지도 크기
array = [list(map(int, input().rstrip())) for _ in range(n)]
house = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    sum = 1 # 초기화
    array[x][y] = 0 # 방문 처리
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1: # 방문할 곳
                array[nx][ny] = 0
                q.append((nx, ny))
                sum += 1
    house.append(sum)

for x in range(n):
    for y in range(n):
        if array[x][y] == 1:
            bfs(x, y)

print(len(house))
print(*sorted(house), sep='\n')
