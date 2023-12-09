# silver3 - 2579. 계단 오르기
# scores = [int(input()) for _ in range(n)]
# dp = [0] * n
# 으로 했더니 계속 인덱스 에러 남.
# n+2로 바꿨더니 정답

import sys

input = sys.stdin.readline

# 한 번에 하나 혹은 두 계단으로 이동 가능
# 연속된 세 개 계단 불가
# 도착 계단 밟기 필수
# 각 계단에 있는 점수 얻음. 점수 총합 최대 구하기.

n = int(input())
scores = [0 for _ in range(n + 2)]
dp = [0] * (n + 2)
for i in range(n):
    scores[i] = int(input())

dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

print(dp[n - 1])
