import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
virus_loc = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 2:
            virus_loc.append((i,j))
            lst[j] = '*' # *은 비활성 바이러스
        elif lst[j] == 1:
            lst[j] = '-' # -은 벽
        else:
            lst[j] = 100 # 100은 빈칸
    graph.append(lst)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(lst):
    global graph
    global time

    activate_graph = [[0]*n for _ in range(n)]

    q = deque()

    for i in lst:
        q.append((i[0], i[1]))
        activate_graph[i[0]][i[1]] = 1


    while True:
        q2 = deque()
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx>=n or nx<0 or ny>=n or ny<0:
                    continue
                if graph[nx][ny] == '-': # 벽 만나면 continue
                    continue
                # if (nx,ny) in lst: # 활성 바이러스 만나면 continue
                if activate_graph[nx][ny] == 1: # 활성 바이러스 만나면 continue
                    continue
                if not time[nx][ny]: # 비활성 또는 빈칸이면서 방문 안한 곳이라면
                    time[nx][ny] = time[x][y] + 1
                    q2.append((nx,ny))
        if len(q2) == 0:
            break
        for i in q2:
            q.append(i)
    flag = True
    max_time = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '*':
                time[i][j] = 0
            if graph[i][j] == 100 and time[i][j] == 0:
                flag = False # 빈칸인데 바이러스 퍼지지 못한경우
                return 0, flag
            max_time = max(max_time, time[i][j])
    #     print(time[i])
    # print(max_time, flag, lst)
    return max_time, flag

virus_list = combinations(virus_loc, m)

answer = int(1e9)
for lst in virus_list:
    visited = [[0] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    xylist = []
    for k in range(m):
        x_, y_ = lst[k][0], lst[k][1]
        xylist.append((x_,y_))

    result, flag = bfs(xylist)
    if flag:
        if answer > result :
            answer = result
if answer != int(1e9):
    print(answer)
else:
    print(-1)
