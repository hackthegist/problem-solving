# def solution(k, room_number):

#     answer = []
#     min_availables = [1]

#     for want_rn in room_number:
#         if want_rn <= min_availables[0]:
#             rn = min_availables[0]
#             min_availables[0] += 1
#             if len(min_availables) != 1:
#                 min_availables.pop(0)
#         else:
#             if len(min_availables) == 1:
#                 rn = want_rn
#                 min_availables.append(want_rn + 1)
#             else:

#                 for i in range(1, len(min_availables)):
#                     if want_rn <= min_availables[i]:
#                         rn = min_availables[i]
#                         min_availables[i] += 1
#                         if i < len(min_availables) - 2 and min_availables[i] == min_availables[i+1]:
#                             min_availables.pop(i)
#                         break
#         answer.append(rn)
#     return answer




def solution(k, room_number):

    answer = []
    availables = [1] * (k+1)
    min_available = 1

    for want_rn in room_number:
        for rn in range(max(min_available, want_rn), k+1):
            if availables[rn]:
                answer.append(rn)
                availables[rn] = 0
                if min_available == rn:
                    min_available = availables.index(1)
                break


    return answer

s1 = solution(10, [1,3,4,1,3,1])
print(s1)


# answer = []
#     availables = [1] * (k+1)
#     min_available = [1]

#     for want_rn in room_number:
#         for rn in range(max(min_available[0], want_rn), k+1):
#             if availables[rn]:
#                 answer.append(rn)
#                 availables[rn] = 0
#                 if rn in min_available:
#                     if rn == min_available[-1]:
#                         min_available[-1] += 1
#                     else:
#                         min_available.pop(min_available.index(rn))
#                 else:
#                     min_available.append(rn+1)
#                 break

#     return answer