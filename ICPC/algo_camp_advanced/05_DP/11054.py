# gold4-11054. 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

# 바이토닉 수열: 수열이 증가했다가 감소하는 수열 (증가만 하거나 감소만 해도 괜찮음)

n = int(input()) # 수열의 크기
array = list(map(int, input().split())) # 수열

up_dp = [1]*n
down_dp = [1]*n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)
        elif array[i] < array[j]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)
            down_dp[i] = max(down_dp[i], up_dp[j] + 1) # 꺾였을 때

print(max(max(up_dp), max(down_dp)))
