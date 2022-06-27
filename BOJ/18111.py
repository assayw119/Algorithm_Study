import sys
n,m,b = list(map(int, sys.stdin.readline().split()))

lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

graph = []
for i in lst:
    for j in i:
        graph.append(j)
graph.sort(reverse=True)

if graph[0] > 256:
    max_h = 256
else:
    max_h = graph[0]
min_h = graph[-1]
result_time = 100000000
result_height = 0
for height in range(min_h, max_h+1):
    time = 0
    block = b
    graph_ = graph.copy()
    for i in range(n*m):
        if graph_[i] > height:
            time += 2 * (graph_[i] - height)
            block += graph_[i] - height
            graph_[i] = height
        elif graph_[i] < height:
            if block > 0:
                time += height - graph_[i]
                block -= height - graph_[i]
                graph_[i] = height
            else:
                continue
        else:
            pass
    # print(time, height)
    # print(graph_)
    if time == 0 or graph_.count(height) != len(graph_):
        continue
    if time < result_time:
        result_time = time
        result_height = height
    elif time == result_time:
        if height > result_height:
            result_height = height
print(result_time, result_height)
