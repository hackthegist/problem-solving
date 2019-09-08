'''
(2018년) KAKAO BLIND RECRUITMENT 무지의 먹방 라이브

입출력 예

food_times	k	result
[3, 1, 2]	5	1
'''

food_times = [100, 20, 0, 31, 591, 6]
k = 200

def solution(food_times, k):

    ft, fc = food_times, len(food_times)
    pos = fc

    if sum(ft) <= k:
        return -1
    
    while k > pos:
        pos = fc
        for i in range(fc):
            if ft[i] == 0:
                pos -= 1
        dvd = k // pos
        for i in range(fc):
            if ft[i] > 0:
                ft[i] -= dvd

        k -= dvd * pos
    
        for i in range(fc):
            if ft[i] < 0:
                k -= ft[i]
                ft[i] = 0
                pos -= 1


    j = 0
    while k != -2:
        if ft[j] > 0:
            ft[j] -= 1
            k -= 1
            if k == -1:
                return j + 1
            j = (j + 1) % len(ft)
        else:
            j = (j + 1) % len(ft)


print(solution(food_times, k))
