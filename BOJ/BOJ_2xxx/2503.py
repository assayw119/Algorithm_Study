import sys

input = sys.stdin.readline
n = int(input())

def test(number, s, b, lst):
    number = str(number)
    new_list = []


    for i in lst: # 숫자 리스트
        strike = 0
        ball = 0
        for j in range(3):
            if str(i)[j] == number[j]:
                strike += 1
            else:
                if str(i)[j] in number:
                    ball += 1
        if s == strike and b == ball:
            new_list.append(i)
    # print(sorted(new_list))
    return new_list
num_list = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and j != k and k != i:
                num_list.append(i*100 + j*10 + k)

for _ in range(n):
    num, s, b = map(int, input().split())
    num_list = test(num, s, b, num_list)
print(len(num_list))