# level2. 주식가격

# 주식 가격이 떨어지지 않은 기간은 몇 초인지

# 초 단위로 기록된 주식가격이 담긴 배열 prices

# 스택에 순차적으로 담다가 하락장인 시점에 새로 정산, 끝나고 나머지 정산
def solution(prices):
    times = [0] * len(prices)
    stack = []
    total_time = len(prices)
    for i in range(total_time):
        # 주식 그래프 꺾인 시점. 하락장 진입
        while stack and stack[-1][1] > prices[i]:
            desc_idx, desc_price = stack.pop()
            times[desc_idx] = i - desc_idx
        stack.append((i, prices[i]))
    # 나머지 시점 정산
    for idx, price in stack:
        times[idx] = total_time - idx - 1
        
    return times



# 기존 풀이: 2중for문
"""
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                # 하락장
                answer[i] += 1
                break
    return answer
"""


# print(solution([1, 2, 3, 2, 3]))
print(solution([1, 2, 1, 3, 2, 4]))