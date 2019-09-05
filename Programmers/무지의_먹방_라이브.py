'''
(2018년) KAKAO BLIND RECRUITMENT 무지의 먹방 라이브

food_times	k	result
[3, 1, 2]	5	1
'''

food_times = [1, 2, 0, 3, 5, 6]
k = 20


def solution(food_times, k):

    fc = len(food_times)
    ft = food_times

    if sum(ft) <= k:
        return -1

    while k > 0:

        dvd = k // fc
        ft = list(map(lambda x: x - dvd, ft))
        k - dvd * fc

        mn = min(ft)

        if k > mn * fc:
            ft = list(map(lambda x: x - mn, ft))
            k -= mn * fc
            for _ in range(ft.count(0)):
                ft.pop(ft.index(0))

        elif k == mn * fc:
            ft = list(map(lambda x: x - mn, ft))
            k -= mn * fc
            for _ in range(ft.count(0)):
                ft.pop(ft.index(0))
            return 1

        else:
            break

    j = 0
    while k != -2:
        if ft[j]:
            ft[j] -= 1
            k -= 1
            if k == -1:
                return j + 1
            j = (j + 1) % len(ft)
        else:
            j = (j + 1) % len(ft)


    # i = 0
    # while i < k:
    #     if food_times[i % fd_cnt]:
    #         food_times[i % fd_cnt] -= 1
    #         i += 1
    #     else:
    #         if stop - k > fd_cnt:
    #             return -1
    #         i += 1
    #         stop += 1
    # answer = (i + 1) % k
    # return answer
print(solution(food_times, k))
