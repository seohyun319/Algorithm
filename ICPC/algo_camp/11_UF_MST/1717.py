# gold5-1717. 집합의 표현

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 시작이 0이면 합집합 연산 수행, 
# 입력 시작이 1이면 두 원소가 같은 집합에 포함돼있는지 확인하는 연산 수행
# 1로 시작하는 입력에 대해 둘이 같은 집합에 포함됐는지 여부 출력

n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)] # 초기값: 자기 자신을 부모 노드로 가지게 함

def find_parent(parent, x):
    if parent[x] != x: # 부모노드가 아니면 
        parent[x] = find_parent(parent, parent[x]) # 더 위로 거슬러가며 그의 부모를 찾음
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 루트 노드를 부모로 삼아 둘을 합침
    if a < b: parent[b] = a
    else: parent[a] = b

for operation, a, b in operations:
    if operation == 0:
        union_parent(parent, a, b)
    elif operation == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("yes")
        else: print("no")
