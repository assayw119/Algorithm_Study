n,m,b = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

max_h = 0
min_h = 256
for i in graph:
    for j in i:
        if j > max_h:
            max_h = j
        if j < min_h:
            min_h = j

result_time = 100000000
result_height = 0
for height in range(min_h, max_h+1):
    time = 0
    block = b
    for i in range(n):
        for j in range(m):
            if graph[i][j] > height:
                time += 2 * (graph[i][j] - height)
                graph[i][j] = height
                block += 1
            elif graph[i][j] < height:
                if block > 0:
                    block -= 1
                    time += height - graph[i][j]
                    graph[i][j] = height
            else:
                pass
    # print(time, height)
    if time == 0:
        continue
    if time < result_time:
        result_time = time
        result_height = height
    elif time == result_time:
        if height > result_height:
            result_height = height
print(result_time, result_height)
