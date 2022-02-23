# C7. 이진 탐색 - 실전문제 '부품 찾기'

import sys
put = sys.stdin.readline

n = int(put())
store = list(map(int, put().split()))
m = int(put())
customer = list(map(int, put().split()))

for i in customer:
    if i in store:
        print("yes", end=' ')
    else: print("no", end=' ')