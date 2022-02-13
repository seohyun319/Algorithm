# silver4-10816. 숫자 카드 2

import sys
put = sys.stdin.readline

# m이 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지

n = int(put()) # 가지고 있는 카드의 개수
cards = list(map(int, put().split())) # 카드에 적혀있는 정수
m = int(put())
nums = list(map(int, put().split())) # 몇 개 가지고 있는지 구해야 할 정수

# 찾고자 하는 원소 개수 구할 때 upper_bound - lower_bound 로 구할 수 있음. 이렇게하면 R - L +1처럼 다른 연산(+1) 고려 안 해도 됨.
# 리스트에서 없는 수 구하려고 하면 lower_bound와 upper_bound가 같은 주소값 가리킬 것. 그러면 lower_bound - upper_bound = 0 이 될 것.

def LowerBound(left, right, key):
  while left < right:
    mid = int((left + right)/2)
    if cards[mid] < key:
      left = mid + 1
    elif cards[mid] >= key:
      right = mid
  return right

def UpperBound(left, right, key):
  while left < right:
    mid = int((left + right)/2)
    if cards[mid] <= key:
      left = mid + 1
    elif cards[mid] > key:
      right = mid        
  return right

# 이분 탐색은 '정렬된' 리스트에서 특정 값 찾음
cards.sort()

for i in nums:
  print(UpperBound(0, n, i) - LowerBound(0, n, i), end=' ')
