for _ in range(int(input())):
    n = int(input())

    array = list(map(int, input().split()))
    total_money = int(input())

    d = [10001] * (total_money + 1)
    d[0] = 0
    d[total_money] = 0

    for i in range(n):
        for j in range(array[i], total_money+1):
            if d[j-array[i]] != 10001:
                if j == total_money:
                    d[j] += 1
                else:
                    d[j] = d[j - array[i]] + 1
                print(d)

    if d[total_money] == 0:
        print(-1)
    else:
        print(d[total_money])
