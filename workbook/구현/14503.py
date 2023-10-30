# gold5-14503. 로봇 청소기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 좌표와 바라보는 방향
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1: d = 3

visited[r][c] = 1 # 현재 위치 청소
cnt = 1
turn_time = 0

while True:
    turn_left()
    # 전진
    nx, ny = r + dx[d], c + dy[d]
    # 아직 청소하지 않은 곳이 있다면
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        r, c = nx, ny # 좌표 갱신
        turn_time = 0 # 초기화
    # 청소할 곳 없으면 그 방향으로 회전
    else: 
        turn_time += 1
    # 다 청소가 돼있거나 벽인 경우
    if turn_time == 4:
        nx, ny = r - dx[d], c - dy[d]
        if graph[nx][ny] == 0: # 후진 가능
            r, c = nx, ny # 좌표 갱신
        else: # 뒤로 갈 수 없으면 작동 멈춤
            break 
        turn_time = 0

print(cnt)
    