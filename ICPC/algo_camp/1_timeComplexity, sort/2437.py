
# gold2-2437. 저울

import sys
input = sys.stdin.readline

# 추를 사용해 측정할 수 없는 양의 정수 무게 중 최솟값

n = int(input()) # 저울추의 개수
weight_list = list(map(int, input().split())) # 저울추의 무게

# 1 2 3로 만들 수 있는 것: 1 2 3 4 5 6 -> 측정 불가한 최소 7. 
# 1 1 2 6로 만들 수 있는 것: 1 2 3 4 6 7 8 9 10 -> 측정 불가한 최소 5.
# 1 1 2로 만들 수 있는 최대 무게인 4 다음에는 1 더한 5를 만들 수 있어야.
# 다음 추는 5보다 큰 6이 와서 연속성 깨짐. 탈락. 

weight_list.sort()
answer = 0
for weight in weight_list:
    # 이번 무게가 전 거 다 합친 거 + 1보다 크면 안 됨
    if weight > answer + 1:
        break
    # 현재까지의 모든 무게 합
    answer += weight
print(answer + 1) # 전 거 다 합친 거 + 1 