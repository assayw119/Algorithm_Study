import sys
from collections import deque
from copy import deepcopy
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
                    # print(i+x,j+y)
                    nx = y
                    ny = 2**k - 1 - x
                    # print('->',i+nx,j+ny)
                    graph[i+nx][j+ny] = arr[i+x][j+y]

            # print()
    return graph

def decrease(arr):
    graph = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx>=n or nx<0 or ny>=n or ny<0:
                        continue
                    if arr[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    graph[x][y] = arr[x][y] - 1
                else:
                    graph[x][y] = arr[x][y]
    return graph

def bfs(arr):
    q = deque()
    visited = [[0]*n for _ in range(n)]
    ice_size = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = 1
                cnt = 1
                size = arr[i][j]
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx>=n or nx<0 or ny>=n or ny<0:
                            continue
                        if arr[nx][ny] > 0 and not visited[nx][ny]:
                            cnt += 1
                            size += arr[nx][ny]
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                ice_size.append((size, cnt))
    return ice_size


for l in L:

    arr = decrease(storm(arr, l))
    for i in arr:
        print(i)
    print(bfs(arr), l)
if bfs(arr) != []:
    max_size = sorted(bfs(arr), key=lambda x:x[1], reverse=True)[0]
    for i in max_size:
        print(i)
else:
    print(0)