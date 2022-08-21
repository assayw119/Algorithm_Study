import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for _ in range(n):
    t,p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n+1)
total = 0
for i in range(n):
    total = max(total, dp[i])
    if i+time[i] > n:
        continue

    dp[i+time[i]] = max(dp[i+time[i]], total + pay[i])
print(max(dp))