# silver4 - 10828. 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = input().split()
    
    if order[0] == 'push':
        stack.append(int(order[1]))
    if order[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    if order[0] == 'size':
        print(len(stack))
    if order[0] == 'empty':
        if stack: print(0)
        else: print(1)
    if order[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
