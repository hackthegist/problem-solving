import re


def solution(words, queries):
    answer = []
    q_dict = {}

    for q in queries:
        if q in q_dict.keys():
            cnt = q_dict[q]
        else:
            qr = q.replace("?", "\w")
            key = "^" + qr + "$"

            cnt = 0
            regex = re.compile(key)
            for w in words:
                mo = regex.match(w)
                if mo:
                    cnt += 1
            q_dict[q] = cnt

        answer.append(cnt)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
