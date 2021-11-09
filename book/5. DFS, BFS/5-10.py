#C5. DFS/BFS - 실전문제 '음료수 얼려 먹기'

# import sys
# put = sys.stdin.readline
n, m = map(int, input().split())
shape = []
for i in range(n):
    shape.append(list(map(int, input())))

def dfs(x, y):
    #범위 넘어가면 끝냄
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False    
    if shape[x][y] == 0:  
        #방문 처리      
        shape[x][y] = 1
        #상좌우하 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)

