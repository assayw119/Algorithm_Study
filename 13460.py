# rowcol = list(map(int, input().split()))
# row = rowcol[0]
# col = rowcol[1]
# lst = []
# for i in range(row):
#     row_ = input()
#     lst.append(row_)
# arr = [[lst[j][i] for i in range(col)] for j in range(row)]
# print(arr)
from collections import deque



def dfs(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if lst[x][y]=='.':
        lst[x][y]='#'


n,m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input())))
