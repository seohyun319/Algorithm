# gold3-11049. 행렬 곱셈 순서

import sys
input = sys.stdin.readline

# 행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하기

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n): 
    for j in range(n - i): # 대각선에서의 열
        dp[j][j+i] = 2**32 # 최댓값
        for k in range(j, j + i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + a[j][0] * a[k][1] * a[j+i][1])
print(dp[0][n-1])