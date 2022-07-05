a = list(input())

counter = {}
for i in a:
    if i.upper() in counter:
        counter[i.upper()] += 1
    else:
        counter[i.upper()] = 1

lst = []
for key, value in counter.items():
    if value == max(counter.values()):
        lst.append(key)

if len(lst) > 1:
    print('?')
else:
    print(lst[0].upper())