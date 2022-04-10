a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    avg = (sum(b) - b[0]) / b[0]
    count = 0

    for i in range(1, len(b)):
        if b[i] > avg:
            count += 1
        else:
            pass

    val = count/b[0]*100
    result = "{:.3f}{}".format(val,'%')
    print(result)