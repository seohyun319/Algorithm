# silver3-15654. N과 M (5)

import sys
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 수열은 사전 순으로 증가하는 순서로 출력

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
array = []

def back():
    if len(array) == m:
        print(*array)
        return
    for i in nums:
        if i not in array:
            array.append(i)
            back()
            array.pop()

back()
