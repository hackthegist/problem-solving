
def count_sum_is_zeros(arr):
    n = len(arr)
    new = []
    list_of_new = []

    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                new.append(arr[j])

        if new and sum(new) == 0:
            list_of_new.append(new)
        new = []

    result = [list(i) for i in set(tuple(i) for i in list_of_new)]
    print(result)


numbers = [int(input("정수를 입력하세요: ")) for i in range(4)]
count_sum_is_zeros(numbers)
