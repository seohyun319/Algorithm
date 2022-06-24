# C12. 구현 - 기출 문제 '문자열 압축'

import sys
input = sys.stdin.readline

# 1시간 넘게 했는데 안 풀려서 답 방식 보고 이해한 후 다시 풂
# 압축 단위만큼 묶어서 봐야하는 건 아는데 구현을 못함. 
# -> 답지에서는 for문에서 step으로 건너뛰는 방식 사용
# 이전 인덱스의 값과 동일하면 숫자 증가하는 로직은 맞게 함. 

# 압축 단위는 s의 길이를 2로 나눈 만큼까지 가야 함. 절반은 나눠야하기 때문. 

def solution(s):
    answer = len(s)
    
    # 1부터 len(s)를 2로 나눈 값만큼까지 
    for step in range(1, len(s)//2 + 1):
        changed = "" # 압축된 문자열
        num = 1 # 반복되는 문자의 반복 횟수
        prev = s[0: step] # 자른 후 맨 첫 문자열
        
        # step만큼 증가시키며 봄
        for i in range(step, len(s), step):
            now = s[i: i + step]
            if prev == now: # 이전과 중복되면
                num += 1
            else: # 이전 값과 달라지면              
                # 해당 조건문은 한 줄로 압축 가능:
                # changed += str(num) + prev if num > 1 else prev
                if num > 1:
                    changed += str(num) + prev
                else: 
                    changed += prev #num 1은 생략함
                # 초기화
                num = 1
                prev = now # 현재 값을 prev에 넣어줌 
        # 가장 마지막으로 갱신된 prev값 넣어주기
        if num > 1:
            changed += str(num) + prev
        else: changed += prev #num 1은 생략함
        # answer의 초기값은 len(s)
        # 갱신되는 answer과 해당 step의 압축된 문자열 길이를 비교함
        answer = min(answer, len(changed))

    return answer





# 시도 방법1 : 
    # num = 1
    # # 한 개 단위
    # for i in range(1, len(s)):
    #     if s[i-1] == s[i]:
    #         num += 1
    #         print(s[i-1])
    #     # 마지막 인덱스일 경우
    #     elif (i-1) == len(s):
    #         print(num, s[i-1])            
    #     else: 
    #         print(num, s[i-1])
    #         num = 1

# 시도 방법 2:
#     for i in range(len(s)):
#         if (i+1) % 2 == 0:
#             s_list.append(s[i-1:i+1])

#         # print(i)
#     print(s_list)
#     for i in range(len(s_list)-1):
#         num = 1
#         if s_list[i+1] == s_list[i]:
#             num += 1
#         print(num)