# silver3 - 1463. 1로 만들기

import sys 
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for x in range(2, n+1):    
    # 1. 1을 빼는 경우
    dp[x] = dp[x - 1] + 1
    # 2. 3으로 나누는 경우
    if x % 3 == 0: 
        dp[x] = min(dp[x // 3] + 1, dp[x])
    # 3. 2로 나누는 경우
    if x % 2 == 0: 
        dp[x] = min(dp[x // 2] + 1, dp[x])
    # 의 세 케이스에서 나누기에 걸리는 경우 
    # 1을 빼는 경우와 나누는 경우 중 최소값 고름

print(dp[n])
