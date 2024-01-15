# level2. 프로세스

from collections import deque

# location번째의 프로세스가 몇 번째로 실행되는지 구하기
# 프로세스 운영 규칙
    # 1. 큐에서 대기중인 프로세스 하나 꺼냄
    # 2. 방금 꺼낸 애보다 우선순위 더 높은 애가 큐에 대기중이면 방금 꺼낸 프로세스를 큐에 다시 넣음
    # 3. 그런 프로세스가 없으면 방금 꺼낸 프로세스 실행. 실행하면 해당 프로세스는 종료

# 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities
# 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location
def solution(priorities, location):
    named_processes = deque() # 프로세스 위치에 따라 번호 매겨진 프로세스들 (중요도, 번호)
    finished_process_cnt = 0 # 실행 완료된 프로세스 개수

    # 프로세스 번호 매김 (중요도, 번호)
    for process, priority in enumerate(priorities):
        named_processes.append((priority, process))
    
    highest_priority = max(named_processes)[0]

    while named_processes:
        current_process = named_processes.popleft()
        # 중요도가 더 높은 프로세스가 있으면 다시 큐에 넣음
        if current_process[0] < highest_priority:
            named_processes.append(current_process)      
        # 아니면 현재 프로세스 실행
        else: 
            finished_process_cnt += 1 
            highest_priority = max(named_processes)[0]
            # 현재 프로세스 번호와 찾는 위치가 동일
            if current_process[1] == location:
                return finished_process_cnt



# 기존 풀이: 우선순위 로직 리팩토링 전. 
# 1. sorted_priorities 리스트
    # 기존: 현재 프로세스를 실행했으면 sorted_priorities를 pop한 이후 [-1]로 계속 제일 마지막 값 뽑음. 
    # 변경: max(named_processes)[0]로 구함
# 2. finished_process
    # 기존: 실행한 프로세스 이름를 순서대로 리스트에 넣어주고, 다 구한 후 해당 리스트를 돌면서 답을 찾음
    # 변경: 프로세스 실행할 때마다 +1씩 해주고 찾는 번호의 프로세스를 발견하면 종료함
"""
def solution(priorities, location):
    named_processes = deque() # 프로세스 위치에 따라 번호 매겨진 프로세스들 (중요도, 번호)
    finished_process = [] # 실행 완료된 프로세스

    # 프로세스 번호 매김 (중요도, 번호)
    for process, priority in enumerate(priorities):
        named_processes.append((priority, process))
    
    sorted_priorities = sorted(priorities)
    highest_priority = sorted_priorities[-1]
    
    while named_processes:
        current_process = named_processes.popleft()
        # 중요도가 더 높은 프로세스가 있으면 다시 큐에 넣음
        if current_process[0] < highest_priority:
            named_processes.append(current_process)      
        # 아니면 현재 프로세스 실행
        else: 
            finished_process.append(current_process[1]) # 프로세스 번호 넣음
            # 다음으로 우선순위 제일 높은 애로 highest_priority 설정
            sorted_priorities.pop()
            if sorted_priorities:
                highest_priority = sorted_priorities[-1]
    
    for x in range(len(finished_process)): 
        if finished_process[x] == location:
            answer = x + 1
    
    return answer 
"""



# 다른 풀이: 우선순위 기준으로 순차적으로 계속 봄
"""
def solution(priorities, location):
    sorted_priorities = sorted(priorities, reverse=True)
    current_idx = 0
    finished_process_cnt = 0 # 실행 완료된 프로세스 개수

    while True:
        # 프로세스 번호, 중요도
        for idx, priority in enumerate(priorities):
            # 현재 보는 거가 제일 우선순위 높은 프로세스
            if priority == sorted_priorities[current_idx]:
                finished_process_cnt += 1
                current_idx += 1
                # 원하는 위치의 프로세스를 보고 있음
                if idx == location:
                    return finished_process_cnt 
"""



print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))