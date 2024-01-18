# level2. 올바른 괄호

def solution(s):
    stack = []
    for i in s:
        if i == "(": 
            stack.append(i)
        elif i == ")": 
            if stack: stack.pop()
            else: return False

    return len(stack) == 0
