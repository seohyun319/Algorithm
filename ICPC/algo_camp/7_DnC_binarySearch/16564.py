# silver1-16564. 히오스 프로게이머

import sys
input = sys.stdin.readline

# 달성할 수 있는 최대 팀 목표레벨 구하기
# 모든 캐릭터 레벨을 동일하게 만들어야 함
# 레벨을 총합 K보다 적게 올릴 수도 있음

n, k = map(int, input().split()) # 캐릭터 개수, 올릴 수 있는 레벨 총합
levels = [int(input()) for _ in range(n)] # 각 캐릭터의 레벨
"""
# 이진탐색으로 풀기
start = min(levels)
end = max(levels) + k # 제일 높은 레벨에 몰빵
result = 0

# 목표 레벨에서 현재 레벨을 뺀 값의 합(사용할 k값)이 k보다 크다면 목표 레벨을 낮춰야 함

while start <= end:
    total = 0 # 올리는 데 사용한 레벨
    mid = (start + end) // 2 # 목표 레벨
    for level in levels:
        if level < mid: # 현재 레벨이 목표 레벨보다 낮으면
            total += mid - level # 레벨 올림
    if total > k: # 올린 레벨이 올릴 수 있는 양보다 많으면
        end = mid - 1 # 목표 레벨 낮춤
    else: 
        result = mid # 목표 레벨 높이기 전에 되는 값 저장해둠
        start = mid + 1

print(result)
"""

levels.sort()

result = levels[0] # 최소값

for i in range(1, n): 
    need = levels[i] - levels[i - 1] # 바로 다음으로 큰 레벨과 동일해지기 위해 필요한 양
    if need * i <= k: # 필요한 양이 쓸 수 있는 양보다 작으면 올릴 수 있음
        result += need
        k -= need * i
    elif (k // i) * i <= k: # 다음 레벨까지는 못올리는데 조금은 올릴 수 있음 (남은 거 n분의 1에서 정수값만큼)
        result += k // i
        k -= (k // i) * i

# 전부 다 최대 레벨까지 올려줬는데 k가 남아돎
if k // n >= 1: # n명한테 최소 1씩 올려줄 수 있음
    result += k // n

print(result)

