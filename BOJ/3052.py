lst = []
for i in range(10):
    a = int(input())
    b = a%42
    lst.append(b)
c = set(lst)
print(len(c))