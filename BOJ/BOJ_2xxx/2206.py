from collections import deque
from copy import deepcopy

n,m = map(int, input().split())

# arr = [list(input()) for _ in range(n)]
arr = []
one_loc = []
for a in range(n):
    lst = list(input())
    arr.append(lst)
    for b in range(m):
        if lst[b] == '1':
            one_loc.append((a,b))

arr[0][0] = '1'

def bfs(start, end, graph):
    q = deque()
    q.append((start, end))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        # print(x,y)

        if x == n-1 and y == m-1:
            # print('!!!')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == '0':

                q.append((nx,ny))
                graph[nx][ny] = str(int(graph[x][y]) + 1)

    return int(graph[n-1][m-1])

result = []
for i,j in one_loc:
    # print(i,j)
    arr_ = deepcopy(arr)
    arr_[i][j] = '0'
    result.append(bfs(0,0,arr_))
#     print()
# print(result)

result.append(bfs(0,0,arr))

if set(result) == {0}:
    print(-1)
elif min(result) == 0:
    print(list(set(result))[1])
else:
    print(min(result))
