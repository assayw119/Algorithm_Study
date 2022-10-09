import sys
from collections import deque

input = sys.stdin.readline
n,q = map(int, input().split())
n = 2**n
arr = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def storm(arr, k):
    graph = [[0]*n for _ in range(n)]
    for i in range(0,n,2**k):
        for j in range(0,n,2**k):
            for x in range(2**k):
                for y in range(2**k):
                    nx = y
                    ny = 2**k - 1 - x
                    graph[i+nx][j+ny] = arr[i+x][j+y]
    # decrease
    graph2 = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx>=n or nx<0 or ny>=n or ny<0:
                        continue
                    if graph[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    graph2[x][y] = graph[x][y] - 1
                else:
                    graph2[x][y] = graph[x][y]
    return graph2

def bfs(arr):
    q = deque()
    visited = [[0]*n for _ in range(n)]
    size = []
    ice_sum = 0
    for i in range(n):
        for j in range(n):
            ice_sum += arr[i][j]
            if arr[i][j] > 0 and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = 1
                cnt = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx>=n or nx<0 or ny>=n or ny<0:
                            continue
                        if arr[nx][ny] > 0 and not visited[nx][ny]:
                            cnt += 1
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                size.append(cnt)
    if size == []:
        ice_size = 0
    else:
        ice_size = max(size)
    return ice_sum, ice_size

for l in L:

    arr = storm(arr, l)

print(bfs(arr)[0])
print(bfs(arr)[1])
