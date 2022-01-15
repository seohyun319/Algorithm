# silver4-15889. 호 안에 수류탄이야!!

# 마지막 사람까지 무사히 전달해야
# 다음 사람까지의 거리보다 사거리가 짧으면 실패
# "사거리 내의 누구에게나" 전달 가능 -> 건너뛸 수도 있겠네

n=int(input())
location=list(map(int,input().split())) #좌표
# n이 1보다 크다면 다음줄 입력 주어짐. 1이면 안 주어짐
if n==1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()
# 두 사람의 거리보다 사거리가 크면 성공, 작으면 실패
# location[i+1] - location[i] > distance[i]   ====> 실패
# 근데 중간에 건너뛰는 경우도 있음. 
# 현재좌표 + 사거리가 다음사람 좌표보다 작으면 실패
# location[i] + distance[i] < location[i+1] ====> 실패
else:
    distance = list(map(int, input().split())) #사거리
    maxd = 0
    for i in range(n-1):
        maxd = max(maxd, location[i] + distance[i])

        if maxd>=location[i+1]:
            continue
        else:
            print("엄마 나 전역 늦어질 것 같아")
            exit()
    print("권병장님, 중대장님이 찾으십니다")