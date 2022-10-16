import sys
from copy import deepcopy
input= sys.stdin.readline

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
new_graph = deepcopy(graph)

# if n==1 or m==1:
#     flag = False
#     for i in range(m):
#         for j in range(n):
#             if graph[i][j] == 0:
#                 flag = True
#                 break
#     if flag:
#         print(1)
#     else:
#         print(0)
# else:
size = 0
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            if graph[i][j] == 0:
                size = 1
                continue


        if new_graph[i][j] != 0:
            continue
        if new_graph[i][j-1] or new_graph[i-1][j] or new_graph[i-1][j-1]:
            continue
        k = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1
        # if k > size:
        graph[i][j] = k
        if k+1 > size:
            size = k+1
for i in graph:
    print(i)
print(size)