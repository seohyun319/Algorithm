#C5. DFS/BFS - 실전문제 '미로 탈출'

# import sys
from collections import deque
# put = sys.stdin.readline
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
dx = [0, -1, 1, 0] #상좌우하 #x y 안 나누면 대각선 방향으로 더해져서 dx dy 나눠냐
dy = [1, 0, 0, -1] 

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나 뽑음
        x, y = queue.popleft()
        # 이동
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            # 영역 벗어나면 무시
            if a<0 or a>=n or b<0 or b>=m:
                continue
            # 괴물 있으면 무시
            if maze[a][b] == 0:
                continue
            # 해당 노드를 처음 방문하면 기록
            if maze[a][b] == 1:
                maze[a][b] = maze[x][y] + 1 #기존 거에 더해야함
                queue.append((a,b))
    return maze[n-1][m-1] #(0,0)이 문제 상 (1,1)로 인식되니까 (n-1,m-1)이어야 문제 상 (n,m)
print(bfs(0,0))

