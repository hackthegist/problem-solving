import sys
sys.stdin = open('SWEA/inputs/5648_in.txt', 'r')

T = int(input())

def move(arr):
    if arr[2] == 0:
        arr[1] += 0.5
    elif arr[2] == 1:
        arr[1] -= 0.5
    elif arr[2] == 2:
        arr[0] -= 0.5
    else:
        arr[0] += 0.5

for tc in range(1, T + 1):
    n = int(input())
    elems = [list(map(int, input().split())) for _ in range(n)]
    gone = [1] * n
    energy = 0

    for i in range(2000):
        for l in range(n):
            if gone[l]:
                move(elems[l])
        for j in range(n-1):
            same = []
            if gone[j]:
                for k in range(j+1, n):
                    if gone[k]:
                        if elems[j][0] == elems[k][0] and elems[j][1] == elems[k][1]:
                            same.append(j)
                            same.append(k)
                same = set(same)
                for m in same:
                    energy += elems[m][3]
                    gone[m] = 0




    print("#{} {}".format(tc, energy))
