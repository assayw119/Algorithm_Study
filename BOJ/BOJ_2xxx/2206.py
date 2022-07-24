from collections import deque
from copy import deepcopy

n,m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0]*m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0,0))
flag = False
min_result = float('inf')
while q:
    w, x, y = q.popleft()
    if x == n-1 and y == m-1:
        min_result = min(visited[w][x][y], min_result)
        flag = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if arr[nx][ny] == 1 and w == 0:
                visited[1][nx][ny] = visited[0][x][y] + 1
                q.append((1,nx,ny))
            elif arr[nx][ny] == 0 and visited[w][nx][ny] == 0:
                visited[w][nx][ny] = visited[w][x][y] + 1
                q.append((w,nx,ny))

print(min_result if flag else -1)