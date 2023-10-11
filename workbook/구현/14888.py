# silver1-14888. 연산자 끼워넣기

import sys
from itertools import permutations
input = sys.stdin.readline

# 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하기

n = int(input())
array = list(map(int, input().split()))
plus, minus, multiplication, division = map(int, input().split())
result_list = []

operation_list = ["+"] * plus + ["-"] * minus + ["*"] * multiplication + ["/"] * division
stack = []
# 1번 방법: itertools의 permutations 사용
# operation_permutation = list(set(permutations(operation_list, n - 1)))
# 2번 방법: 백트래킹으로 operation_permutation 직접 만들기
operation_permutation = []

# operation_permutation 만들기
def back():
    if len(stack) == n - 1:
        operation_permutation.append([operation_list[stack[i]] for i in range(n-1)])        
    last_operator = ""
    for i in range(n - 1):
        if i not in stack:
            if last_operator != operation_list[i]:
                stack.append(i)
                last_operator = operation_list[i]
                back()
                stack.pop()

back()

def division_calculator(a, b):
    if a > 0: return a // b
    else: return -(-a // b)

for operation in operation_permutation:
    result = array[0]
    for i in range(1, n):
        if operation[i-1] == "+":
            result += array[i]
        if operation[i-1] == "-":
            result -= array[i]
        if operation[i-1] == "*":
            result *= array[i]
        if operation[i-1] == "/":
            result = division_calculator(result, array[i])
    result_list.append(result)

print(max(result_list))
print(min(result_list))
