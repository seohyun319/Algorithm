# C4. 구현 - 실전문제 '왕실의 나이트' - 2번째 

import sys
input = sys.stdin.readline

# L자 형태로 이동하는 나이트가 이동할 수 있는 경우의 수 출력
# 정원 밖으로 나갈 수 없음. 

position = str(input()) # 현재 나이트가 위치한 곳의 좌표
col = ord(position[0]) - ord('a') + 1
row = int(position[1])
num = 0

move = [
    (1, 2), (1, -2), (-1, 2), (-1, -2), 
    (2, 1), (2, -1), (-2, 1), (-2, -1)]

for x, y in move:
    nx = col + x
    ny = row + y
    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    else: num += 1

print(num)


