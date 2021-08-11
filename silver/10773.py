#10773 제로
import sys
put = sys.stdin.readline

num = int(put())
line = []

for _ in range(num):
    money = int(put())
    if (money==0):
        line.pop()
    else:
        line.append(money)

print(sum(line))
