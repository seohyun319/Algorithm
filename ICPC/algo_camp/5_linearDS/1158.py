# silver4-1158. 요세푸스 문제
import sys 
from collections import deque
input = sys.stdin.readline

# (N, K)-요세프스 순열 구하기
# 요세푸스 순열: 원을 이뤄 앉아있는 사람 중 k번째 사람을 순서대로 제거. 

n, k = map(int, input().split())
q = deque(range(1, n+1))
pop_list = []

# 원형으로 앉아있음 -> 원형 큐 생각하면 됨. 

while q:
    q.rotate(-(k - 1))
    pop_num = q.popleft()
    pop_list.append(pop_num)
print("<", end='')
print(*pop_list, sep=', ', end='')
print(">")