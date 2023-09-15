# gold5-5639. 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 트리를 전위 순회한 결과가 주어질 때, 후위순회한 결과 출력
# 전위: 루트-왼-오
# 후위: 왼-오-루트

pre_order = []
while True:
    try: pre_order.append(int(input()))
    except: break

def post_order(array):
    if len(array) <= 1: return array
    for i in range(1, len(array)):
        if array[i] > array[0]: # 루트보다 크면
            return post_order(array[1:i]) + post_order(array[i:]) + [array[0]]
    return post_order(array[1:]) + [array[0]] # 모두 루트보다 작으면

print(*post_order(pre_order), sep="\n")
