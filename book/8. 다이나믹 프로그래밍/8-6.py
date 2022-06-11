# C8. 다이나믹 프로그래밍 - 실전문제 '개미 전사'

import sys
put = sys.stdin.readline

# i-1번째를 털면 현재(i번째)의 식량 창고는 못 함(연속돼서)
# i-2번째를 털면 현재(i번째)와 함께 털 수 있음
# a(i) = max(a(i-1), a(i-2) + k)

n = int(put())
foods = list(map(int, put().split()))

d = [0]*101 # dp 테이블 초기화

d[0] = foods[0] # 원소가 하나면 최대값은 자기 자신
d[1] = max(foods[0], foods[1]) # 두 개면 최대값은 둘 중 최대

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + foods[i])

print(d[n-1]) # 리스트가 0부터 시작해서
