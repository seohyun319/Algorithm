# silver1-1802. 종이 접기

import sys
input = sys.stdin.readline

# 종이를 동호의 방법대로 다시 접을 수 있으면 YES를, 접을 수 없으면 NO를 출력

# 1 0 0 가능: 가운데 있는 0으로 접고 그 종이를 한 번 더 접음 -> 1 0 이렇게 대칭이니까 가능함
# 100 0 110 가능: 가운데 0 기준으로 접으면 100 110 대칭. (앞에 거 순서 뒤집으면 001, 숫자 반전하면 110)

# 한 번만 접는 게 아님 -> 재귀
def check(info):
    mid_idx = len(info) // 2
    left_side = info[:mid_idx]
    right_side = info[mid_idx + 1:]
    if len(info) == 1: return True
    for i in range(mid_idx):
        if left_side[::-1][i] == right_side[i]:
            return False
    return check(left_side) and check(right_side)

t = int(input())
for _ in range(t):
    info = list(input().rstrip()) # 1은 OUT, 0은 IN    
    if check(info): print("YES")
    else: print("NO")
