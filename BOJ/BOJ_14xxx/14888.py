import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
plus, minus, multi, divi = map(int, input().split())

cal = []
for _ in range(plus):
    cal.append('+')
for _ in range(minus):
    cal.append('-')
for _ in range(multi):
    cal.append('*')
for _ in range(divi):
    cal.append('/')

def calculate(s, num1, num2):
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '*':
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2

max_num = float('-inf')
min_num = float('inf')
permu = permutations(cal, n-1)
permu = list(set(permu))
for c in permu:
    lst = deepcopy(num_list)
    for i in range(len(c)):
        lst[i+1] = calculate(c[i], lst[i], lst[i+1])
    max_num = max(max_num, lst[n-1])
    min_num = min(min_num, lst[n-1])
print(max_num)
print(min_num)


