# C4. 구현 - 실전문제 '왕실의 나이트'

import sys
put = sys.stdin.readline
n = list(put())
a = ord(n[0]) - ord('a') + 1
b = int(n[1])
count=0
steps = [
    (2,1), (2,-1), (-2,1), (-2,-1), 
    (1,2), (1,-2), (-1,2), (-1,-2)
]

for step in steps:
    x = a+step[0]
    y = b+step[1]
    if x<1 or y<1 or x>8 or y>8:
        continue
    else: count+=1
print(count)