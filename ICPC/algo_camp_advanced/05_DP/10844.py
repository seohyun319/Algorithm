# silver1-10844. 쉬운 계단 수

import sys
input = sys.stdin.readline

# 길이가 N인 계단 수가 총 몇 개 있는지
# 0으로 시작하는 수는 계단수가 아니다

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

# 0 / 1~8 / 9는 속성이 다름. 
# n*10짜리 개수만 들고 있으면 됨. 
dp[1] = [0] + [1]*9 # 1~8 / 9 => 8 + 1 => 9
# dp[2] = 17 # 10 12, 21 23, 32 34, ..., 87 89 / 98 => 8*2 + 1 => 17 
# 각 수에서 일의 자리수 기준으로 구함. 0은 +1인 1, 9는 -1인 8의 경우 하나씩만 있고, 나머지 1~8은 -1, +1 두개씩 존재

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]        
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1_000_000_000)
