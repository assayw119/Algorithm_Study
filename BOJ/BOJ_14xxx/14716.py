import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

q = deque()
visited = [[0]*n for _ in range(m)]
dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]
cnt = 0
for i in range(m):
    for j in range(n):

        if not visited[i][j] and arr[i][j] == 1:
            q.append((i,j))

            while q:
                x,y = q.popleft()

                visited[x][y] = 1
                for k in range(8):

                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx>=m or nx<0 or ny>=n or ny<0:
                        continue
                    if visited[nx][ny]:
                        continue
                    if arr[nx][ny] == 1:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
            cnt += 1
print(cnt)