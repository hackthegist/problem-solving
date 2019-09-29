import sys
sys.stdin = open("Programmers/2019_라인_코딩테스트/01.txt", "r")

m, c = map(int, input().strip().split(' '))
msgs = [int(input()) for _ in range(m)]
processing = [0] * c
sec = 0

while msgs or sum(processing) > 0:
    if msgs:
        for i in range(c):
            if processing[i] == 0:
                processing[i] = msgs.pop(0)
            if not msgs:
                break
        
    for j in range(c):
        if processing[j]:
            processing[j] -= 1
    sec += 1

print(sec)