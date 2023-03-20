# silver4-1764. 듣보잡
# for문으로 순회해가며 not_seen_people에 not_heard_people 있으면 리스트에 넣는 식으로 했는데 시간 초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard_people = [input().rstrip() for _ in range(n)]
not_seen_people = [input().rstrip() for _ in range(m)]

answer = set(not_heard_people) & set(not_seen_people) # 교집합
print(len(answer))
print(*sorted(answer), sep="\n")