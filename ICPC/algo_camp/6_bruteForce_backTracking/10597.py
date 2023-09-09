# silver1-10597. 순열장난

import sys
input = sys.stdin.readline

# 공백이 사라진 수열이 주어질 때, 복구된 수열 출력
# 순열은 1부터 N까지의 수로 이루어짐. 모두 10진수이고 공백으로 분리됨

nums = input().rstrip()
array = []

# 앞자리수 0 아니게 하면 될 듯
# 1부터 순서대로 다 있는 순열이니까 길이가 9 이하면 1부터 n까지 있는 것
# 길이가 10 이상이면 길이에서 1~9의 경우인 9를 뺌. 그리고 그 수에서 2씩 나누면 됨 (두 자리 수로 이뤄져 있으니까)
if len(nums) < 10: 
    n = len(nums)
else:
    n = 9 + (len(nums) - 9) // 2

def back(i):
    if i == len(nums):
        print(*array)
        exit()
    if nums[i] != "0": # 앞자리가 0이 아님
        single = nums[i] # 한자리수
        double = nums[i : i + 2] # 두자리수
        # 한자리수
        if int(single) <= n and single not in array:
            array.append(single)
            back(i + 1)
            array.pop()
        # 두자리수
        if int(double) <= n and double not in array:
            array.append(double)
            back(i + 2)
            array.pop()            

back(0)

print(array)
