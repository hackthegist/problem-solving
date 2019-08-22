edges = [1, 2, 2, 4, 2, 5, 4, 3, 2, 3, 3, 6]
adj_t = [[0] * 7 for _ in range(7)]

for i in range(0, len(edges), 2):
    adj_t[edges[i]][edges[i+1]] += 1

# 1 repetative method


def my_dfs(node):
    visited = [0] * 7
    stack = []
    visited[node] += 1
    print(node)

    while 0 in visited[1:]:
        for i in range(1, 7):
            if adj_t[node][i] and not visited[i]:
                stack.append(node)
                node = i
                visited[node] += 1
                print(node)
                break
        else:
            node = stack.pop()

    print("well exploered!")


my_dfs(1)
