drum = ["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
drum2 = ["**","**"]

def solution(drum):
    n = len(drum)
    answer = 0
    ht = {
        '#': (1, 0),
        '>': (0, 1),
        '<': (0, -1),
        '*': (1, 0),
    }

    for y in range(n):
        x = 0
        star = 0
        while x < n:
            dx, dy = ht[drum[x][y]]
            if drum[x][y] == '*':
                star += 1
            if star == 2:
                break
            x += dx
            y += dy
            if x >= n:
                answer += 1
                break
            if not 0 <= x < n:
                break
            if not 0 <= y < n:
                break
            

    return answer
print(solution(drum2))
