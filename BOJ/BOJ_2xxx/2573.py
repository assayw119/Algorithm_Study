import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def decrease(arr):
    q = deque()
    graph = deepcopy(arr)
    visited = [[0]*m for _ in range(n)]
    cnt = 0 # 빙하 개수 체크용
    for x in range(n):
        for y in range(m):
            if arr[x][y] >= 1 and not visited[x][y]:
                cnt += 1
                q.append((x,y))
                while q:
                    q_x, q_y = q.popleft()
                    visited[q_x][q_y] = 1

                    for i in range(4):
                        nx = q_x + dx[i]
                        ny = q_y + dy[i]

                        if nx>=n or nx<0 or ny>=m or ny<0:
                            continue
                        if arr[nx][ny] > 0 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny] = 1
                        if arr[nx][ny] == 0:
                            if graph[q_x][q_y] > 0:
                                graph[q_x][q_y] -= 1
    return graph, cnt


n,m = map(int ,input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

year = 0
while 1:
    arr, cnt = decrease(arr)
    if cnt > 1: # 2개 이상으로 분리가 된 경우
        print(year)
        break
    elif cnt == 0: # 분리가 안되고 다 녹은 경우
        print(0)
        break
    else: # 1년 후에도 분리가 되지 않은 경우
        year += 1