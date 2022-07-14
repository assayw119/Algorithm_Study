from collections import deque

n,m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
# visited = [[False] * n for _ in range(n)]

def search_std(location):
    global n
    global arr
    std_x, std_y = n,n
    for x, y in location:
        if arr[x][y] != 0:
            if x < std_x:
                std_x = x
                std_y = y
            elif x == std_x:
                if y < std_y:
                    std_x = x
                    std_y = y
    return std_x, std_y

def search(x,y, graph):
    global max_block_len
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    loc = []
    block_list_info = []
    block_len, rainbow_len = 1,0
    # max_block_len = 0
    while q:


        q_x, q_y = q.popleft()
        loc.append((q_x, q_y))
        for i in range(4):
            nx = q_x + dx[i]
            ny = q_y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            if (graph[nx][ny] == graph[x][y] or graph[nx][ny] == 0) and not visited[nx][ny] and graph[nx][ny] != -1:
                q.append((nx, ny))
                visited[nx][ny] = True

                if graph[nx][ny] == 0:
                    rainbow_len += 1
                block_len += 1
                # if block_len > max_block_len:
                #     max_block_len = block_len

    if block_len >= 2:
        block_list_info.append((block_len, rainbow_len, loc))
    return block_list_info

def delete(x,y,graph):
    graph[x][y] = -2


def gravity(graph):

    for x in range(n-1,-1,-1):
        for y in range(n-1,-1,-1):
            if graph[x][y] == -1:
                continue
            elif graph[x][y] != -2:
                k = x
                while True:
                    if k<n-1:
                        if graph[k+1][y] == -1:
                            break
                        if graph[k+1][y] == -2:
                            graph[k+1][y] = graph[k][y]
                            graph[k][y] = -2
                            k += 1
                        else:
                            break
                    else:
                        break
    return graph

def turn(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph


point = 0
# print(search(1,0,arr))
while True:

    block_list_group = []
    max_block_len = 0
    max_rainbow_len = 0

    count = 0
    break_limit = 0
    before_x, before_y = 0,0

    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]
            if arr[i][j] > 0:
                count += 1
                search_result = search(i,j,arr)

                if search_result != []:
                    # 크기가 가장 큰 블록
                    if search_result[0][0] > max_block_len:
                        max_block_len = search_result[0][0]
                        max_rainbow_len = search_result[0][1]
                        result_loc = search_result[0][2]
                        a = arr[i][j]
                    elif search_result[0][0] == max_block_len:
                        # 블록 크기가 같고 무지개 블록 수가 가장 많은 블록
                        if search_result[0][1] > max_rainbow_len:
                            max_block_len = search_result[0][0]
                            max_rainbow_len = search_result[0][1]
                            result_loc = search_result[0][2]
                            a = arr[i][j]
                        elif search_result[0][1] == max_rainbow_len:
                            # 블록 크기, 무지개 블록 수가 같고 기준블록 행이 가장 큰 블록.
                            std_x, std_y = search_std(search_result[0][2])
                            if before_x < std_x:
                                max_block_len = search_result[0][0]
                                max_rainbow_len = search_result[0][1]
                                result_loc = search_result[0][2]
                                before_x = std_x
                                before_y = std_y
                            elif before_x == std_x:
                                # 행까지 다 같고 열이 더 큰 블록
                                if before_y < std_y:
                                    max_block_len = search_result[0][0]
                                    max_rainbow_len = search_result[0][1]
                                    result_loc = search_result[0][2]
                                    before_x = std_x
                                    before_y = std_y

                else:
                    break_limit += 1
    if count == break_limit:
        break
    point += max_block_len ** 2
    # print(max_block_len, max_rainbow_len, result_loc)
    # print(point)
    for i,j in result_loc:
        delete(i,j,arr)
    # print(gravity(arr))
    # print(turn(gravity(arr)))
    arr = gravity(turn(gravity(arr)))
    # print(arr)
    # print()



print(point)





