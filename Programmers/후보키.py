'''
(2018년)KAKAO BLIND RECRUITMENT 후보키

relation	                        result
[["100","ryan","music","2"],
 ["200","apeach","math","2"],
 ["300","tube","computer","3"],
 ["400","con","computer","4"],
 ["500","muzi","music","3"],
 ["600","apeach","music","2"]]	        2
'''

relation = [["100","ryan","music","2"],
 ["200","apeach","math","2"],
 ["300","tube","computer","3"],
 ["400","con","computer","4"],
 ["500","muzi","music","3"],
 ["600","apeach","music","2"]]

def solution(relation):
    answer = 0
    attr_cnt = len(relation[0])
    cardi = len(relation)
    rt_rel = [[relation[j][i] for j in range(cardi)] for i in range(attr_cnt)]
    to_pop = []

    for k in range(len(rt_rel)):
        if len(set(rt_rel[k])) == cardi:
            answer += 1
            to_pop.append(k)
    for elem in to_pop:
        rt_rel.pop(elem)
    
    print(rt_rel)
    return answer

solution(relation)