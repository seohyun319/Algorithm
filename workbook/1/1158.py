# silver4 요세푸스 문제
import sys 
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n+1))
pop_list = []

while q:
    q.rotate(-(k - 1))
    pop_num = q.popleft()
    pop_list.append(pop_num)

print("<", end='')
print(*pop_list, sep=', ', end='')
print(">")