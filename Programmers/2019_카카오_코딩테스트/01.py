

def make_zip(s, l):
    li = []
    idx = 0

    while len(s) > 0:
        if len(s) >= l:
            first = s[:l]
            s = s[l:]
        else:
            first = s
            s = []

        if not li:
            li.append([first, 1])
        else:
            if li[idx][0] == first:
                li[idx][1] += 1
            else:
                li.append([first, 1])
                idx += 1

    result = ""
    for wc in li:
        result += str(wc[1]) + wc[0]
    return result.replace("1", "")


def solution(s):
    max_len = len(s)
    answer = max_len

    for i in range(1, max_len):
        s_len = len(make_zip(s, i))
        answer = s_len if answer > s_len else answer

    return answer


s_li = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede",
        "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for s in s_li:
    print(solution(s))
