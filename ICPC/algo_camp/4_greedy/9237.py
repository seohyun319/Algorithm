# silver5-9237. 이장님 초대

n = int(input())
days = list(map(int, input().split()))
days.sort(reverse=True)

finished_date = 0
for idx, day in enumerate(days):
    finished_date = max(finished_date, idx + day + 1) # 날짜(idx는 0부터 시작하니 idx + 1) + 걸리는 일수

print(finished_date + 1) # 다 자란 '다음날'
