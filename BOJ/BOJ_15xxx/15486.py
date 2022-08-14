import sys
input = sys.stdin.readline

n = int(input())
day = []
pay = []
for _ in range(n):
    d,p = map(int, input().split())
    day.append(d)
    pay.append(p)
total_pay = 0

dp = [0] * (n+1)
for i in range(n):
    total_pay = max(total_pay, dp[i])
    if i + day[i] > n:
        continue
    dp[i + day[i]] = max(total_pay + pay[i], dp[i+day[i]])
print(max(dp))