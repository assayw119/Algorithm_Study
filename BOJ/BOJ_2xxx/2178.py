import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

q = deque()
q.append((0,0))
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if arr[nx][ny] == 0 or visited[nx][ny]:
            continue
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx,ny))

        if nx == n-1 and ny == m-1:
            print(visited[nx][ny])
            break
