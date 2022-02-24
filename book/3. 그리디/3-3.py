# C3. GREEDY - 실전 문제 '숫자 카드 게임'

import sys
put = sys.stdin.readline
answer=0
n, m = map(int, put().split())
for i in range(1, n+1):
    nums = list(map(int, put().split()))
    answer_list = min(nums)
    answer = max(answer, answer_list)    
print(answer)