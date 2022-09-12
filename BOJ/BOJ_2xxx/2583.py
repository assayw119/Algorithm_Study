import sys
from collections import deque
input = sys.stdin.readline
m,n,k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(k)]

graph = [[0] * m for _ in range(n)]

for i in range(k):
    x1,y1,x2,y2 = arr[i]

    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[x][y] = 1

q = deque()
visited = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
area_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            q.append((i,j))
            cnt += 1

            area = 1
            while q:
                x,y = q.popleft()
                visited[x][y] = 1

                for o in range(4):

                    nx = x + dx[o]
                    ny = y + dy[o]

                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                    if graph[nx][ny] == 0 and not visited[nx][ny]:
                        area += 1
                        q.append((nx,ny))
                        visited[nx][ny] = 1
            area_list.append(area)
print(cnt)
for a in sorted(area_list):
    print(a, end=' ')