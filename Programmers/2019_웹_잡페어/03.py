sticker = [12, 12, 12, 12, 80, 14, 22, 100, 12, 12]

def solution(sticker):
    sticker = [0] + sticker + [0]
    answer = 0

    while sum(sticker):
        mx = sticker.index(max(sticker))
        if sticker[mx] >= sticker[mx-1] + sticker[mx+1]:
            answer += sticker[mx]
            sticker[mx-1:mx+2] = [0, 0, 0]
            
        else:
            sticker[mx] = 0

    
    return answer

print(solution(sticker))

 

def solution2(sticker):
    res = 0

    def go(i, s):
        global res

        if i < len(sticker):
            res = s if s > res else res
            return
        if i:
            go(i+2, s+sticker[i])
            go(i+3, s+sticker[i+1])  

    go(0, 0)

    return res

print(solution2(sticker))