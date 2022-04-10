def d(a):
    b = list(map(int, str(a)))
    ans = a
    for i in b:
        ans += i
    return ans

lst10000 = [i for i in range(1, 10000)]
lst = []
for i in lst10000:
    if d(i) in lst10000:
        lst.append(d(i))
result = sorted(set(lst10000) - set(lst))

for i in result:
    print(i)