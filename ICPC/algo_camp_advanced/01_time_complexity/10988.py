# bronze2-10988. 팰린드롬인지 확인하기

import sys
input = sys.stdin.readline

word = input().rstrip()
if word == word[::-1]: 
    print(1)
else:
    print(0)