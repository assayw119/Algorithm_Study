n,k = map(int, input().split())

weight = [0]
value = [0]
for i in range(n):
    w,v = map(int, input().split())
    weight.append(w)
    value.append(v)

d = [[0] * (k+1) for i in range(n+1)]
total = []
for i in range(n):
    for j,jval in enumerate(weight):
        if i>j:
            pass
        else:
            if ival+jval <= k:
                total.append(value[i]+value[j])
print(max(total))
