import sys
import math

# sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)
visited = [[False]*n for _ in range(n)]
# print(list(set(visited[0])))
# root_n = int(math.log(n,3))

# for i in range(root_n,0,-1):
#     new_graph = []
#     for x in range(3**i):
#         for y in range(3**i):
#             if visited[x][y] == False:

dic = {}
dic['-1'] = 0
dic['0'] = 0
dic['1'] = 0
def check(graph, num):
    # global graph
    global visited
    global n
    global dic

    # for i in range(0, num, num2):
    #     for j in range(0, num, num2):
    graph_split = []

    for x in range(num):
        for y in range(num):
            # print(i+x, j+y)
            graph_split.append(graph[x][y])
    # print(list(set(new_graph)))
    if len(list(set(graph_split))) > 1:

        root_n = num // 3
        new_graph = []
        for a in range(0,num,root_n):
            l = graph[a:a + root_n]

            for b in range(0,num,root_n):
                for i in l:
                    new_graph.append(i[b:b+root_n])
        print(new_graph)
        check(new_graph, root_n)
        # check(graph, num, root_n)
    else:
        dic[str(list(set(graph_split))[0])] += 1
    return dic

print(check(graph, n))
