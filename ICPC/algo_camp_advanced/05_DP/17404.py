# gold4-17404. RGB거리 2

import sys
input = sys.stdin.readline

# 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
# 집의 색은 인접한 색 (앞뒤)와 달라야 함
# 이때, 1번 집 왼쪽에는 N번 집이, N번 집 오른쪽에는 1번 집이 있는 순환 구조

n = int(input()) # 집의 수
costs = [list(map(int, input().split())) for _ in range(n)] # 각 집을 빨강, 초록, 파랑으로 칠하는 비용

final_costs = []
INF = 10 ** 9

for first_color in range(3): # 1번 집의 색
    dp = [[INF] * 3 for _ in range(n)] 
    dp[0][first_color] = costs[0][first_color]

    for i in range(1, n):
        for j in range(3):
            # i번째 집을 j색으로 칠할 때, i-1번째 집은 j가 아닌 색으로 칠해야 함
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + costs[i][j]
    
    for last_color in range(3): # n번 집의 색
        # 1번 집의 색과 n번 집의 색이 같은 경우는 제외하고 최종 비용을 구함
        if first_color != last_color: 
            final_costs.append(dp[-1][last_color])

print(min(final_costs))
