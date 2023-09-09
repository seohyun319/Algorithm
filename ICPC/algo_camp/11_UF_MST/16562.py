# gold4-16562. 친구비

import sys
input = sys.stdin.readline

# 친구비를 주면 한 달간 친구가 생긴다! 
# '친구의 친구는 친구다'를 이용해 모든 사람과 친구가 되는 최소 비용 출력, 안 되면 Oh no 출력

n, m, k = map(int, input().split()) # 학생 수, 친구관계 수, 가지고 있는 돈
friend_cost = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b): # 비용 적은 기준으로 합쳐줌
    a = find_parent(a)
    b = find_parent(b)
    if friend_cost[a] < friend_cost[b]:
        parent[b] = a
        friend_cost[b] = 0 # 비용 더 적은 애가 부모가 됐으니까 b의 비용은 더할 필요 없어짐 -> 0으로.
    else: 
        parent[a] = b
        friend_cost[a] = 0

for _ in range(m):
    v, w = map(int, input().split())
    union_parent(v, w) # 친구 관계에 있으니까 합쳐줌

total_cost = sum(friend_cost)
if total_cost <= k:
    print(total_cost)
else: # 친구 사귀는 데 드는 총 비용이 예산보다 크다면 모두와 친구가 될 수 없음
    print("Oh no")
