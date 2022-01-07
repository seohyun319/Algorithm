# C6. 정렬 - 실전문제 '두 배열의 원소 교체'

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)  # b는 큰 값부터 오게.

for i in range(k):
    if a[i]  < b[i]: # a가 b보다 작은 경우 swap
        a[i], b[i] = b[i], a[i]
    else: break

print(sum(a))

