import sys
n,m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    miro = list(map(int, sys.stdin.readline().split()))
    graph.append(miro)

dx = [1,0,1]
dy = [0,1,1]

temp = [[0]*m for _ in range(n)]
temp[0][0] = graph[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            temp[i][j] = graph[i][j] + temp[i][j-1]
        elif j == 0:
            temp[i][j] = graph[i][j] + temp[i-1][j]
        else:
            temp[i][j] = max(temp[i-1][j], temp[i][j-1])
            temp[i][j] += graph[i][j]
print(temp[n-1][m-1])