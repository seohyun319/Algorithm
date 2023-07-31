# silver3-15666. N과 M (12)

import sys
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 수열은 사전 순으로 증가하는 순서로 출력
# 같은 수를 여러 번 골라도 된다.
# 중복되는 수열을 여러 번 출력하면 안됨
# 고른 수열은 비내림차순

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
array = []

def back(idx):
    if len(array) == m:
        for i in array:
            print(nums[i], end=' ')
        print()
        return
    last_num = 0
    for i in range(idx, n): 
        if nums[i] != last_num:
            array.append(i)
            last_num = nums[i]
            back(i)
            array.pop()

back(0)
