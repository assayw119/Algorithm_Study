a = int(input())
for i in range(a):
    b = input()
    c = b.replace('X', ' ').split()

    val = 0
    for i in c:
        num = len(i)
        while num>0:
            val += num
            num -= 1
    print(val)