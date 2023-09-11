# silver4-1018. 체스판 다시 칠하기

import sys
input = sys.stdin.readline

# 각 좌표끼리 더한 값을 2로 나눠서 0이면 블랙 1이면 화이트 뭐 이런 식으로 쭉 뽑아놓고 개수 쭉 구하기

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
wb = ["W", "B"]
answer_list = []

# 8 * 8로 자름: n - 8 + 1까지 봄 (range에서 뒤 범위 1 더해줌)
for x in range(n - 7):
    for y in range(m - 7): 
        repaint = 0
        # 8 * 8만큼 돌기
        for i in range(x, x + 8): 
            for j in range(y, y + 8):
                # 보드의 이번 값이 원하는 값이 아니면 다시 칠함
                # (i + j) % 2는 좌표끼리 더한 값을 2로 나눈 나머지, 0 또는 1임. 01010101 이렇게 원하는 체스판 모양대로 나올 것. 
                # wb[(i + j) % 2]는 이번에 나오길 기대하는 값 (0일 때 흰색, 1일 때 검은색)
                if board[i][j] != wb[(i + j) % 2]: 
                    repaint += 1
        repaint = min(repaint, 8*8 - repaint) # 맨 위쪽 칸 검은색인 경우와 흰 색인 경우 중 최소값
        answer_list.append(repaint)

print(min(answer_list))
