#silver3_atm

import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result=0

arr.sort()

for i in range(num):
    result += arr[i]*(num-i)

print(result)