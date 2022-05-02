n, k = map(int,input().split())
s = list(map(int, input().split()))


count = 0
for i in s:
    if i % 2 != 0:
        count += 1
        # print(i)
        s.remove(i)
    if k == count:
        break
    elif k > count:


for i in s:
    if i % 2 == 0: