n = int(input())
seats = list(map(int, input().strip().split(' ')))
max_zeros = 0
zeros = 0

for i in range(n):
    if not seats[i]:
        zeros += 1
    else:
        zeros = 0
    max_zeros = zeros if zeros > max_zeros else max_zeros

if max_zeros % 2 == 1:
    print(max_zeros//2 + 1)
else:
    print(max_zeros//2)