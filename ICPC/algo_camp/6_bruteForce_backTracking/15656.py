# silver3-15656. N과 M (7)

import sys
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 수열은 사전 순으로 증가하는 순서로 출력
# 고른 수열은 오름차순이어야 한다.

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
array = []

def back():
    if len(array) == m:
        print(*array)
        return
    for i in nums:
        array.append(i)
        back()
        array.pop()

back()
