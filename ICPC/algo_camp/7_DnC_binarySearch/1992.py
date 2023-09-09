# silver1-1992. 쿼드트리

import sys
input = sys.stdin.readline

# 주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"
# 모두 1로만 되어 있으면 압축 결과는 "1"
# 0과 1이 섞여 있으면 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래의 4개의 영상으로 나누어 압축
# 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현

n = int(input())
array = [list(input().rstrip()) for _ in range(n)]
dx = []

# 4칸씩 묶어 표현
def compress(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if array[i][j] != array[x][y]: 
                new_size = size // 2
                return "(" + compress(x, y, new_size) + compress(x, y + new_size, new_size) + compress(x + new_size, y, new_size) + compress(x + new_size, y + new_size, new_size) + ")"
    # size가 1이면 자동으로 여기로 옴
    return array[x][y]

print(compress(0, 0, n))