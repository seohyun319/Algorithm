# gold1-4198. 열차정렬

import sys
input = sys.stdin.readline

# 각 차량이 역에 도착하는 순서대로 차량들의 중량이 주어질 때, 에린이 만들 수 있는 가장 긴 열차배열의 길이(=차량의 수)
# 각 차량이 기차역에 도착 시 할 수 있는 행동
    # 1. 전면 혹은 후미에 차량을 추가
    # 2. 차량을 열차에 추가하는 것을 거부
# 무게 내림차순 정렬을 맞추며 최대한 긴 배열 만들어야 함

n = int(input()) # 열차의 수
weights = [int(input()) for _ in range(n)] # 각 열차의 무게
# 인덱스를 weights 기준으로 정렬
idx_list = [i for i in range(n)]
idx_list.sort(key = lambda x: weights[x])

up_dp = [1]*n
down_dp = [1]*n

if n == 0:
    print(0)
    exit()

for idx in range(n):
    for prev in range(idx):
        if idx_list[idx] > idx_list[prev]:
            up_dp[idx] = max(up_dp[idx], up_dp[prev] + 1)
            # 감소했다가 증가
            up_dp[idx] = max(up_dp[idx], down_dp[prev] + 1)
        else:
            down_dp[idx] = max(down_dp[idx], down_dp[prev] + 1)

print(max(max(up_dp), max(down_dp)))
