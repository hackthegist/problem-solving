def solution(n, lost, reserve):
    lost_and_reserve = set(lost) & set(reserve)
    for s in lost_and_reserve:
        lost.pop(lost.index(s))
        reserve.pop(reserve.index(s))
    rest = n - len(lost)
    
    lost = sorted(lost)
    reserve = sorted(reserve)
    l = r = 0
    while l < len(lost) and r < len(reserve):
        if abs(lost[l] - reserve[r]) == 1:
            l += 1
            r += 1
        elif l < r:
            l += 1
        elif r < l:
            r += 1
    if l == r:
        borrow = l
    elif l > r:
    answer = rest + 
    return answer