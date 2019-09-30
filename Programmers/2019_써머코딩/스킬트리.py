skill, skill_trees = 'CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']

def solution(skill, skill_trees):
    i = -1
    answer = 0
    
    for skt in skill_trees:
        for sk in skt:
            if sk == skill[i+1]:
                i += 1
        if i == len(skill) - 1:
            answer += 1 
        i = -1
    
    return answer

print(solution(skill, skill_trees))