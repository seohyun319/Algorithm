#C5. DFS/BFS - 실전문제 '음료수 얼려 먹기' - 2번째

import sys
input = sys.stdin.readline

# 구멍 0, 칸막이 1일 때 생성되는 아이스크림의 개수
# 구멍 연결하면 아이스크림 하나

n, m = map(int, input().split()) 
graph = [list(map(int, input().rstrip())) for _ in range(n)]
answer = 0
print(graph)

def dfs(x, y):
    # 범위 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 방문 안 했다면 방문
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 연결된 노드 재귀적 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)
    

# 4 5
# 00110
# 00011
# 11111
# 00000