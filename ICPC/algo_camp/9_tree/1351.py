# gold4-1351. 무한 수열

import sys
input = sys.stdin.readline

# 무한 수열 A
# A0 = 1
# Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
# An 구하기

n, p, q = map(int, input().split()) 
array = {} # 딕셔너리

def dfs(n):
    if n < 1: return 1
    elif n in array: return array[n]
    array[n] = dfs(n//p) + dfs(n//q)
    return array[n]

print(dfs(n))
