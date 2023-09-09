# silver3-1935. 후위 표기식2

import sys
input = sys.stdin.readline

# num_idx를 1씩 올려주며 다음 수를 보는 방식은 같은 알파벳이 여러 번 오는 경우 커버가 안 됨
# if x.isalpha():
#     stack.append(nums[num_idx])
#     num_idx += 1

n = int(input())
formula = list(input().rstrip())
nums = [int(input()) for _ in range(n)]
stack = []

for x in formula:
    if x.isalpha():
        stack.append(nums[ord(x) - ord('A')]) # A는 0번 인덱스
    else: 
        second = stack.pop()
        first = stack.pop()
        if x == "+": 
            stack.append(first + second)
        if x == "-": 
            stack.append(first - second)
        if x == "*": 
            stack.append(first * second)
        if x == "/": 
            stack.append(first / second)

print("%.2f" %stack[0])
