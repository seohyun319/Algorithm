# silver3-15650. N과 M(2)

import sys
put = sys.stdin.readline

# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

n, m = map(int, put().split())
arr = []

def dfs(start):
  # m개만큼 골랐을 때만 프린트
  if len(arr) == m:
    print(' '.join(map(str, arr)))
    return
  for i in range(start, n+1):
    if i not in arr:
      arr.append(i)
      dfs(i+1)
      # 다음 dfs 함수 수행하라고 기존에 넣었던 거 빼줌
      arr.pop()

dfs(1)

"""
n, m = map(int, input().split())
array = []

def back(i):
    if len(array) == m: # m개만큼 고름
        print(*array)
        return
    for num in range(i, n): # 자식 노드에 대해: i부터 n까지의 수
        array.append(num + 1) # 자식으로 이동
        back(num + 1) # 오름차순 다음
        array.pop() # 부모로 이동

back(0)
"""