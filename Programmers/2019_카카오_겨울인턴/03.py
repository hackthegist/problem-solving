import re
from math import factorial

def solution(user_id, banned_id):
    answer = 1
    dict_b_id = {}
    for b_id in banned_id:
        if b_id in dict_b_id.keys():
            dict_b_id[b_id] += 1
        else:
            dict_b_id[b_id] = 1
    print(dict_b_id)
    for b_id in dict_b_id.keys():
        pattern = b_id.replace("*", ".")
        p_com = re.compile("^" + pattern + "$")

        match_id_cnt = 0
        pop_1 = 0
        pop_idx = None
        for u_id in user_id:
            if p_com.match(u_id):
                if not pop_1:
                    pop_idx = user_id.index(u_id)
                    pop_1 = 1

                match_id_cnt += 1

        answer *= factorial(match_id_cnt) // (factorial(dict_b_id[b_id]) * factorial(match_id_cnt - dict_b_id[b_id]))
        print(b_id, answer)
        if pop_1:
            user_id.pop(pop_idx)
    
    return answer

s1 = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
s2 = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
s3 = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(s3)

import re

# def solution(user_id, banned_id):
#     answer = 1

#     for b_id in banned_id:
#         pattern = b_id.replace("*", ".")
#         p_com = re.compile("^" + pattern + "$")

#         match_id_cnt = 0
#         for u_id in user_id:
#             if p_com.match(u_id):
#                 match_id_cnt += 1

#         answer *= match_id_cnt
    
#     return answer