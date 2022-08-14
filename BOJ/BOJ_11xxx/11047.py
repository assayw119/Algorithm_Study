import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = []
for _ in range(n):
    num = int(input())
    if num <= k:
        coin.append(num)

cnt = 0
for i in range(len(coin)-1,-1,-1):
    if k == 0:
        break
    while 1:
        if k // coin[i] >= 1:
            k -= coin[i]
            cnt += 1
        else:
            break

print(cnt)