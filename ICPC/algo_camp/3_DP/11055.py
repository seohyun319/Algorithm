# silver2-11055. 가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = array[:] # 얕은 복사

for i in range(n):
    for j in range(i, n):
        if dp[j] > dp[i]: # 증가할 때
            dp[j] = max(dp[j], dp[i] + array[j]) # 자기 자신과, 이전 단계까지의 합에 이번 array의 값 구한 것의 크기 비교
print(max(dp))
