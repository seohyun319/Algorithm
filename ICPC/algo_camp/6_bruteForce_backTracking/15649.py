# silver3-15649. N과 M (1)

import sys
input = sys.stdin.readline

# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n, m = map(int, input().split())
array = []

def back(i):
    if len(array) == m: # 정답이면 출력
        print(*array)
        return
    for num in range(1, n + 1): # 자식 노드에 대해: 1부터 n까지의 수
        if num not in array: # 정답에 유망: 중복 안 됨
            array.append(num) # 자식으로 이동
            back(i + 1) # 재귀
            array.pop() # 부모로 이동

back(0)