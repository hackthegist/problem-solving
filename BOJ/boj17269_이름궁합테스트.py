'''
University > 인하대학교 > 2019 인하대학교 프로그래밍 경진대회(IUPC) G번
17269. 이름궁합테스트
'''

import sys
sys.stdin = open("BOJ/inputs/17269_in.txt", "r")

ans = ""
for i in range(1, int(input())+1):
    N, M = map(int, input().split())
    table = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    print(ord('A')) # 65
    
    A, B = input().split()
    A = [table[ord(a)-65] for a in A]
    B = [table[ord(b)-65] for b in B]
    len_A, len_B = len(A), len(B)
    merged = []
    if len_A < len_B:
        for i in range(len_A):
            merged.append(A[i])
            merged.append(B[i])
        merged += B[len_A:]
    else:
        for i in range(len_B):
            merged.append(A[i])
            merged.append(B[i])
        merged += A[len_B:]
    new_merged = []
    while len(merged) > 1:
        new_merged.append


    # ans += "#{} {}\n".format(i, result)

print(ans)