import random


def get_abs(num):
    num = num if num >= 0 else -num
    return num


numbers = list(range(1, 26))
random.shuffle(numbers)
num_mat = [numbers[i:i+5] for i in range(0, len(numbers), 5)]

print(num_mat)
