# C3. GREEDY - 실전 문제 '1이 될 때까지'

import sys
put = sys.stdin.readline
n, k = map(int, put().split())
num=0
while n!=1:
    if n%k==0: 
        n=n/k
        num+=1
    else: 
        n=n-1
        num+=1
print(num)
    


