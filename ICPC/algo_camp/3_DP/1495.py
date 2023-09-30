# silver1-1495. 기타리스트

import sys
input = sys.stdin.readline

# 마지막 곡을 연주할 수 있는 볼륨 중 최댓값
# 매번 곡 시작 전 볼륨을 바꾸는데, 리스트에 있는 값대로만 바꿀 수 있음. 
# 리스트 값만큼 더하거나 뺌
# 0보다 작은 값이나 m보다 큰 값은 볼륨으로 설정할 수 없음

n, s, m = map(int, input().split()) # 곡의 개수, 시작 볼륨, 볼륨의 최대값
volumes = list(map(int, input().split())) # 바꿀 수 있는 볼륨 리스트
dp = [[0]*(m+1) for _ in range(n+1)]
max_volume = -1 # 불가능할 경우 -1 출력 위해 초기값 -1로 설정 (max_volume이 갱신되지 않았으면 -1 출력할 것)

dp[0][s] = 1
for x in range(n):
    volume = volumes[x]
    for v in range(m+1):
        if dp[x][v] == 1:
            # 다음 곡의 볼륨 설정: 현재 볼륨에서 리스트에 있는 값만큼 더하거나 뺌
            if v + volume >= 0 and v + volume <= m:
                dp[x + 1][v + volume] = 1
            if v - volume >= 0 and v - volume <= m:
                dp[x + 1][v - volume] = 1

# 마지막 곡을 연주할 수 있는 볼륨 중 최댓값
for v in range(m+1):
    # dp[n]에 1이 있으면 마지막 곡(n번재 곡)까지 연주 가능한 것
    if dp[n][v] == 1:
        max_volume = v

print(max_volume)
