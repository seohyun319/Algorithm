# silver4-13413. 오셀로 재배치
# 기존에 풀었던 방법: '임의의' 말 위치를 바꾸는 게 아니라 '바로 옆' 말 위치를 서로 바꾸는 거로 생각해서 틀림
    # if initial_state와 target_state가 같으면: pass, elif 스왑 가능한 조건이면 스왑, else 색 바꾸기 함
    # 인덱스 에러 난 이유: elif문에서 i < n - 1 조건을 and and 뒤 맨 마지막에 넣어서 맨 앞의 조건문에서 인덱스에러가 난 것. 

import sys
input = sys.stdin.readline

# 목표 상태를 만들기 위한 작업의 최소 횟수
# 가능한 작업
    # 1. 배치된 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
    # 2. 말 1개를 들어 뒤집어 놓아 색상을 변경한다.

# 위치 바꾸는 게 유효하려면 바꿀 애가 서로 다른 애여야 함 
# 위치 바꿀 수 있으면 바꾸는 게 각각 색 바꾸는 것보다 좋음

t = int(input())
for _ in range(t):
    n = int(input())
    # 초기 상태와 목표 상태. 흰색 면 W, 검은색 면 B
    initial_state = list(input().rstrip())
    target_state = list(input().rstrip())
    different = {"BW": 0, "WB": 0}
    cnt = 0
    for i in range(n):        
        if initial_state[i] == target_state[i]: pass
        else:
            if initial_state[i] == "B" and target_state[i] == "W": 
                if different["WB"] > 0: # 스왑해줄 애가 존재 => 1번 작업 
                    cnt += 1
                    different["WB"] -= 1
                else: different["BW"] += 1
            elif initial_state[i] == "W" and target_state[i] == "B": 
                if different["BW"] > 0: # 1번 작업
                    cnt += 1
                    different["BW"] -= 1
                else: different["WB"] += 1
    cnt += different["BW"] + different["WB"] # 2번 작업
    print(cnt)
        
