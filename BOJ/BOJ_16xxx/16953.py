a,k = map(int, input().split())

count = 1
def test(b):
    global count, a
    if b % 2 == 1 and str(b)[-1] != '1':
        return -1
    else:
        if str(b)[-1] == '1':
            b_ = int(str(int(b))[:-1])
            count += 1
        else:
            b_ = int(b//2)
            count += 1
        if a == b_:
            return count
        elif a > b_:
            return -1
        else:
            return test(b_)


print(test(k))