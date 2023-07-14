# silver3-15655. N과 M (6)

import sys
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 수열은 사전 순으로 증가하는 순서로 출력
# 같은 수를 여러 번 골라도 된다.

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
array = []

def back(i):
    if len(array) == m:
        print(*array)
        return
    for idx in range(i, n):
        array.append(nums[idx])
        back(idx + 1)
        array.pop()

back(0)
