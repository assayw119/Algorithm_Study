from collections import deque

m,n = map(int, input().split())
data = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        data.append((graph[i][j], 0, i, j))
q = deque(data)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0

while q:
    tomato, s, x, y = q.popleft()
    if tomato == 1:

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((graph[nx][ny], s+1, nx, ny))
            else:
                continue

days = []
for i in range(n):
    for j in range(m):
        days.append(graph[i][j])

if 0 in days:
    print(-1)
else:
    print(s)
