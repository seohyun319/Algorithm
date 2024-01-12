# gold5-14891. 톱니바퀴

import sys
from collections import deque
input = sys.stdin.readline

# 맞닿은 극이 달라야 회전함 (상대의 반대 방향으로 회전)
# 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력
# 점수: 톱니바퀴의 12시방향이 S극이면 1번은 1점, 2번은 2점, 3번은 4점, 4번은 8점

first = deque(map(str, input().rstrip())) # 12시방향부터 시계방향 순서대로 N극은 0, S극은 1
second = deque(map(str, input().rstrip()))
third = deque(map(str, input().rstrip()))
fourth = deque(map(str, input().rstrip()))
k = int(input()) # 회전 횟수
rotation_info = [list(map(int, input().split())) for _ in range(k)] # 회전시킨 톱니바퀴 번호, 방향 (1은 시계, -1은 반시계)
score = 0

# 3번째, 7번째 (2번, 6번 인덱스)가 맞닿음 체크 기준

for num, direction in rotation_info:
    if num == 1:
        if first[2] != second[6]: # 첫 번째 돌아가면 두 세 네번째 돌아가는지 체크해서 끝부터 돌림 (미리 돌아가버리면 인덱스 안 맞음)
            if second[2] != third[6]: 
                if third[2] != fourth[6]: 
                    fourth.rotate(-direction)
                third.rotate(direction)
            second.rotate(-direction)
        first.rotate(direction)
    if num == 2:    
        if first[2] != second[6]: first.rotate(-direction) # 두 번째로 인한 연쇄작용 왼쪽
        if second[2] != third[6]: # 두 번째로 인한 연쇄작용 오른쪽 
            if third[2] != fourth[6]: 
                fourth.rotate(direction)
            third.rotate(-direction)
        second.rotate(direction)       
    if num == 3:    
        if third[2] != fourth[6]: fourth.rotate(-direction) # 세 번째로 인한 연쇄작용 오른쪽
        if second[2] != third[6]: # 세 번째로 인한 왼쪽 
            if first[2] != second[6]: 
                first.rotate(direction)
            second.rotate(-direction)
        third.rotate(direction)   
    if num == 4:
        if third[2] != fourth[6]: 
            if second[2] != third[6]: 
                if first[2] != second[6]: 
                    first.rotate(-direction)
                second.rotate(direction)
            third.rotate(-direction)
        fourth.rotate(direction)

if first[0] == '1': score += 1
if second[0] == '1': score += 2
if third[0] == '1': score += 4
if fourth[0] == '1': score += 8

print(score)
