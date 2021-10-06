# C4. 구현 - '상하좌우'

import sys
put = sys.stdin.readline
n = int(put())
plan = list(put().split())
x=1
y=1
for i in plan:  
    if i=='R': 
        if x==n: continue
        else: x+=1
    elif i=='L': 
        if x==1: continue
        else: x-=1
    elif i=='U': 
        if y==1: continue
        else: y-=1
    elif i=='D': 
        if y==n: continue
        else: y+=1
print(y, x)


