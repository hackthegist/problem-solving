

# # 2
# def solution(n):
#     length = 2**n
#     answer = [] 

#     for i in range(0, n):
#         answer.append(0)

#         if i > 0:
#             for j in range(2**i-2,-1,-1):
#                 if answer[j]:
#                     answer.append(0)
#                 else:

#                     answer.append(1)
#     return answer
    w = 8
    h = 12
        
    
    if w == h:
        useless = w
    else:
        lcm = 1
        if w < h:
            for i in range(1, w+1):
                if w % i == 0 and h % i == 0:
                    if lcm < i:
                        lcm = i
            useless = ((w // lcm) - 1) * ((h // lcm) - 1) * (w // lcm)
            
        else:
            for i in range(1, h+1):
                if w % i == 0 and h % i == 0:
                    if lcm < i:
                        lcm = i
            useless = ((w // lcm) - 1) * ((h // lcm) - 1) * (h // lcm)
        
    
    answer = (w * h) - useless