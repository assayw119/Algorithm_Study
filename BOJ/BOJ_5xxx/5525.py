# n = int(input())
# m = int(input())
# s = list(input())
#
# k = 2*n+1
# result = 0
# def check(x):
#     global s, n, result, k
#
#     # print(s[x:x+k], x)
#     if s[x:x+k] == ['I'] + ['O', 'I']*n:
#         result += 1
#
# for i in range(m-k):
#     check(i)
# print(result)

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

k = 2*n+1
result = 0
num = 0
ioi_count = 0
while 1:
    if s[num:num+3] == 'IOI':
        num += 2
        ioi_count += 1
        if ioi_count == n:
            result += 1
            ioi_count -= 1
    else:
        num += 1
        ioi_count = 0
    if num >= m-1:
        break
print(result)