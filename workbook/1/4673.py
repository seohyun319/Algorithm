# silver5 셀프 넘버
# 생성자가 없는 숫자가 셀프 넘버
# 33은 39의 생성자 (33 + 3 + 3 = 39)

all_num = [n for n in range(1, 10001)]
not_self_num = []

# 생성자 있는 숫자들
for num in all_num:
    for n in str(num)  :
        num += int(n)
    if num < 10001:
        not_self_num.append(num)
# 중복 제거한 not_self_num을 all_num에서 제거
for remove_num in set(not_self_num):
    all_num.remove(remove_num)

print(*all_num, sep="\n")


# 시간 초과
# all_num = [n for n in range(1, 10001)]

# for num in range(1, 10001):
#     while num < 10001:
#         for n in str(num):
#             num += int(n)
#         if num in all_num:
#             all_num.remove(num)

# print(*all_num, sep="\n")
