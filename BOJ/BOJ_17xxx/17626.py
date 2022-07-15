import math

n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2,n+1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
    else:
        j = 1
        min_value = 5

        while i-j**2 > 0:
            min_value = min(min_value, dp[i-j**2])
            j += 1
        dp[i] = min_value + 1
print(dp[n])