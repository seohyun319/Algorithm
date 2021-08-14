#2309 일곱 난쟁이
import sys

nsum = 0
dwarf = []
for _ in range(9):
    height = int(sys.stdin.readline())
    dwarf.append(height)
    nsum += height

dwarf.sort()

for i in range(9):
    for j in range(9):
        if nsum - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k!=i and k!=j: print(dwarf[k])
            sys.exit() #프로그램 종료 (break는 for문 끝냄)
