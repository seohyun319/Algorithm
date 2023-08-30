# gold4-2661. 좋은수열

import sys
input = sys.stdin.readline

# 나쁜 수열: 동일한 부분수열이 붙어있음
# 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력

n = int(input())
array = [] 

# 이번 숫자 넣었을 때 좋은 수열이 깨지는지 아닌지 체크
# 마지막 기준으로 1, 2, 3.. 길이만큼 직전 거랑 체크
def check(num): # 이번에 체크할 숫자
    # 1인 케이스는 array[-1] != num에서 체크하고 들어오니까 2부터 
    # 마지막 숫자(이번에 체크할 숫자) 포함한 길이 (len(array) + 1)에서 
    # 2로 나누고 (바로 인접한 부분수열까지 체크하기 때문에 길이가 6일 때 앞의 3, 뒤의 3을 체크하면 됨)
    # range 마지막 1 더해줌        
    for length in range(2, (len(array) + 1) // 2 + 1):
        check_array = array[:] + [num]
        if check_array[-length : ] == check_array[-(length * 2) : -length]:
            return False
    return True

def back():
    if len(array) == n:
        print(*array, sep='')
        exit()
    for num in range(1, 4):
        # array가 비어있거나
        # 바로 직전 거랑 동일하지 않으면
        # 체크하고 true면 append
        if (not array or array[-1] != num) and check(num):
            array.append(num)
            back()
            array.pop()

back()