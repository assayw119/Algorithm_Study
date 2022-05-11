n, k = map(int,input().split())
s = list(map(int, input().split()))

def max_1(lst):

    max_count = 0
    count = 0
    for i in range(len(lst)-1):
        if lst[i] == 1 and lst[i] == lst[i+1]:
            count += 1
        else:




for i in range(len(s)):
    if s[i] % 2 == 1:
        s[i] = 0
    else:
        s[i] = 1

print(max_1(s))