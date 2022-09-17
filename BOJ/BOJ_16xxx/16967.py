import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h+x)]

result = []
for i in range(x):
    result.append(graph[i][:w])

if x < h:
    for i in range(x,h):
        k = graph[i][y:]
        a = graph[i-x][:w-y+1]
        lst = [i-j for i,j in zip(k, a)]
        lst = graph[i][:y] + lst[:w-1]
        result.append(lst)
        graph[i] = lst
for i in range(h):

    for j in range(w):
        print(result[i][j], end=' ')
    print()