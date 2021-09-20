# C3. GREEDY

import sys
put = sys.stdin.readline

n = int(put())
count = 0

list = [500, 100, 50, 10]
for coin in list:
    # n - i
    # count =+ 1
    count += n // coin
    n %= coin

print(count)


