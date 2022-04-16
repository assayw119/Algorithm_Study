import math

n = int(input())

# def test(n):
#
#     sqrt_num = int(math.sqrt(n))
#     print(sqrt_num, '*'*20)
#     count = 0
#     dic = {}
#     for i in range(sqrt_num,0,-1):
#         rest_num = n - i*i
#         count += 1
#
#         if rest_num == 0:
#             break
#
#
#         test(rest_num)
#     print()
#
# print(test(n))

num_list = [True for i in range(int(math.sqrt(n)))]
sqrt_list = [i*i for i in range(int(math.sqrt(n)),0,-1)]

# for i in range(1, n+1):
#     s = []
#     for j in sqrt_list:
#         if j > i:
#             break
#         s.append(num_list[i-j])
#     print(s)
#     num_list[i] = min(s) + 1
# # print(num_list)

total = 0
lst = []
for idx, i in enumerate(sqrt_list):
    if num_list[idx] == False:
        continue
    if total + i > n:
        continue
    else:
        total += i
        lst.append(i)
        num_list[idx] = False
        if total == n:
            break
    print(num_list)
print(lst)

if sum(lst) == n:
    print(len(lst))
else:
    print(len(lst) + n - sum(lst))