# gold4-14500. 테트로미노
# 기존 코드 시간 초과: 지금까지 구했던 max_num이 이번에 구할 값보다 크면 아예 가질 않는 로직 추가
    # 참고: (https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8)

import sys
input = sys.stdin.readline

# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성
# 회전, 대칭 가능

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

stack = [] # 현재까지 탐색한 애들 담음
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_num = 0

graph_max_num = 0 # 그래프가 가지고 있는 최대값
for i in range(n):
    for j in range(m):
        graph_max_num = max(graph_max_num, graph[i][j])

def dfs(temp_sum):
    global max_num, graph_max_num
    # 지금까지 구했던 max_num이 이번에 구할 값보다 크면 아예 가질 않음
    # 이번에 구할 값의 최대 경우: 
        # temp_sum + 현재 시점에서 나머지 칸(현재는 len(stack)만큼 옴, 나머지 칸 개수는 4 - len(stack)임)이 전부 최대값인 경우
    if max_num >= temp_sum + graph_max_num * (4 - len(stack)):
        return
    if len(stack) == 4: # 4개까지 탐색: 테트로미노
        max_num = max(max_num, temp_sum)
        return 
    for a, b in stack:
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and [nx, ny] not in stack:
                stack.append([nx, ny])
                temp_sum += graph[nx][ny]
                dfs(temp_sum)
                stack.pop()
                temp_sum -= graph[nx][ny]

for i in range(n):
    for j in range(m):
        stack = [[i, j]] # 처음 값 넣어줌
        dfs(graph[i][j])

print(max_num)
