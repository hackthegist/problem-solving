import random

numbers = list(range(1, 26))
random.shuffle(numbers)
num_mat = [numbers[i:i+5] for i in range(0, len(numbers), 5)]

print(num_mat)


for h in range(5):
    for l in range(5):
        mn_x, mn_y = h, l
        for j in range(h, 5):
            for k in range(l, 5):
                if num_mat[j][k] < num_mat[mn_x][mn_y]:
                    mn_x, mn_y, j, k = j, k, mn_x, mn_y
        num_mat[mn_x][mn_y], num_mat[j][k] = num_mat[j][k], num_mat[mn_x][mn_y]

print(num_mat)
