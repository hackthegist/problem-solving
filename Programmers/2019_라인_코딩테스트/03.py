import sys
sys.stdin = open("Programmers/2019_라인_코딩테스트/03.txt", "r")

n = int(input())
peoples = [list(map(int, input().strip().split(' '))) for _ in range(n)]
peoples = sorted(peoples, key=lambda x: x[0])
bathrooms = []

min_time = peoples[0][0]
for p in peoples:
    if p[0] == min_time:
        bathrooms.append(p)
        continue
    
    for b in range(len(bathrooms)):
        if bathrooms[b][1] > p[0]:
            if b == len(bathrooms) - 1:
                bathrooms.append(p)
        else:
            bathrooms[b] = p
            break
print(len(bathrooms))