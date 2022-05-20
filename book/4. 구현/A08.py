# C12. 구현 - 기출 문제 '문자열 재정렬'

import sys
input = sys.stdin.readline

# 알페벳 오름차순 출력한 뒤 모든 숫자 더한 값 이어서 출력
# K1KA5CB7이 오면 ABCKK13 출력

s = str(input().rstrip())
sum = 0
alpa_list = []

for i in s:
    if i.isalpha():
        alpa_list.append(i)
    else: sum += int(i)

alpa_list.sort()

print(''.join(alpa_list), end='')
if sum: print(sum) # sum이 0이 아닐 때 출력. 