# gold2-17136. 색종이 붙이기

import sys
input = sys.stdin.readline

# 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류의 색종이를 5개씩 가지고 있음
# 10×10인 종이 중 1이 적힌 칸 위에 색종이를 붙일 때 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수

board = [list(map(int, input().split())) for _ in range(10)]
remain_papers = [5, 5, 5, 5, 5]
answer = 26

# 다음에 볼 게 0이 아닌지 체크 (색종이 붙일 수 있는지)
def check(y, x, length):
    for i in range(y, y + length + 1):
        for j in range(x, x + length + 1):
            if board[i][j] == 0:
                return False
    return True

# 색종이 붙임
def attach(y, x, length):
    for i in range(y, y + length + 1):
        for j in range(x, x + length + 1):
            board[i][j] = 0
    remain_papers[length] -= 1

# 색종이 붙였던 거 다시 돌려놓음
def remove(y, x, length):
    for i in range(y, y + length + 1):
        for j in range(x, x + length + 1):
            board[i][j] = 1
    remain_papers[length] += 1

def back(y, x, cnt):
    global answer
    # 끝까지 다 봄
    if y >= 10:
        answer = min(answer, cnt)
        return
    # 한 줄 다 봄 -> 다음 줄 보기
    if x >= 10:
        back(y + 1, 0, cnt)
        return

    # 색종이 붙이기
    if board[y][x] == 1:
        for length in range(5):
            # 범위 넘김
            if y + length >= 10 or x + length >= 10: continue
            # 종이 다 씀
            if not remain_papers[length]: continue            
            if check(y, x, length):
                attach(y, x, length)
                back(y, x + length + 1, cnt + 1)
                remove(y, x, length)    
    else: # 현재가 0이면 그 다음 오른쪽 거 확인
        back(y, x + 1, cnt)

back(0, 0, 0)

if answer != 26:
    print(answer) 
else: print(-1)