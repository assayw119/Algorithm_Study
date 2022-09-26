from collections import deque


def solution(n, costs):
    answer = 0

    graph = [[] for _ in range(n)]
    for i in costs:
        x, y, cost = i
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    cost_list = []
    for i in range(n):
        visited = [False for _ in range(n)]
        cost_list.append(bfs(graph, i))
    print(cost_list)
    answer = min(cost_list)

    return answer


def bfs(graph, start):
    q = deque()
    q.append(start)
    # visited[start] = True

    cost_list = []
    while q:

        x = q.popleft()

        cost = 0
        q2 = deque()
        for y, c in graph[x]:
            q2.append((y, c))

        while q2:
            visited = [False for _ in range(len(graph))]
            visited[x] = True
            visited[y] = True
            y, c = q2.popleft()
            # for y,c in graph[x]:

            # if visited[y]:
            #     continue
            # q.append(y)
            # visited[y] = True
            # cost += c
            for y_, c_ in graph[y]:
                if visited[y]:
                    continue
                q2.append((y_, c_))
                cost += c
        cost_list.append(cost)
    print(start, cost_list)

    return min(cost_list)


# def solution(n, costs):
#     answer = 0
#
#     graph = [[] for _ in range(n)]
#     for i in costs:
#         x, y, cost = i
#         graph[x].append((y, cost))
#         graph[y].append((x, cost))
#
#     cost_list = []
#     for i in range(n):
#         visited = [False for _ in range(n)]
#         cost_list.append(bfs(graph, visited, i))
#     print(cost_list)
#     answer = min(cost_list)
#
#     return answer
#
#
# def bfs(graph, visited, start):
#     q = deque()
#     q.append(start)
#     visited[start] = True
#
#     cost = 0
#     while q:
#         x = q.popleft()
#         for y, c in graph[x]:
#             if visited[y]:
#                 continue
#             q.append(y)
#             visited[y] = True
#             cost += c
#     return cost