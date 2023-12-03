# silver1 - 2156. 포도주 시식

import sys 
input = sys.stdin.readline

# 연속 3개 불가

n = int(input())
grape = [0 for _ in range(n+2)] # 포도주 양
for i in range(n):
    grape[i] = int(input())
dp = [0] * (n+2)

dp[0] = grape[0]
dp[1] = grape[0] + grape[1]
dp[2] = max(grape[0] + grape[2], grape[1] + grape[2], grape[0] + grape[1])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i])

print(dp[n-1])