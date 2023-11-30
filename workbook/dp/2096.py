# gold1 - 2096. 내려가기

import sys 
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split()) # 첫 번째 줄 입력값
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]

min_dp[0][0] = max_dp[0][0] = a
min_dp[0][1] = max_dp[0][1] = b
min_dp[0][2] = max_dp[0][2] = c

for i in range(1, n):
    a, b, c = map(int, input().split()) # 2번째 줄부터 for문 돌면서 계속 갱신
    min_dp[i%2][0] = min(min_dp[i%2 - 1][0] + a, min_dp[i%2 - 1][1] + a)
    min_dp[i%2][1] = min(min_dp[i%2 - 1][0] + b, min_dp[i%2 - 1][1] + b, min_dp[i%2 - 1][2] + b)
    min_dp[i%2][2] = min(min_dp[i%2 - 1][1] + c, min_dp[i%2 - 1][2] + c)
    
    max_dp[i%2][0] = max(max_dp[i%2 - 1][0] + a, max_dp[i%2 - 1][1] + a)
    max_dp[i%2][1] = max(max_dp[i%2 - 1][0] + b, max_dp[i%2 - 1][1] + b, max_dp[i%2 - 1][2] + b)
    max_dp[i%2][2] = max(max_dp[i%2 - 1][1] + c, max_dp[i%2 - 1][2] + c)

if n%2 == 1: # n이 홀수면
    print(max(max_dp[0]), min(min_dp[0]))
else: # n이 짝수면
    print(max(max_dp[1]), min(min_dp[1]))




## 3. python3은 메모리초과, pypy는 정답
# n = int(input())
# nums = [list(map(int, input().split())) for _ in range(n)]
# min_dp = [[0] * 3 for _ in range(2)]
# max_dp = [[0] * 3 for _ in range(2)]

# min_dp[0][0] = max_dp[0][0] = nums[0][0] 
# min_dp[0][1] = max_dp[0][1] = nums[0][1] 
# min_dp[0][2] = max_dp[0][2] = nums[0][2] 

# for i in range(1, n):
#     min_dp[i%2][0] = min(min_dp[i%2 - 1][0] + nums[i][0], min_dp[i%2 - 1][1] + nums[i][0])
#     min_dp[i%2][1] = min(min_dp[i%2 - 1][0] + nums[i][1], min_dp[i%2 - 1][1] + nums[i][1], min_dp[i%2 - 1][2] + nums[i][1])
#     min_dp[i%2][2] = min(min_dp[i%2 - 1][1] + nums[i][2], min_dp[i%2 - 1][2] + nums[i][2])

#     max_dp[i%2][0] = max(max_dp[i%2 - 1][0] + nums[i][0], max_dp[i%2 - 1][1] + nums[i][0])
#     max_dp[i%2][1] = max(max_dp[i%2 - 1][0] + nums[i][1], max_dp[i%2 - 1][1] + nums[i][1], max_dp[i%2 - 1][2] + nums[i][1])
#     max_dp[i%2][2] = max(max_dp[i%2 - 1][1] + nums[i][2], max_dp[i%2 - 1][2] + nums[i][2])

# if n%2 == 1: # n이 홀수면
#     print(max(max_dp[0]), min(min_dp[0]))
# else: # n이 짝수면
#     print(max(max_dp[1]), min(min_dp[1]))



## 2. python3은 메모리초과, pypy는 정답
# n = int(input())
# a, b, c = map(int, input().split()) # 첫 번째 줄 입력값
# min_dp = [[0] * 3 for _ in range(n)]
# max_dp = [[0] * 3 for _ in range(n)]

# min_dp[0][0] = max_dp[0][0] = a
# min_dp[0][1] = max_dp[0][1] = b
# min_dp[0][2] = max_dp[0][2] = c 

# for i in range(1, n):
#     a, b, c = map(int, input().split()) 
#     min_dp[i][0] = min(min_dp[i-1][0] + a, min_dp[i-1][1] + a)
#     min_dp[i][1] = min(min_dp[i-1][0] + b, min_dp[i-1][1] + b, min_dp[i-1][2] + b)
#     min_dp[i][2] = min(min_dp[i-1][1] + c, min_dp[i-1][2] + c)

#     max_dp[i][0] = max(max_dp[i-1][0] + a, max_dp[i-1][1] + a)
#     max_dp[i][1] = max(max_dp[i-1][0] + b, max_dp[i-1][1] + b, max_dp[i-1][2] + b)
#     max_dp[i][2] = max(max_dp[i-1][1] + c, max_dp[i-1][2] + c)
    
# print(max(max_dp[n-1]), min(min_dp[n-1]))




## 1. 메모리 초과 (python, pypy)
# n = int(input())
# nums = [list(map(int, input().split())) for _ in range(n)]
# min_dp = [[0] * 3 for _ in range(n)]
# max_dp = [[0] * 3 for _ in range(n)]

# min_dp[0][0] = max_dp[0][0] = nums[0][0] 
# min_dp[0][1] = max_dp[0][1] = nums[0][1] 
# min_dp[0][2] = max_dp[0][2] = nums[0][2] 

# for i in range(1, n):
#     min_dp[i][0] = min(min_dp[i-1][0] + nums[i][0], min_dp[i-1][1] + nums[i][0])
#     min_dp[i][1] = min(min_dp[i-1][0] + nums[i][1], min_dp[i-1][1] + nums[i][1], min_dp[i-1][2] + nums[i][1])
#     min_dp[i][2] = min(min_dp[i-1][1] + nums[i][2], min_dp[i-1][2] + nums[i][2])

# for i in range(1, n):
#     max_dp[i][0] = max(max_dp[i-1][0] + nums[i][0], max_dp[i-1][1] + nums[i][0])
#     max_dp[i][1] = max(max_dp[i-1][0] + nums[i][1], max_dp[i-1][1] + nums[i][1], max_dp[i-1][2] + nums[i][1])
#     max_dp[i][2] = max(max_dp[i-1][1] + nums[i][2], max_dp[i-1][2] + nums[i][2])

# print(max(max_dp[n-1]), min(min_dp[n-1]))
