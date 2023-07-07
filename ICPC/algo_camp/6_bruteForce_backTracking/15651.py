# silver3-15650. N과 M(2)

import sys
put = sys.stdin.readline

# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

n, m = map(int, input().split())
array = []

def back(i):
    if len(array) == m: # m개만큼 고름
        print(*array)
        return
    for num in range(1, n + 1): # 자식 노드에 대해: 1부터 n까지의 수       
        array.append(num) # 자식으로 이동
        back(i + 1) 
        array.pop() # 부모로 이동

back(1)
