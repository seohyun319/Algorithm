# gold4-1915. 가장 큰 정사각형

import sys
input = sys.stdin.readline

"""
2)
    1 1
    1 2
3)
    1 1 1
    1 2 2
    1 2 3
4)
    1 1 1 1
    1 2 2 2
    1 2 3 3
    1 2 3 4
"""

array = []
n, m = map(int, input().split())
for _ in range(n):
    array.append(list(map(int, list(input().rstrip()))))
answer = 0

for i in range(n):
    for j in range(m):
        # i > 0 and j > 0 안 하면 array[i-1][j]의 -1 케이스에서 음수가 되니까 조건으로 걸러줌
        if array[i][j] == 1 and i > 0 and j > 0: # 1로 된 거 크기 구해야 하니까
            array[i][j] += min(array[i-1][j], array[i][j-1], array[i-1][j-1]) 
        answer = max(answer, array[i][j]) # 지금까지 쌓아온 거랑 현재 구한 것 중 최대값

print(answer * answer) # 넓이


"""
기존 틀린 코드:

for i in range(1, n):
    for j in range(1, m):
        if array[i][j] == 1: # 1로 된 거 크기 구해야 하니까
            array[i][j] += min(array[i-1][j], array[i][j-1], array[i-1][j-1]) 
        answer = max(answer, array[i][j]) # 지금까지 쌓아온 거랑 현재 구한 것 중 최대값

반례:
    0 0 0 
    0 0 0 
    1 0 0 
의 경우 기존 코드는 오른쪽 아래 네 칸만 계산하니까 max 계산하는 곳을 아예 못 들어오는 문제

저거 answer를 for문에서 구하지 말고 일단 array 배열 다 구해놓고 거기에서 구하면 될 수도

"""