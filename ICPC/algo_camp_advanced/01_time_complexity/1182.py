# silver2-1182. 부분수열의 합

import sys
input = sys.stdin.readline

# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0 # 경우의 수
array = []

def back(depth, nums_sum): 
    global cnt
    if depth == n:
        if nums_sum == s:
            cnt += 1
        return    
    back(depth + 1, nums_sum) # 새 숫자 안 더해주는 케이스
    back(depth + 1, nums_sum + nums[depth]) # 인덱스(depth)에 해당하는 숫자 더해주는 케이스


back(0, 0)
if s == 0: cnt -= 1 # 부분수열의 길이가 0인 경우 (부분수열이 아무것도 없을 때) 케이스 대응
print(cnt)

"""
# 기존에 인덱스 백트래킹이 아니라 그냥 백트래킹 해줘서 틀림. 
def back(idx):
    global cnt
    if array and sum(array) == s:
        cnt += 1
    for i in range(idx, n):
        array.append(nums[i])
        back(i+1)
        array.pop()

back(0)
print(cnt)
    """


"""
# ? nums_cnt를 받아서 if s == 0: cnt -= 1를 안 해주는 코드
def back(depth, nums_sum, nums_cnt): 
    global cnt
    if depth == n:
        if nums_sum == s and nums_cnt > 0:
            cnt += 1
        return    
    back(depth + 1, nums_sum, nums_cnt) # 새 숫자 안 더해주는 케이스
    back(depth + 1, nums_sum + nums[depth], nums_cnt + 1) # 인덱스(depth)에 해당하는 숫자 더해주는 케이스


back(0, 0, 0)
"""