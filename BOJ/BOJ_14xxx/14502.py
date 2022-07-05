import sys
import itertools
from collections import deque
from copy import deepcopy

n,m = map(int, sys.stdin.readline().split())
graph_ = []
zero_place = []
two_place = []
for i in range(n):
    place = list(map(int, sys.stdin.readline().split()))
    graph_.append(place)
for i in range(n):
    for j in range(m):
        if graph_[i][j] == 0:
            zero_place.append([i,j])
        elif graph_[i][j] == 2:
            two_place.append([i,j])

def bfs(x, y):
    global graph
    global visited
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True
    while q:
        x_, y_ = q.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    # print(graph)
result = []
combinations = itertools.combinations(zero_place, 3)
for c in combinations:
    # print(c)
    graph = deepcopy(graph_)
    for loc in c:
        graph[loc[0]][loc[1]] = 1
    visited = [[False] * m for _ in range(n)]
    for point in two_place:
        bfs(point[0], point[1])
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    # print(count)
    result.append(count)
    # break
print(max(result))


