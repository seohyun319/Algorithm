# silver4-1026. 보물

# 길이가 N인 정수 배열 A와 B
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 최소로 만들기 위해 A의 수를 재배열 (A만)
# S의 최솟값을 출력

import sys
put = sys.stdin.readline
n = int(put()) # 길이
a = list(map(int, put().split())) # A 배열
b = list(map(int, put().split())) # B 배열

# A를 재배열해 B의 가장 큰 수와 A의 가장 작은 수가 곱해지게 해야 함
# A 오름차순, B 내림차순 정렬하면 됨. 근데 B는 정렬하면 안 되는데 어떡하지..?
# 둘 다 정렬해서 계산해도 A는 원본 배열 바꾸고 B는 얕은 복사로 하면 되지 않을까
# 문제에서 재배열된 A배열을 요구하지 않으니까 신경 안 쓰고 저렇게 해도 될 듯

a.sort()
b.sort(reverse=True)

sum = 0
for i in range(n):
  sum += a[i]*b[i]
print(sum)