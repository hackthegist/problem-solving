n, sprints = 10, [1,5,10,3]
n1, sprints1 = 5, [1, 5]

def getMostVisited(n, sprints):
    len_sprints = len(sprints) - 1
    to_accumulate = [0] * (n+2)

    for i in range(len_sprints):
        if sprints[i] < sprints[i+1]:
            start, end = sprints[i], sprints[i+1]
        else:
            start, end = sprints[i+1], sprints[i]
        to_accumulate[start] += 1
        to_accumulate[end+1] -= 1

    visited = [0] * (n+1)
    inc = 0
    for i in range(len(visited)):
        inc += to_accumulate[i]
        visited[i] = inc

    return visited.index(max(visited))

print(getMostVisited(n, sprints))

# def getMostVisited(n, sprints):
#     visited = [0] * (n + 1)
#     i = 0
#     while i < len(sprints) - 1:
#         double = []
#         start = sprints[i]
#         if sprints[i] < sprints[i+1]:
#             while i < len(sprints) - 1 and sprints[i] < sprints[i+1]:
#                 double.append(sprints[i+1])
#                 i += 1   
#             end = sprints[i]
#         else:
#             while i < len(sprints) - 1 and sprints[i] > sprints[i+1]:
#                 double.append(sprints[i+1])
#                 i += 1
#             end = sprints[i]
#         double.pop() 

#         if start < end:
#             for j in range(start, end+1):
#                 visited[j] += 1
#         else:
#             for j in range(start, end-1, -1):
#                 visited[j] += 1
#         for d in double:
#             visited[d] += 1
    
#     max_value = max(visited)
#     return visited.index(max_value)




# def getMostVisited(n, sprints):
#     visited = [0] * (n + 1)
#     for i in range(len(sprints)-1):
#         start, end = sprints[i], sprints[i+1]
#         if start < end:
#             for j in range(start, end+1):
#                 visited[j] += 1
#         else:
#             for j in range(start, end-1, -1):
#                 visited[j] += 1
    
#     max_value = max(visited)
#     return visited.index(max_value)

# def getMostVisited(n, sprints):
#     len_sprints = len(sprints) - 1
#     visited = [[0] * (n + 1) for _ in range(len_sprints)]

#     for i in range(len_sprints):
#         if sprints[i] < sprints[i+1]:
#             start, end = sprints[i], sprints[i+1]
#         else:
#             start, end = sprints[i+1], sprints[i]

#         visited[i][start:end+1] = [1] * (end - start + 1)
    
#     ans, ans_idx = 0, 0
#     for j in range(n):
#         sum_ = sum([visited[i][j] for i in range(len_sprints)])
#         if ans < sum_:
#             ans = sum_
#             ans_idx = j

#     return ans_idx

# def getMostVisited(n, sprints):
#     len_sprints = len(sprints) - 1
#     visited = [[0] * (n+1) for _ in range(n+1)]

#     for i in range(len_sprints):
#         if sprints[i] < sprints[i+1]:
#             start, end = sprints[i], sprints[i+1]
#         else:
#             start, end = sprints[i+1], sprints[i]
#         visited[start][end] += 1

#     ans_arr = [0] * (n+1)
#     for m in range(1, n+1):
#         for i in range(1, m+1):
#             for j in range(m, n+1):
#                 ans_arr[m] += visited[i][j]

#     return ans_arr.index(max(ans_arr))

# def getMostVisited(n, sprints):
#     len_sprints = len(sprints) - 1
#     ans_arr = [0] * (n+1)

#     for i in range(len_sprints):
#         if sprints[i] < sprints[i+1]:
#             start, end = sprints[i], sprints[i+1]
#         else:
#             start, end = sprints[i+1], sprints[i]
#         ans_arr[start:end+1] = [v+1 for v in ans_arr[start:end+1]]

#     return ans_arr.index(max(ans_arr))