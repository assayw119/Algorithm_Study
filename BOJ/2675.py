a = int(input())

for i in range(a):
    b = input().split()
    ans = ''
    for i in range(len(b[1])):
        ans += b[1][i] * int(b[0])
    print(ans)