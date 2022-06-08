# C7. 이진 탐색 - 실전문제 '떡볶이 떡 만들기'

import sys
put = sys.stdin.readline

n, m = list(map(int, put().split()))
heights = list(map(int, put().split()))

start = 0
end = max(heights)
answer = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 
    #잘랐을 때의 총합
    for i in heights:
        if i > mid:
            total += i - mid    
    # 찾고자 하는 값(m)보다 총합이 적은 경우 왼쪽 확인
    if total < m:
        end = mid - 1
    # 찾고자 하는 값(m)보다 총합이 큰 경우 오른쪽 확인
    else:      
        answer = mid
        start = mid + 1

print(answer)
