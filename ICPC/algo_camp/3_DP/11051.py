# silver2-11051. 이항 계수 2

import sys
input = sys.stdin.readline

# 이항계수 n k => nCk = (n!) / ((n-k)!k!)

n, k = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

coefficient = factorial(n) // (factorial(n - k) * factorial(k))
print(coefficient % 10007)