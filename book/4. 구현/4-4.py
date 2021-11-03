# C4. 구현 - 실전문제 '게임 개발'

import sys
put = sys.stdin.readline
n, m = map(int, put().split())
a, b, d = map(int, put().split())
stepX = [0, 1, 0, -1] #북 동 남 서
stepY = [-1, 0, 1, 0] #북 동 남 서

maps = [] 
for i in range(n):
    maps.append(list(map(int, put().split())))
maps[a][b] = 1 #현재위치. 방문해서 1

go=1 #방문 횟수. 현재 칸부터 방문한 거로 침. 
turn=0 #회전 횟수

# def turn_left():
#     global d
#     d-=1
#     if d==-1: d=3 #북쪽 보면 서쪽으로

while True:
    #방향 전환. 현재방향 기준 왼쪽으로.     
    d-=1
    if d==-1: d=3 #북쪽 보면 서쪽으로

    # # 서쪽 안 갔으면 서쪽으로 감 = map[b][a-1]
    # # 북으로 map[b+1][a]
    # # 동으로 map[b][a+1]
    # # 남으로 map[b-1][a]
    #a, b 좌표 바뀌는 걸 x, y에 저장
    x = a + stepX[d]
    y = b + stepY[d]

    #방향 전환 후 그 방향에(정면에) 가보지 않은 칸 존재하면 전진
    if maps[x][y] == 0: #안 가봤거나 바다가 아님
        maps[x][y] = 1 #가봤음 표시
        #현재 좌표로 바꿔줌
        a=x
        b=y
        go += 1 
        turn = 0
        continue
    else: #아니면 회전
        turn += 1

    #네 방향 다 가봤으면 한 칸 뒤로 감
    if turn == 4: 
        #기존에 step은 한 칸 앞으로 갔는데 -1 곱하면 한 칸 뒤로 감
        x = a - stepX[d]
        y = b - stepY[d]
        if maps[x][y] == 0:
            a=x
            b=y
        else: break #바다라서 뒤로 못 가면 움직임 멈춤
        turn = 0 #회전 횟수 초기화
print(go)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1