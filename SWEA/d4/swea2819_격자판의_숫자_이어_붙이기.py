'''
2819. 격자판의 숫자 이어 붙이기
'''

import sys
sys.stdin = open("SWEA/inputs/2819_in.txt", "r")

def turn(arr):
    return [[arr[j][i] for j in range(3, -1, -1)] for i in range(4)]

ans = ''
for tc in range(1, int(input())+1):
    
    nums = [[*map(int, input().split())] for _ in range(4)]
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = set()
    
    for _ in range(4):
        data = [[0,0], [0,1], [0,2], [1,2]]
        [d.append(str(nums[d[0]][d[1]])) for d in data]
        for _ in range(6):
            data_n = len(data)
            for k in range(data_n):
                for i, j in moves:
                    x, y = data[k][0], data[k][1] 
                    x += i
                    y += j
                    if not 0 <= x < 4:
                        continue
                    if not 0 <= y < 4:
                        continue
                    data.append([x, y, data[k][2] + str(nums[x][y])])

            data = data[data_n:]
        res.update({d[2] for d in data})
        nums = turn(nums)
    
    ans += "#{} {}\n".format(tc, len(res))

print(ans)