# silver3-14425. 문자열 집합

import sys
input = sys.stdin.readline

# check_list중 몇 개가 집합 s에 포함돼있는지

n, m = map(int, input().split())
s_list = [input().rstrip() for _ in range(n)] # 집합 s에 포함돼있는 문자열
check_list = [input().rstrip() for _ in range(m)] # 검사해야 하는 문자열
cnt = 0

for string in check_list:
    if string in s_list: cnt += 1
print(cnt)