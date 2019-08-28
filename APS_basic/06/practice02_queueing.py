q = []
mzz = 20
mzz_list = [1] * 20

for i in range(20):
    q.append(i)
    pop_ = q.pop(0)
    mzz -= mzz_list[i]
    mzz_list[i] += 1
    q.append(pop_)
    # print("==> {}번 학생: 입장하여 줄을 선다.".format(i))
    # print("{}번 학생이 {}개를 받았다.".format(pop_, mzz_list[i]))
    # input("다음 단계를 진행합니다...")
