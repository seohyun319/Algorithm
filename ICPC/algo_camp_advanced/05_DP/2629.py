# gold3-2629. 양팔저울

import sys
input = sys.stdin.readline

# 주어진 추만을 사용하여 구슬의 무게를 확인할 수 있는지
# 1, 4g 추로는 1, (4-1), 4, (4+1) 확인 가능

n = int(input()) # 추의 개수
metals_weight = list(map(int, input().split())) # 추의 무게들 (가벼운 것부터 차례대로)
marvels_num = int(input()) # 구슬의 개수
marvels_weight = list(map(int, input().split())) # 확인할 구슬의 무게들

# 추 무게를 하나씩 보면서 1로 만들어줌
# 이미 1인 곳(이미 올려본 적 있는 추) 기준으로 현재 추를 빼거나 더할 수 있음

metals_weight_sum = sum(metals_weight)
dp = [0] * (metals_weight_sum * 2 + 1) # 음수값부터 양수값까지

dp[metals_weight_sum] = 1 # 무게 0인 지점
for weight in metals_weight:
    # 현재 시점의 dp 리스트의 값이 1인 것들만 current_weight_indexes에 담아줌
    current_weight_indexes = []
    for idx in range(metals_weight_sum * 2 + 1):
        if dp[idx]:
            current_weight_indexes.append(idx)
    
    # 이미 1인 곳 기준으로 현재 추의 무게를 더하거나 뺌
    for idx in current_weight_indexes:
        if 0 <= idx + weight <= metals_weight_sum * 2 + 1:
            dp[idx + weight] = 1
        if 0 <= idx - weight <= metals_weight_sum * 2 + 1:
            dp[idx - weight] = 1

for marvel in marvels_weight:
    # marvel과 metals_weight_sum을 더해주는 이유는 metals_weight_sum에 대당하는 인덱스가 무게 0인 지점이기 때문
    # metals_weight_sum은 최대 30개*500g인 1500g, marvel은 최대 40000g이 입력으로 들어오기에 marvel이 더 크진 않은지 체크해줘야 인덱스 에러가 안 남
    if marvel <= metals_weight_sum and dp[marvel + metals_weight_sum]: 
        print("Y", end=' ')
    else:
        print("N", end=' ')

