import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    length = int(input())
    start, end = map(int, input().split())
    d_x, d_y = map(int, input().split())
    if (start, end) == (d_x, d_y):
        print(0)
        continue

    q = deque()
    q.append((start,end))

    dx = [2,-2,1,-1,2,-2,1,-1]
    dy = [1,1,2,2,-1,-1,-2,-2]

    visited = [[100000]*length for _ in range(length)]
    visited[start][end] = 0

    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=length or nx<0 or ny>=length or ny<0:
                continue

            k = visited[x][y] + 1
            if visited[nx][ny] > k:
                visited[nx][ny] = k
                q.append((nx,ny))

    print(visited[d_x][d_y])