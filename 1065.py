def h(a):
    han = 0
    if a < 100:
        han = a
    else:
        han = 99
        for i in range(100, a+1):
            num1 = i // 100
            num2 = i % 100 // 10
            num3 = i % 10

            test1 = num1 - num2
            test2 = num2 - num3

            if test1 == test2:
                han += 1
                # print(test1, test2, i)

            elif -test1 == -test2:
                han += 1
                # print(test1, test2, i)
    return han

print(h(int(input())))
