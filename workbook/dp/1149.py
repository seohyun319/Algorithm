# silver3 - 1149. RGB거리

import sys 
input = sys.stdin.readline

# 집 색 연속 불가. 모든 집 칠하는 비용 최솟값

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)] # 빨 초 파로 칠하는 비용
dp = [[0] * 3 for _ in range(n)]

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + rgb[i][0], dp[i-1][2] + rgb[i][0])
    dp[i][1] = min(dp[i-1][0] + rgb[i][1], dp[i-1][2] + rgb[i][1])
    dp[i][2] = min(dp[i-1][0] + rgb[i][2], dp[i-1][1] + rgb[i][2])

print(min(dp[n-1]))

