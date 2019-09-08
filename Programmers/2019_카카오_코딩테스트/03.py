import copy


def rotate(key, m):
    return [[key[j][i] for j in range(m-1, -1, -1)] for i in range(m)]


def is_fit(b, mn, mx, n):
    for i in range(mn, mx):
        for j in range(mn, mx):
            if b[i][j] == 0:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    board_len = (m * 2 + n - 2)
    n_0 = m-1
    n_m = n_0 + n

    board = [[0] * board_len for _ in range(board_len)]

    for i in range(n_0, n_m):
        for j in range(n_0, n_m):
            board[i][j] = lock[i-n_0][j-n_0]

    for k in range(0, n_m):
        for l in range(0, n_m):
            for _ in range(4):
                test = copy.deepcopy(board)
                for q in range(k, k+m):
                    for r in range(l, l+m):
                        if n_0 <= q < n_m and n_0 <= r < n_m:
                            if test[q][r] == 0:
                                test[q][r] = key[q-k][r-l]
                            else:
                                test[q][r] = 0 if key[q-k][r-l] == 1 else 1

                if is_fit(test, n_0, n_m, n):
                    return True
                key = rotate(key, m)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
# print(rotate(key, len(lock)))
