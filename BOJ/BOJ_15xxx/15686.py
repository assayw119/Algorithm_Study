from collections import deque
from itertools import combinations
from copy import deepcopy

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(arr):
    chicken = []
    house = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                house.append((i, j))
            if arr[i][j] == 2:
                chicken.append((i, j))
    return chicken, house

def close(x,y,arr):
    q = deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny]:
                if arr[nx][ny] == 2:
                    return nx,ny
                else:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i,j))
        if arr[i][j] == 2:
            chicken.append((i,j))



min_result = float('inf')
for k in list(combinations(check(arr)[0], len(chicken)-m)):
    arr_ = deepcopy(arr)
    for x,y in k:
        arr_[x][y] = 0
    distance = 0
    for x,y in check(arr_)[1]:
        close_x, close_y = close(x,y,arr_)
        distance += abs(x-close_x) + abs(y-close_y)
    min_result = min(min_result, distance)
print(min_result)
