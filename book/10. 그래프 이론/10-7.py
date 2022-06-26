# C10. 그래프 이론 - 실전 문제 '팀 결성'

import sys
put = sys.stdin.readline

n, m = map(int, put().split()) #학생 총 n번까지, m은 입력 개수
parent = [0] * (n + 1) # 부모 테이블 초기화하기 

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 테이블상에서, 자기 자신을 부모로 가지도록 설정
for i in range(1, n + 1):
    parent[i] = i


# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, put().split())
    # 합치기(Union) 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기(Find) 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
