from collections import deque

a = int(input())
graph = []
for i in range(a):
    graph.append(list(map(str, input().split())))

q = deque(graph)