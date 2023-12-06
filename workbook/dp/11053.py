# silver2 - 11053. 가장 긴 증가하는 부분 수열

import sys 
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [1] * (n)

for i in range(n):
    for j in range(i, n):
        if array[j] > array[i]:
            # dp[j] = dp[i] + 1 만 있으면 10 20 10의 경우 마지막 10때문에 덮어씌워짐
            dp[j] = max(dp[i] + 1, dp[j])

print(max(dp))