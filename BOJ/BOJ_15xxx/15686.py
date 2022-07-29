from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check():
    chicken = []
    house = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                house.append((i, j))
            if arr[i][j] == 2:
                chicken.append((i, j))
    return chicken, house

min_result = float('inf')
for k in list(combinations(check()[0], m)):
    total_distance = 0
    for h_x, h_y in check()[1]:
        min_distance = float('inf')
        for c_x, c_y in k:
            min_distance = min(min_distance, abs(c_x - h_x) + abs(c_y - h_y))
        total_distance += min_distance
    min_result = min(min_result, total_distance)
print(min_result)