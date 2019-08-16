'''
4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

보이어-무어 알고리즘 사용
1. 두 문자열을 정렬한 후 짧은 문자열의 뒤에서부터 비교
2. 짧은 문자열과 모두 일치하면 1을 출력
3. 다른 문자가 있다면 해당 문자가 짧은 문자열에 존재하는지 조사
4.   존재한다면 같은 문자를 기준으로 두 문자열을 정렬 -> 1
5.   없다면 짧은 문자열의 길이만큼 오른쪽으로 이동하여 두 문자열 정렬 -> 1
'''

import sys
sys.stdin = open("SWEA/inputs/4864_in.txt", "r")

t = int(input())
for i in range(t):
    short = input()
    long = input()
    ln_s, ln_l = len(short), len(long)
    cnt = 0

    while cnt < ln_l - ln_s + 1:
        for j in range(ln_s):
            ri = ln_s-1 - j
            if long[cnt+ri] != short[ri]:
                break
        else:
            result = 1
            break

        for k in range(len(short[:ri])):
            if short[ri-1-k] == long[cnt+ri]:
                cnt += k+1
                break
        else:
            cnt += ri+1

        result = 0

    print("#{} {}".format(i+1, result))
