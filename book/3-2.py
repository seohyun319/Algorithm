# C3. GREEDY - 실전 문제 '큰 수의 법칙'

import sys
put = sys.stdin.readline

n, m, k = map(int, put().split())
nums = list(map(int, put().split()))
sum = 0

nums.sort(reverse=True)
for i in range(1, m+1):
    if i < k: 
        sum += nums[0]
    elif i % k != 1:
        sum += nums[0]
    elif i % k == 1:
        sum += nums[1]
print(sum)
