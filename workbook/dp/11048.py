# silver1 - 11048. 이동하기 

import sys 
input = sys.stdin.readline

# 미로 안에서 오른쪽, 아래, 대각선(오른쪽아래 방향만)으로 이동 가능할 때, 챙길 수 있는 사탕 개수 최댓값
n, m = map(int, input().split())
candies = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        candies[i][j] += max(candies[i][j-1], candies[i-1][j], candies[i-1][j-1]) 

print(candies[n][m])

