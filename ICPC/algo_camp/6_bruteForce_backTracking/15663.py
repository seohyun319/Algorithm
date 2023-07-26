# silver2-15663. N과 M (9)

import sys
input = sys.stdin.readline

# N개의 자연수 중에서 M개를 고른 수열
# 수열은 사전 순으로 증가하는 순서로 출력
# 중복되는 수열을 여러 번 출력하면 안됨

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 마지막거랑 일치하는지만 중복 체크하면 됨

nums.sort()
array = []

def back():
    if len(array) == m:
        for i in array:
            print(nums[i], end=' ')
        print()
        return
    last_num = 0
    for i in range(n): # 인덱스
        if i not in array:
            if nums[i] != last_num:
                array.append(i)
                last_num = nums[i]
                back()
                array.pop()

back()
