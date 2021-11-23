# C6. 정렬 - 실전문제 '위에서 아래로'

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

nums = sorted(nums, reverse=True)

for i in nums:
    print(i, end=' ')