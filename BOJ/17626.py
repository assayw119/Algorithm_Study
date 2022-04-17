import math
from itertools import combinations
from itertools import product

# n = int(input())
# num_list = [True for i in range(int(math.sqrt(n)))]
# sqrt_list = [i*i for i in range(int(math.sqrt(n)),0,-1)]

def test(a):
    for i in range(a):
        if a-i in sqrt_list:
            test(i)
print(test(n))

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
