# silver4 괄호
import sys 
input = sys.stdin.readline

t = int(input()) 
for _ in range(t):
    stack = [] # 테스트 케이스마다 스택 초기화
    ps = input().rstrip() # 각 줄 입력
    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append("(")        
        # )가 오고 스택 맨 위가 (일 때
        elif ps[i] == ")" and stack and stack[-1] == "(": 
                stack.pop()
        else:
            stack.append("-")
    # 정답 출력: 스택에 - or (가 남아있으면 올바른 괄호 문자열이 아님
    if stack: print("NO")
    else: print("YES")
        

# 기존에 )가 왔는데 pop해야 하는 경우를 
# elif ps[i] == ")" and stack: 
# 로 처리했더니 )가 짝수 번 오는 케이스는 그냥 pop됨 
# (첫 번째는 -가 append되고 두 번째에는 -가 있으니까 stack은 true가 돼서..)
# -> 조건을 스택에 무언가가 존재할 때가 아니라 스택의 맨 위가 (일 경우로 바꿔줌
# elif ps[i] == ")" and stack[-1] == "(": 
# 로 하니까 스택에 아무것도 안 남아있는데 )가 오는 경우 에러 남
# -> stack이 존재하는지까지 처리해야