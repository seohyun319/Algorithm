#silver4_덱

# 왜 틀린 건지 모르겠어요..
import sys
put = sys.stdin.readline
from collections import deque
# deque: stack & queue를 합친 자료구소 (가장 자리에 원소 삽입, 삭제 가능)
#        append: 오른쪽 삽입, deque: 왼쪽 삽입, popleft: 왼쪽 원소 제거. clear

num = int(put())
q = deque()

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