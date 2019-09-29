import sys
sys.stdin = open("Programmers/2019_라인_코딩테스트/06.txt", "r")

n, method = input().strip().split(' ')
nums = [list(input().strip().split(' ')) for _ in range(int(n))]

y = 0
for num in nums:
    y = int(num[0]) if int(num[0]) > y else y
    num[1] = list(map(int, list(num[1])))

def draw(size, max_y, num):
    x, y = size, (2*size) - 1
    res = [0] * max_y
    row = [0] * x

    if num == 1:
        for i in range(y):
            for j in range(x):
                if j == x-1:
                    row[j] = '#'
                else:
                    row[j] = '.'
            res[i] = ''.join(row)
            
    return res

print(draw(5, 9, 1))




# for i in range(n):
#     size, nums = map(int, input().strip().split(' '))
#     nums = list(nums)

# print(a + b)