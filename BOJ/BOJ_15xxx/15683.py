import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = []
for i in range(n):
    for j in range(m):
        for k in range(1,6):
            if graph[i][j] == k:
                q.append((i,j,k))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
for x,y,c in q:

    if c == 5:
        for i in range(4):
            for j in range(1,6):
                nx = x + dx[i]*j
                ny = y + dy[i]*j

                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if graph[nx][ny] != 0:
                    break
                graph[nx][ny] = '#'

for i in graph:
    print(i)

def direction_4(graph, x,y,c):


def count_0(graph, x,y,direction):
    cnt = 0
    for i in range(1,m):
        if direction == 'left':
            nx,ny = x,y-i
        if direction == 'right':
            nx,ny = x,y+1
    for i in range(1,n):
        if direction == 'up':
            nx,ny = x-i,y
        if direction == 'down':
            nx,ny = x+i,y

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue

        
