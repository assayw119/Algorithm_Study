import sys

input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            print(dp[i][j])
            break
        down_point = i + graph[i][j]
        left_point = j + graph[i][j]

        if 0 <= left_point < n:
            dp[i][left_point] += dp[i][j]
        if 0 <= down_point < n:
            dp[down_point][j] += dp[i][j]

