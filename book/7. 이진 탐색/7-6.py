# C7. 이진 탐색 - 실전문제 '부품 찾기' - 이진 탐색으로 풀기

import sys
put = sys.stdin.readline

n = int(put())
store = list(map(int, put().split()))
m = int(put())
customer = list(map(int, put().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 몫 구함
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

for i in customer:
    result = binary_search(store, i, 0,  n-1)
    if result != None:
        print("yes", end=' ')
    else: print("no", end=' ')
    