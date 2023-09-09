# silver3-15652. N과 M(4)

import sys
put = sys.stdin.readline

# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순

n, m = map(int, input().split())
array = []

def back(i):
    if len(array) == m: # m개만큼 고름
        print(*array)
        return
    for num in range(i, n + 1): 
        array.append(num) # 자식으로 이동
        back(num) 
        array.pop() # 부모로 이동

back(1)
