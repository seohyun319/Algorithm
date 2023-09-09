# gold4-3078. 좋은 친구

import sys
from collections import deque
input = sys.stdin.readline

# 좋은 친구가 몇 쌍 있는지 구하기
# 모든 학생은 자신과 반 등수의 차이가 K를 넘으면 친구가 아님
# 좋은 친구는 이름의 길이가 같아야 함
# -> 좋은 친구는 등수의 차이가 K를 넘지 않으며 이름의 길이가 같음

n, k = map(int, input().split())
len_names = {i : 0 for i in range(2, 21)} # 2 ~ 20글자
q = deque()
answer = 0

for i in range(n):
    name = input().rstrip() # 성적 순으로 입력됨
    if i > k: # 범위 넘어가면 하나씩 빼줌
        popped_name = q.popleft()
        len_names[len(popped_name)] -= 1 # 딕셔너리에서도 빼줌
    answer += len_names[len(name)] # 이름 같은 수만큼 더함
    q.append(name)
    len_names[len(name)] += 1 # 딕셔너리에 더해줌

print(answer)
