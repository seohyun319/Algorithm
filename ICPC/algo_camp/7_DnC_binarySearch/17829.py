# silver2-17829. 222-풀링

import sys
input = sys.stdin.readline

# 222-풀링:
# 1. 행렬을 2×2 정사각형으로 나눈다.
# 2. 각 정사각형에서 2번째로 큰 수만 남긴다. 
# 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

def pooling(graph, size):
    if size == 1: return graph[0][0]
    new_graph = [[] for _ in range(size // 2)]
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            four = [graph[i][j], graph[i][j + 1], graph[i + 1][j], graph[i + 1][j + 1]]
            four.sort()
            new_graph[i // 2].append(four[2]) # 두번째로 큰 수
    return pooling(new_graph, size // 2)

print(pooling(array, n))