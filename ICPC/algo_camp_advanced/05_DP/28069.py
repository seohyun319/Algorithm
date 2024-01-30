# gold5-28069. 김밥천국의 계단

import sys
input = sys.stdin.readline

# 민희가 미니김밥을 먹을 수 있는지 구하기
# 민희는 매번 2가지 행동 중 하나를 선택해 총 K번 행동 가능
# 정확히 K번째 행동에서 N번째 계단에 도달하면 미니김밥 먹을 수 있음
# 1. 계단 한 칸 올라가기
# 2. 지팡이 두드려 i + i/2번째 계단으로 순간이동

n, k = map(int, input().split()) # 계단 개수, 계단 오르는 횟수
INF = 10 ** 9
dp = [INF]*(n+1)
dp[0] = 0
dp[1] = 1

# 1
# 2 / 2 + 1 (3)
# 3 / 3 + 1 (4)
# 4 / 4 + 2 (6)

for stair in range(n+1):
    first_action = stair + 1
    second_action = stair + stair // 2
    if first_action <= n:
        dp[first_action] = min(dp[first_action], dp[stair] + 1)
    if second_action <= n:
        dp[second_action] = min(dp[second_action], dp[stair] + 1)

# 0번째와 1번째에 2번 행동을 하면 이동 없이 행동 수를 늘릴 수 있음
# 0번째와 1번째에 행동을 더 할 수도 있기 때문에 ==이 아니라 <=로 비교함
if dp[n] <= k:
    print("minigimbob")
else:
    print("water")


"""
# 메모리 초과
dp = [[0]*(n+1) for _ in range(k+1)]

dp[0][0] = 1
for action in range(k):
    for stair in range(n+1):
        if dp[action][stair] == 1:
            if stair + 1 <= n:
                dp[action + 1][stair + 1] = 1
            if stair + stair // 2 <= n:
                dp[action + 1][stair + stair // 2] = 1
            
if dp[k][n] == 1:
    print("minigimbob")
else:
    print("water")

"""