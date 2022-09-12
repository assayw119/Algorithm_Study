import sys
input = sys.stdin.readline

n = int(input())
power = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [0]*101
for i in range(n):
    p = power[i]
    h = happy[i]

    for j in range(100,0,-1):

        if j > p:
            dp[j] = max(dp[j], dp[j-p] + h)
            # print(dp)
print(max(dp))


# lst = []
# dp = [0] * 100
# for i in range(n):
#     lst.append((power[i], happy[i]))
#     if power[i] < 100:
#         dp[power[i]] = happy[i]
#
# lst.sort(key=lambda x:x[0], reverse=True)
#
# for i in range(n):
#     visited = [0]*100
#     for j in range(99,-1,-1):
#         if dp[j] != 0 and j+lst[i][0] < 100 and not visited[j] and j != lst[i][0]:
#             dp[j+lst[i][0]] = max(dp[j+lst[i][0]], dp[j] + lst[i][1])
#             visited[j+lst[i][0]] = 1
#             print(dp)
# print(max(dp))