import math
from itertools import combinations
from itertools import product

n = int(input())
num_list = [True for i in range(int(math.sqrt(n)))]
sqrt_list = [i*i for i in range(int(math.sqrt(n)),0,-1)]

# def test(a):
#     s = int(math.sqrt(a))
#     sqrt_list = [i * i for i in range(s, 0, -1)]
#
#     for i in range(a,0,-1):
#         # if i in sqrt_list:
#         #     new_a = a - i
#         #     test(new_a)
#         #     return new_a
#         count = 0
#         count_lst = []
#         for j in range(0,a+1):
#             if a-j in sqrt_list:
#                 new_a = a - (i - j)
#                 print(new_a)
#                 count += 1
#                 test(new_a)
#             count_lst.append(count)
#             return count_lst
# print(test(n))


dp = [int(1e9)] * (n+1)






# result = []
# for a in sqrt_list:
#     for b in sqrt_list:
#         for c in sqrt_list:
#             for d in sqrt_list:
#                 if a+b+c+d == n:
#                     lst = [a,b,c,d]
#                     length = len(lst) - lst.count(0)
#                     result.append(length)
# print(min(result))
