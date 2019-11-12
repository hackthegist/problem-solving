def solution(stones, k):
    for i in range(k+1):
        cnt = 0
        for stone in stones:
            if stone <= i:
                cnt += 1
                print(cnt)
                if cnt == k:
                    answer = i
                    break

            else:
                cnt = 0
        
    
    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)