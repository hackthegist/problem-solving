'''
5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기
'''

import sys
sys.stdin = open("SWEA/inputs/5110_in.txt", "r")

class Node:
    def __init__(self, l_link, data, r_link):
        self.data = data
        self.l_link = l_link
        self.r_link = r_link

    def init_list(list_):
        for i in range(len(list_)):
            if i == 0:
                head = Node(None, list_[i], None)
            else:
                head.append(list_[i])
        return head


    def append(head, data):
        if head == None:
            head = Node(None, data, None)
        else:
            p = head
            while p.r_link != None:
                p = p.r_link
            p.r_link = Node(p, data, None)

    def insert_nodes(head1, head2):
        
        p1 = head1
        while p1.data <= head2.data:
            if not p1.r_link:
                break
            p1 = p1.r_link 
        
        p2 = head2 
        while p2.r_link != None:
            p2 = p2.r_link
        
        if p1 == head1:
            p1.l_link = p2
            p2.r_link = p1
        else:

            if p1.data <= head2.data:
                p1.r_link = head2
                head2.l_link = p1
        
            else:
                p1.l_link.r_link = head2
                head2.l_link = p1.l_link
                p1.l_link = p2
                p2.r_link = p1


        return head1
          
t = int(input())
ans = ""

for tc in range(1, t+1):
    n, m = map(int, input().split())

    list1 = list(map(int, input().split()))
    head1 = Node.init_list(list1)
    
    for _ in range(m-1):
        list2 = list(map(int, input().split()))
        head2 = Node.init_list(list2)
        head1 = Node.insert_nodes(head1, head2)
        
    p = head1
    while p.r_link != None:
        print(p.data)
        p = p.r_link
        
        
        
    # for _ in range(10):
    #     res += str(stack.pop()) + " "
    
    # ans += "#{} {}\n".format(tc, res)

print(ans)