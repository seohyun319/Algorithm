# gold4-2370. 시장 선거 포스터

import sys
input = sys.stdin.readline

# 모든 후보자는 오직 한 개의 포스터만을 벽에 붙일 수 있다.
# 모든 포스터는 벽의 높이와 같게 하고, 포스터 너비는 자유다.
# 벽은 조각으로 나누어져 있으며, 하나의 조각의 단위는 byte다.
# 각각의 포스터는 정해진 벽 부분에 빈틈없이 붙어야 한다.
# 이미 붙이려는 부분에 포스터가 있어도 그 위에다 붙일 수 있다.
# 입력된 순서대로 포스터를 붙인 후에 보이는 포스터의 총 수를 출력

n = int(input()) # 포스터 개수
left_and_right = [list(map(int, input().split())) for _ in range(n)]
coordinate = sorted(set(sum(left_and_right, []))) # 사용되는 좌표들 (sum 이용해 2차원 배열 1차원 배열로 만듦)
positions = {coordinate[i] : i for i in range(len(coordinate))} # 실제 값(coordinate[i])이랑 압축 값(i)을 딕셔너리로 만들어줌
wall = [0] * len(coordinate)
for i in range(n):
    # 실제 값이랑 압축된 값 매칭
    left = positions[left_and_right[i][0]]
    right = positions[left_and_right[i][1]]
    for position in range(left, right + 1):
        wall[position] = i # 해당하는 위치에 이번 포스터 값으로 항상 덮어씌움

print(len(set(wall))) # 보이는 포스터 종류
