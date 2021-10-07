# C4. 구현 - '시각'

import sys
put = sys.stdin.readline
n = int(put())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count+=1
print(count)