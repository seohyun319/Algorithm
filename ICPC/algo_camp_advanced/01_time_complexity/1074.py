# silver1-1074. Z

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, c = map(int, input().split())
visit_count = 0 # 방문 횟수

# 큰 거부터 구획으로 돌고 작은 거로 재귀로 넘어와야 함
# 몇 사분면인지 체크 후 해당 사분면으로 들어가서 다시 나눔

def visit_graph(y, x, num): # num: 제곱 적용된 배열 칸 개수. 
    global visit_count
    next_num = (num // 2) ** 2 
    if num == 1: return visit_count

    if x < num // 2 and y < num // 2: 
        return visit_graph(y, x, num // 2)
    if x >= num // 2 and y < num // 2: 
        visit_count += next_num
        return visit_graph(y, x - num // 2, num // 2)
    if x < num // 2 and y >= num // 2: 
        visit_count += next_num * 2
        return visit_graph(y - num // 2, x, num // 2)
    if x >= num // 2 and y >= num // 2: 
        visit_count += next_num * 3
        return visit_graph(y - num // 2, x - num // 2, num // 2)

print(visit_graph(r, c, 2**n))