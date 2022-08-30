import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    happy = False
    n = int(input())
    house_x, house_y = map(int, input().split())
    mart = [list(map(int, input().split())) for _ in range(n)]
    mart.sort()
    festival_x, festival_y = map(int, input().split())


    visited = {}
    visited[(house_x,house_y)] = 0
    for i,j in mart:
        visited[(i,j)] = 0
    q = deque()
    q.append((house_x, house_y))

    while q:
        x,y = q.popleft()
        if visited[(x,y)]:
            continue
        if abs(festival_x-x) + abs(festival_y-y) <= 1000:
            happy = True
            break
        for mart_x, mart_y in mart:
            if abs(mart_x-x) + abs(mart_y-y) <= 1000 and not visited[(mart_x, mart_y)]:
                q.append((mart_x, mart_y))
        visited[(x,y)] = 1

    if happy:
        print('happy')
    else:
        print('sad')