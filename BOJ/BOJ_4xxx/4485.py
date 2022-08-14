import sys
from collections import deque

input = sys.stdin.readline
num = 0
while 1:
    n = int(input())
    num += 1
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[100000]*n for _ in range(n)]
    visited[0][0] = arr[0][0]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            k = visited[x][y] + arr[nx][ny]
            if k < visited[nx][ny]:
                visited[nx][ny] = k
                q.append((nx,ny))
    print(f'Problem {num}: {visited[n-1][n-1]}')

