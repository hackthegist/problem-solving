'''
Power set 구하기

타겟: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a: 논리 리스트
k: 탐색 단계 
inp: Power set의 원소 개수
'''


def backtrack(a, k, inp):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == inp:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, inp, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, inp)


def process_solution(a, k):
    tg = list(range(12))
    res = []

    for i in range(1, 11):
        if a[i]:
            res.append(tg[i])
    if sum(res) == 10:
        print(res)


def construct_candidates(a, k, inp, c):
    c[0] = True
    c[1] = False
    return 2


MAXCANDIDATES = 100
NMAX = 11
a = [0] * NMAX
backtrack(a, 0, 10)
