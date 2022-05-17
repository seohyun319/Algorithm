# C12. 구현 - 기출 문제 '럭키 스트레이트'

import sys
input = sys.stdin.readline

# 럭키스트레이트 사용할 수 있는 상태인지 알려주기
# 사용 가능 상황:
# 자릿수 기준으로 캐릭터 점수 N을 반으로 나눠 왼쪽 부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황
# e.g, 123402는 1+2+3 == 4+0+2라서 사용 가능.

n = str(input().rstrip())
half_len = int(len(n)/2)
left = n[:half_len]
right = n[half_len:]
sum_left, sum_right = 0, 0

# 절반으로 나눈 자릿수를 각각 더함
for i in left:
    sum_left += int(i)
for i in right:
    sum_right += int(i)

if sum_left == sum_right:
    print("LUCKY")
else: print("READY")


# --------
# sum_left, sum_right의 2가지 변수로 나누지 않고
# 첫 번째 sum값에서 두 번째 sum값을 빼는 방법도 있다!
# 결과가 0이면 둘이 동일한 것
# for i in range(helf_len):
#     sum += int(n[i])
# for i in range(helf_len, len(n)):
# 이런 식으로 변수 따로 지정 없이 범위를 바로 나눈다