data = [[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]
data2 = [[1, 0, 3], [2, 1, 3], [3, 3, 2], [4, 9, 1], [5, 10, 2]]
data3 = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]	


def solution(data):
    waiting = []
    processing = []
    sub_processing = []
    answer = []

    sec = 0
    while data or waiting or sub_processing or processing:
        while data and data[0][1] == sec:
                waiting.append(data.pop(0))

        if waiting and not processing and not sub_processing:
            waiting = sorted(waiting, key=lambda x: x[2])
            min_time = waiting[0][1]
            while waiting[0][1] == min_time:
                sub_processing.append(waiting.pop(0))
                if not waiting:
                    break

        if sub_processing and not processing:
            sub_processing = sorted(sub_processing, key=lambda x: x[1])
            processing.append(sub_processing.pop(0))
        
        if processing:
            for process in processing:
                process[2] -= 1
            if processing[0][2] == 0:
                answer.append(processing.pop(0)[0])
        sec += 1

    return answer

print(solution(data))
print(solution(data2))
print(solution(data3))


