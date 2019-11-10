def solution(board, moves):
    length = len(board)
    # rotated_board = [[board[x][y] for x in range(length)] for y in range(length-1, -1, -1)]
    # print(rotated_board)
    stack = []
    answer = 0

    for move in moves:
        for x in range(length):
            if board[x][move-1]:
                if stack and stack[-1] == board[x][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[x][move-1])
                    
                board[x][move-1] = 0
                break
    
    
    return answer

s = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(s)