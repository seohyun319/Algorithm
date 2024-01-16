# level2. 다리를 지나는 트럭

from collections import deque

# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 
# bridge_length만큼 초가 소요됨 (한 칸에 1초)
"""
# 전부 줄짓지 않고 각자 이동 -> 트럭개수*bridge_length + 1 (다리에서 나가는 1초)
# 줄지어 이동 -> 트럭개수*bridge_length + 1*동시에 있는 애 개수

# 초 기준으로 생각을 바꿔보자
# 1~100, 2~101, 3~102, ..., 8~107, 9~108, 10~109, 110
# 동시에 가도 1초씩 밀림. 시작시간 기준 + bridge_length초 걸림. 
# 마지막 애 시작시간 계산하면 됨
# 스택에 넣은 후에 뺄 때 bridge_length만큼 경과했다 보면 됨
"""
# 다리 진입 시각, 탈출 시각으로 봤을 때
# 진입 시간 최소 1초 간격
# 맨 앞 애 탈출 시각에 조건 성립하면 새로운 애 진입 가능
# 바로 앞 애랑 합쳤을 때 무게 조건 넘으면 바로 앞 애 탈출 시각까지 기다려야

# -> 다리 진입 시각, 탈출 시각 이용해 구하기


# 다리에 동시에 올라갈 수 있는 트럭 최대 수, 다리가 견딜 수 있는 무게, 트럭 별 무게
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    waiting_trucks = deque(truck_weights)
    time_list = deque()
    append_time = 1
    
    while waiting_trucks:
        # 다리에 트럭 새로 추가 가능하면 진입
        if len(bridge) + 1 <= bridge_length and sum(bridge) + waiting_trucks[0] <= weight:
            bridge.append(waiting_trucks.popleft())
            time_list.append((append_time, append_time + bridge_length)) # 진입 시각, 탈출 시각
            append_time += 1 # 다음 진입은 최소 1초 후
        # 진입 불가 시 맨 앞 트럭 빼고 시간 업데이트
        else:
            bridge.popleft()
            # 놓친 케이스:
            # 맨 앞 거가 빠지는 시각과 최소 1초 보정된 값 중 더 큰 거로 갱신
            append_time = max(time_list.popleft()[1], append_time)
        
    return time_list[-1][1] # 최종으로 빠지는 시간



# 다른 방법: 다리에 트럭 못 올라가면 0 올려 다리 길이 유지. 매번 시작 전에 다리에서 popleft해줌. 
"""
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    waiting_trucks = deque(truck_weights)
    total_weight = 0
    time = 0

    while waiting_trucks:
        total_weight -= bridge.popleft()
        time += 1
        if total_weight + waiting_trucks[0] > weight:
            bridge.append(0)
        else:
            current_truck = waiting_trucks.popleft()
            bridge.append(current_truck)
            total_weight += current_truck

    time += bridge_length

    return time
"""



print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))