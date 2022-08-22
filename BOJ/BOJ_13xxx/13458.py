# a = int(input())
# student = list(map(int, input().split()))
# b, c = map(int, input().split())
# cnt = a
# for i in range(a):
#     # 총감독관 배치
#     student[i] -= b
#     if student[i] < 0:
#         student[i] = 0
#
#     # 부감독관 배치
#     if student[i] % c != 0:
#         cnt += student[i] // c + 1
#     else:
#         cnt += student[i] // c
# print(cnt)

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

b,c = map(int, input().split())

cnt = n # 총감독관은 한명씩 배치

for i in range(n):
    a[i] -= b
    if a[i] > 0 and a[i] % c == 0:
        cnt += a[i] // c
    if a[i] > 0 and a[i] % c != 0:
        cnt += a[i] // c + 1
print(cnt)
