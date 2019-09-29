bishops = ["D5", "E8", "G2"]

def solution(bishops):
    board = [[1] * 8 for _ in range(8)]
    move = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for b in bishops:
        bx, by = 8 - int(b[1]), ord(b[0]) - ord('A'), 
        board[bx][by] = 0
        
        for i, j in move:
            x, y = bx, by
            while 0 <= x < 8 and 0 <= y < 8:
                x += i
                y += j
                print(x, y)
                if not 0 <= x < 8:
                    break 
                if not 0 <= y < 8:
                    break
                board[x][y] = 0
    answer = sum([sum(board[i]) for i in range(8)])
    # for k in range(8):
    #     for l in range(8):
    #         answer += board[k][l]
    return answer

print(solution(bishops))