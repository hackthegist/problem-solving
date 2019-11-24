k0, marks0  = 4, [20, 40, 60, 80, 100, 100] 
k1, marks1 = 4, [2,2,3,4,5]
k2, marks2 = 1, [0]

def numofPrizes(k, marks):
    sorted_marks = sorted(marks, reverse=True)

    zero_idx = -1 
    for i in range(len(sorted_marks)-1, -1, -1):
        if not sorted_marks[i]:
            zero_idx = i
        else:
            break
    if zero_idx >= 0:
        sorted_marks = sorted_marks[:zero_idx]
    
    if not sorted_marks:
        return 0

    r, ranks = 1, [1]
    for i in range(1, len(sorted_marks)):
        r += 1
        if sorted_marks[i-1] == sorted_marks[i]:
            ranks.append(ranks[-1])
        else:
            ranks.append(r)
        

   
    for i in range(len(sorted_marks)):
        if ranks[i] > k:
            ans = i
            break
    else:
        ans = i + 1

    return ans

print(numofPrizes(k0, marks0))