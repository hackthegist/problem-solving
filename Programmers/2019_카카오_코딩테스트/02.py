
def is_balanced(p):
    lcnt = 0
    rcnt = 0
    for ch in p:
        if ch == "(":
            lcnt += 1
        else:
            rcnt += 1
    return lcnt == rcnt


def is_correct(p):
    stack = []
    for ch in p:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False
    if stack:
        return False
    else:
        return True


def solution(p):
    answer = ""
    if not p:
        return ""
    else:
        idx = 0
        u = p[idx]
        while not is_balanced(first):
            idx += 1
            u = p[:idx+1]
            v = p[idz+1:]

        if is_correct(u):
            # v로 위 단계 반복
        else:

    return answer


print(is_correct("()()()()"))
print(is_correct("(()(()()))"))
