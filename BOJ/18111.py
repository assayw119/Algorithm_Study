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

max_h = graph[0]
min_h = graph[-1]
result_time = 999999999
result_height = 0
for height in range(min_h, max_h+1):
    time = 0
    block = b
    graph_ = graph.copy()
    if (sum(graph_)+block)/len(graph) < height:
        continue

    for i in range(n*m):
        if block < 0:
            break
        temp = graph_[i] - height
        if graph_[i] > height:
            time += 2 * temp
            block += temp
        elif graph_[i] < height:
            if block > 0:
                time += -temp
                block -= -temp
        # graph_[i] = height
        # print(time, height, block)
        # print(graph_, (sum(graph_)+block))
    if time == 0:
        result_time = 0
        result_height = graph[0]
    elif time < result_time:
        result_time = time
        result_height = height
    elif time == result_time:
        if height > result_height:
            result_height = height
print(result_time, result_height)
