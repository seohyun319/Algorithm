# silver3 - 2193. 이친수

import sys 
input = sys.stdin.readline

# 1
# 10
# 101 100
# 1010 1001 1000
# 10101 10100 10010 10001 10000
# 101010 101001 101000 100101 10100 100010 100001 100000
# 피보나치인 듯

n = int(input())
dp = [0] * 91

dp[1] = 1
dp[2] = 1

for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
