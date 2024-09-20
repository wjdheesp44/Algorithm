n, w, L = map(int, input().split())  # 트럭 수, 다리 길이, 최대하중 입력
truck_weights = list(map(int, input().split()))  # 트럭 무게 입력

bridge = [0] * w  # 다리 위에 올라가 있는 트럭의 상태를 저장하는 큐
total_weight = 0  # 현재 다리 위 트럭들의 무게 합
time = 0  # 경과 시간

for truck in truck_weights:
    while True:
        time += 1
        total_weight -= bridge.pop(0)

        # 다리 위에 트럭을 올릴 수 있으면 올리고 반복 종료
        if total_weight + truck <= L:
            bridge.append(truck)
            total_weight += truck
            break
        else:
            bridge.append(0)

time += w
print(time)