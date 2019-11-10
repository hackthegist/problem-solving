
def solution(s):
    dict_s = {}
    q = ""

    for ch in s:
        if ch.isdigit():
            q += ch
        else:
            if q:
                num = int(q)
                q = ""
                if num in dict_s.keys():
                    dict_s[num] += 1
                else:
                    dict_s[num] = 1

    answer = sorted(dict_s, key=lambda x: dict_s[x], reverse=True)
    return answer


s1 = solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
s2 = solution("{{20,111},{111}}")
print(s2)