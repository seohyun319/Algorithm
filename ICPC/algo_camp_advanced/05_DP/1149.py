# silver1-1149. RGB거리

import sys
input = sys.stdin.readline

n = int(input()) # 집의 수
costs = [list(map(int, input().split())) for _ in range(n)] # 각 집을 빨강, 초록, 파랑으로 칠하는 비용

for i in range(1, n):
    for j in range(3):
        costs[i][j] += min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3])

print(min(costs[-1]))
