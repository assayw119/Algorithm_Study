from collections import deque
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)

def bfs(x, y):
    global graph
    global visited
    q = deque()
    q.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = True
    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny] >= height and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
result = []
for height in range(max(max(graph))+1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= height and not visited[i][j]:
                bfs(i,j)
                count += 1
                # print(height, (i,j), count)
    result.append(count)
print(max(result))
