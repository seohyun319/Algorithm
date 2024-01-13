# level2. 기능개발

import math

# 각 배포마다 몇 개의 기능이 배포되는지 
# 진도 100일 때 배포 가능
# 뒤에 있는 기능은 먼저 완료되더라도 앞 기능 배포되면 그때 같이 배포됨

develop_days = [] # 작업 소요 일자
deploy_works_cnt = [] # 각 배포마다 배포되는 기능 개수
FULL_PROGRESS = 100

# progresses: 먼저 배포돼야 하는 순서대로의 작업 진도
# speeds: 각 작업의 개발 속도
def solution(progresses, speeds):
    total_works_cnt = len(progresses) # 작업 개수
    # 소요일자 각각 계산    
    for day in range(total_works_cnt):        
        left_progress = FULL_PROGRESS - progresses[day]
        left_day = math.ceil(left_progress / speeds[day])
        develop_days.append(left_day)
    
    recent_deploy_planned_day = develop_days[0] # 최신 배포 예정 일자
    deployed_works = 1 # 배포되는 기능 개수
    for i in range(1, total_works_cnt):             
        # 다음 작업 완료일보다 앞 기능 배포예정일이 더 늦으면 기다렸다가 같이 배포
        if recent_deploy_planned_day >= develop_days[i]:
            deployed_works += 1
        # 아니면 앞 배포 열차 먼저 보냄
        else:
            deploy_works_cnt.append(deployed_works)
            recent_deploy_planned_day = develop_days[i]
            deployed_works = 1 # 초기화

    deploy_works_cnt.append(deployed_works) # 남은 애들도 배포    
    
    return deploy_works_cnt