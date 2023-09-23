# silver3-9095. 1, 2, 3 더하기

import sys
input = sys.stdin.readline

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
# 1: 1
# 2: 1+1, 2 -> 2
# 3: 1+1+1, 1+2, 2+1, 3 -> 4
# 4: 1+1+1+1, 1+2+1, 2+1+1, 3+1, | 1+1+2, 2+2 | 1+3 -> 7 (4+2+1)
# 5: 4번 케이스에 1씩 더함 (7개) | 3번 케이스에 2씩 더함 (4개) | 2번 케이스에 3씩 더함 (2개) -> 13

t = int(input())
dp = [0] * (11+1)
dp[0] = 1
for i in range(1, 11+1):
    if dp[i - 1] > 0:
        dp[i] += dp[i - 1]
    if dp[i - 2] > 0:
        dp[i] += dp[i - 2]
    if dp[i - 3] > 0:
        dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
    
