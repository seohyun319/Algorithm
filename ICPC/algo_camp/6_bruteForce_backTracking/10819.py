# silver2-10819. 차이를 최대로

import sys
input = sys.stdin.readline

# 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값 구하기
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

n = int(input())
nums = list(map(int, input().split()))
array = []
max_num = 0

def formula(index_list):
    sum = 0
    for i in range(n - 1): # 수끼리 연산하니까 연산을 n-2번 함
        sum += abs(nums[index_list[i]] - nums[index_list[i + 1]])
    return sum

def back(i):
    global max_num
    if len(array) == n:
        max_num = max(max_num, formula(array))
        return
    for num in range(n):
        if num not in array:
            array.append(num)
            back(i + 1)
            array.pop()

back(1)
print(max_num)
