# silver3 - 1003. 피보나치 함수

import sys

input = sys.stdin.readline


def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    # 이미 계산했으면 그대로 쓰기
    if dp[x] != 0:
        return dp[x]
    # 계산한 적 없으면 새로 계산
    dp[x] = fibonacci(x - 1) + fibonacci(x - 2)

    return dp[x]


t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 1] + [0] * (n - 1)

    fibonacci(n)
    print(dp[n - 1], dp[n])


# 시간 초과
"""
def fibonacci(x):
    global zero, one
    if x == 0:
        zero += 1
        return 0
    if x == 1:
        one += 1
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 0, 0
    
    fibonacci(n)
    print(zero, one)
"""
