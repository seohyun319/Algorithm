# gold4-4803. 트리

import sys
input = sys.stdin.readline

# 트리는 사이클이 없는 연결 요소. 
# 그래프 주어졌을 때 트리 개수 세기

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    parent = [i for i in range(n + 1)]
    cycles = []
    cycle_parent = set() # 사이클이 발생한 노드의 부모 노드
    tree = 0
    for _ in range(m):
        a, b = map(int, input().split()) # 간선
        if find_parent(parent, a) != find_parent(parent, b): # 부모가 다르면 트리 합쳐줌
            union_parent(parent, a, b)
        else: cycles.append(a) # 부모가 같으면 사이클 리스트에 추가
    
    for i in range(n+1):
        find_parent(parent, i)

    for cycle in cycles:
        cycle_parent.add(parent[cycle])
    
    for i in set(parent): # 중복 제거한 부모 노드 리스트에서
        # 부모 노드가 사이클이 없으면 
        # (i != 0은 초기값 세팅이 0이라서 넣어줌. 0번 인덱스의 값인 0을 제외)
        if i != 0 and i not in cycle_parent: 
            tree += 1 # 트리 개수 추가

    if tree == 0: print(f'Case {case}: No trees.')
    elif tree == 1: print(f'Case {case}: There is one tree.')
    else: print(f'Case {case}: A forest of {tree} trees.')

    case += 1