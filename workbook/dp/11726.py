# silver3 - 11726. 2×n 타일링

import sys 
input = sys.stdin.readline

# 1 세로 
# 2 세로 + 가로
# 3 세로 + 가로세로
# 5 가로세로*2 + 양옆하나씩 두고 가로세로 - 전부 세로
# 피보나치

n = int(input())
dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
