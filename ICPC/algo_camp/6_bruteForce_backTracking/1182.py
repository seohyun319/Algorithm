# silver2-1182. 부분수열의 합

import sys
input = sys.stdin.readline

# 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하기
# 인덱스 백트래킹

n, s = map(int, input().split())
array = list(map(int, input().split()))

sub_array = []
cnt = 0 # 합이 s가 되는 부분수열의 개수
sub_sum = 0

def find_sum_s(i):
    global cnt, sub_sum
    if sub_array and sub_sum == s:
        cnt += 1    
    for idx in range(i, n):
        sub_array.append(idx)
        sub_sum += array[idx]
        find_sum_s(idx + 1)
        sub_sum -= array[sub_array.pop()] # 다시 빼줌

find_sum_s(0)
print(cnt)

