'''
(2018년) KAKAO BLIND RECRUITMENT    길 찾기 게임

입출력 예

nodeinfo	
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	

result
[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
'''
import operator

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

def solution(nodeinfo):
    answer = [[]]
    ni = sorted(nodeinfo, key=operator.itemgetter(1, 0), reverse=True)
    print(ni)

    return answer

solution(nodeinfo)