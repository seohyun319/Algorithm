# C4. 구현 - 실전문제 '게임 개발' - 2번째

import sys
input = sys.stdin.readline

# 1. 현재위치 현재방향 기준 왼쪽 방향(-90도)부터 차례로 갈 곳 정함
# 2. 바로 왼쪽에 안 가본 곳 있으면 왼쪽으로 회전 후 전진. 없으면 왼쪽으로 회전하고 1단계
# 3. 네 방향 모두 이미 가봤거나 바다로 돼있으면 방향 유지한 채 한 칸 뒤로가고 1단계. (뒤가 바다면 멈추기)
# 처음에 캐릭터는 항상 육지에 위치
# 캐릭터가 방문한 칸 수 출력

n, m = map(int, input().split()) # 세로, 가로
a, b, d = map(int, input().split()) # 게임캐릭터가 있는 칸의 좌표 (a, b)와 바라보는 방향 d
graph = [list(map(int, input().split())) for _ in range(n)] # 맵 정보 (0은 육지, 1은 바다)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_left():
    global d
    if d == 0: d = 3
    d -= 1

graph[a][b] = 1 # 현재 위치 방문
cnt = 1
turn_time = 0 # 네 방향 모두 가는 케이스 고려

while True:
    turn_left()
    nx = a + dx[d]
    ny = b + dy[d]
    # 회전 후 정면이 안 가본 곳이라면 이동
    if graph[nx][ny] == 0:
        graph[nx][ny] = 1 # 방문 처리
        cnt += 1
        a, b = nx, ny # 좌표 갱신
        turn_time = 0
        continue
    else: # 이미 간 곳이라면        
        turn_time += 1
    
    if turn_time == 4: # 네 방향 모두 갔다면
        # 뒤로가기
        nx = a - dx[d]
        ny = b - dy[d]
        # 뒤로 갈 수 있으면 가기
        if graph[nx][ny] == 0:            
            a, b = nx, ny # 좌표 갱신
        else: # 뒤로 갈 수 없으면
            break
        turn_time = 0

print(cnt)


