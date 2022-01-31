#silver4_균형잡힌 세상

import sys
put = sys.stdin.readline

while(1): 
    line = put().rstrip()
    if line == '.': break     
    stack = []
    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if  stack and stack[-1] == "(":
                stack.pop()
                flag=True
                break
            else: flag=False
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
                flag=True
                break
            else: flag=False
    if (flag and not stack) : print("yes")
    elif (not flag or stack): print("no")


'''
def push_front(x):
    q.appendleft(x)

def push_back(x):
    q.append(x)

def pop_front():
    if len(q)==0:
        return -1 
    else:
        return q.popleft()         
        
def pop_back():
    if len(q)==0:
        return -1 
    else:        
        return q.pop()
        
def size():
    return len(q)

def empty():
    if len(q)==0:
        return 1
    else: return 0

def front():
    if len(q)==0:
        return -1
    else: return q[0]
    
def back():
    if len(q)==0:
        return -1
    else: return q[-1]

for _ in range(num):
    order_split = put().split()
    order = order_split[0]
    if order=='push_front':
        push_front(order_split[1])
    if order=='push_back':
        push_back(order_split[1])
    elif order=='pop_front':
        print(pop_front())
    elif order=='pop_back':
        print(pop_back())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())

        '''