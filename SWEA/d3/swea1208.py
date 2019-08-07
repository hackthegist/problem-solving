'''
[S/W 문제해결 기본] 1일차 - Flatten
'''

# 1. from scratch


def get_min_max_idx(li):
    mn = mx = li[0]
    idx_mn = idx_mx = 0
    for idx, value in enumerate(li):
        if value < mn:
            mn = value
            idx_mn = idx
        if value > mx:
            mx = value
            idx_mx = idx
    return idx_mn, idx_mx


for i in range(10):
    dump_c = int(input())
    nums = list(map(int, input().split()))

    i_mn, i_mx = get_min_max_idx(nums)
    gap = nums[i_mx] - nums[i_mn]

    for _ in range(dump_c):
        if not gap <= 1:
            nums[i_mn] += 1
            nums[i_mx] -= 1
            i_mn, i_mx = get_min_max_idx(nums)
            gap = nums[i_mx] - nums[i_mn]
        else:
            result = gap
            break

    print("#{} {}".format(i+1, gap))


# use counting list


# use sort()
for i in range(10):
    dump_c = int(input())
    nums = list(map(int, input().split()))

    for _ in range(dump_c):
        nums.sort()
        nums[0] += 1
        nums[-1] -= 1
        nums.sort()
        gap = nums[-1] - nums[0]
        if gap <= 1:
            gap = 0
            break

    print("#{} {}".format(i+1, gap))
