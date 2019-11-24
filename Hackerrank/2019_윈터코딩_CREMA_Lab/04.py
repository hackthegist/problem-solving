from collections import Counter
from array import array

requestTime1 = [1,1,1,1,2,2,2,3,4,4,4,8,8,8]
requestTime2 = [1,1,1,1,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12,13,13,13,13,14,14,14,14,14,16,16,16,16,16,16,17,17,17,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,20,20,20,20,20]

# def droppedRequests(requestTime):
#     dict_times = dict(Counter(requestTime))
#     list_times = (k for k in dict_times.keys())
    
#     dropped = 0
#     ten_sec = one_min = 0
#     for t in list_times:
#         to_drop = []
#         acc = dict_times[t]

#         one_sec = acc - acc_list_times[t-1]
#         if one_sec > 3:
#             to_drop.append(one_sec - 3)

#         if i > 10:
#             ten_sec += acc - acc_list_times[t-10]
#         else: 
#             ten_sec += acc
#         if ten_sec > 20:
#             to_drop.append(min(ten_sec - 20, one_sec))

#         if i > 60:
#             one_min += acc - acc_list_times[t-60]
#         else:
#             one_min += acc
#         if one_min > 60:
#             to_drop.append(min(one_min - 60, one_sec))

#         if to_drop:
#             dropped += max(to_drop)
    
#     return dropped

def droppedRequests(requestTime):
    dict_times = dict(Counter(requestTime))
    keys = dict_times.keys()
    acc_list_times = [0] * (requestTime[-1]+1)
    for i in range(len(acc_list_times)):
        if i in keys:
            acc_list_times[i] = acc_list_times[i-1] + dict_times[i]
        else:
            acc_list_times[i] = acc_list_times[i-1] 
    
    dropped = 0
    for i in range(1, len(acc_list_times)):
        to_drop = []
        acc = acc_list_times[i]

        one_sec = acc - acc_list_times[i-1]
        if one_sec > 3:
            to_drop.append(one_sec - 3)

        if i > 10:
            ten_sec = acc - acc_list_times[i-10]
        else: 
            ten_sec = acc
        if ten_sec > 20:
            to_drop.append(min(ten_sec - 20, one_sec))

        if i > 60:
            one_min = acc - acc_list_times[i-60]
        else:
            one_min = acc
        if one_min > 60:
            to_drop.append(min(one_min - 60, one_sec))

        if to_drop:
            dropped += max(to_drop)
    
    return dropped

print(droppedRequests(requestTime2))


# def droppedRequests1(requestTime):
#     times = dict(Counter(requestTime))
#     time_keys = tuple(times.keys())
#     time_values = tuple(times.values())

#     at_once = 0
#     ten_sec = 0
#     one_min = 0
#     dropped = 0

    
#     for i in range(len(time_keys)):
#         to_drop = []
#         t = time_keys[i]
#         if times[t] > 3:
#             to_drop.append(times[t] - 3)

#         ten_sec += times[t]
#         if t > 11:
#             if t-10 in time_keys:
#                 ten_sec -= times[t-10]
#         if ten_sec > 20:
#             # dropped += ten_sec - 20
#             to_drop.append(min(ten_sec - 20, times[t]))

#         one_min += times[t]
#         if t > 60:
#             if t-60 in time_keys:
#                 one_min -= times[t-60]
#         if one_min > 60:
#             # dropped += ten_sec - 60
#             to_drop.append(min(one_min - 60, times[t]))
#         if to_drop:
#             dropped += max(to_drop)
         
#     return dropped



# def droppedRequests(requestTime):
#     times = dict(Counter(requestTime))
#     dropped = 0
#     time_keys = times.keys()
#     time_values = times.values()
    
#     for t in time_values:
#         if t > 3:
#             dropped += t - 3
#     acc = 0
#     for i in range(len(time_keys)):
#         acc += 

#     return time_keys