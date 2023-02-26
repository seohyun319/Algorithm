# silver4-2003. 수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0 # 합이 m이 되는 경우의 수

for i in range(n):
    # 수 하나만으로 m 만족하는 경우
    if array[i] == m: cnt += 1
    # 합으로 m 만족하는 경우
    temp_sum = array[i]
    for j in range(i + 1, n):
        temp_sum += array[j]
        if temp_sum == m:
            cnt += 1
print(cnt)




# 다른 풀이: 합 리스트에서 빼는 방식. 
# temp_sum[i] - temp_sum[j]은 array[j] + ... + array[i]와 동일

# n, m = map(int, input().split())
# array = list(map(int, input().split()))

# temp_sum = [0]
# sum = 0
# for number in array:
#     sum += number
#     temp_sum.append(sum)

# cnt = 0
# for i in range(n + 1):
#     for j in range(i):
#         if temp_sum[i] - temp_sum[j] == m:
#             cnt += 1

# print(cnt)