# bronze3-20360. Binary numbers

import sys
input = sys.stdin.readline

# 2진수로 나타냈을 때 1의 위치
# 증가하는 순서대로 출력
# 13은 1101이므로 0, 2, 3

n = int(input())

binary = bin(n)[2:]
for i in range(len(binary) - 1, -1, -1):
    if binary[i] == '1': 
        print(len(binary) - i - 1, end=' ')