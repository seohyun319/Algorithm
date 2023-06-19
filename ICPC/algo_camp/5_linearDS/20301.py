# silver3-20301. 반전 요세푸스
import sys 
from collections import deque
input = sys.stdin.readline

# (N, K, M)-반전 요세프스 순열 구하기
# 요세푸스 순열: 원을 이뤄 앉아있는 사람 중 k번째 사람을 순서대로 제거. 
# 반전: M명의 사람이 제거될 때마다 원 돌리는 방향 바꿈

n, k, m = map(int, input().split())
q = deque(range(1, n+1))
pop_list = []
removal_number = 0 # 제거된 횟수
rotate_content = -(k - 1) # q.rotate 안에 들어갈 내용

# 원형으로 앉아있음 -> 원형 큐 생각하면 됨. 

while q:
    if removal_number == m: # 방향 바꿀 때가 옴
        if rotate_content == k:
            rotate_content = -(k - 1)
        else: rotate_content = k
        removal_number = 0
    q.rotate(rotate_content)
    pop_num = q.popleft()
    pop_list.append(pop_num)
    removal_number += 1

print(*pop_list, sep='\n', end='')
