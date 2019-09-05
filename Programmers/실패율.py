'''
(2018년)KAKAO BLIND RECRUITMENT 실패율

N   Stages                      Output
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]
'''


N = 4
stages = [4,4,4,4,4]

def solution(N, stages):
    stage_users = {}
    players = len(stages)
    
    for stage in range(1, N+1):
        stucks = stages.count(stage)
        stage_users[stage] = stucks / players if stucks != 0 else 0
        players -= stucks
            
    sorted_list = sorted(stage_users.items(), key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in sorted_list]
      
    return answer

print(solution(N, stages))

