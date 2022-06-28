import sys

a = int(sys.stdin.readline())

def sorting(lst, temp, count):
    num_max = max(lst)
    if lst[0] != num_max:
        lst.append(lst[0])
        if temp[0] == True:
            temp.append(True)
        else:
            temp.append(False)
        del lst[0]
        del temp[0]
        # print(lst, temp)
        return sorting(lst, temp, count)
    else:
        if temp[0] == True:
            idx = temp.index(True)
            return idx + count + 1
        else:
            count += 1
            # print(lst, temp)
            return sorting(lst[1:], temp[1:], count)

for _ in range(a):
    n, m = map(int, sys.stdin.readline().split())
    q = list(map(int, sys.stdin.readline().split()))
    temp = [False] * n
    temp[m] = True

    print(sorting(q, temp, 0))
