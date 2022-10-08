from collections import deque
import sys

input = sys.stdin.readline

n, m, k, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

num=1
result = 0
while 1:
    visited = [[0] * n for _ in range(n)]

    q = deque()

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            # 성장
            if graph[i][j] > 0:
                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if graph[nx][ny] > 0:
                        graph[i][j] += 1

                q.append((i, j))
                visited[i][j] = 1

            # 제초제 연도 지남 처리
            if graph[i][j] < -1:
                graph[i][j] += 1
                if graph[i][j] == -1:
                    graph[i][j] = 0
    # print("성장", num,'번쩨')
    # for i in graph:
    #     print(i)
    # print()

    # 번식
    while q:
        x, y = q.popleft()

        # 번식 위치 찾기, 번식하는 나무 수
        new_tree = []
        new_cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] < 0:
                continue
            if visited[nx][ny]:
                continue
            new_tree.append((nx, ny))
            new_cnt += 1

        # 번식하기
        for new_x, new_y in new_tree:
            graph[new_x][new_y] += graph[x][y] // new_cnt
            # visited[new_x][new_y] = 1
    # print("번식", num,'번쩨')
    # for i in graph:
    #     print(i)
    # print()


    # 어느곳에 제초할까
    dx = [1,-1,1,-1]
    dy = [1,1,-1,-1]


    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                q.append((i,j))

    max_delete_tree = 0
    max_delete_loc = (n,n)
    while q:
        x,y = q.popleft()
        delete_tree = graph[x][y]
        for i in range(4):
            for j in range(1,k+1):
                nx = x + dx[i]*j
                ny = y + dy[i]*j
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] <= 0:
                    break
                if graph[nx][ny] > 0:
                    delete_tree += graph[nx][ny]
        if delete_tree >= max_delete_tree:
            # 박멸나무 수 같은 경우 더 작은 행/열
            if delete_tree == max_delete_tree:
                max_delete_loc = min((x,y), max_delete_loc)
            else:
                max_delete_loc = x,y
            max_delete_tree = delete_tree

    # 제초 시작
    # print(max_delete_loc)
    if max_delete_loc != (n,n):
        jx,jy = max_delete_loc
        result += graph[jx][jy]
        graph[jx][jy] = -(c+2)
        for i in range(4):
            for j in range(1,k+1):
                nx = jx + dx[i] * j
                ny = jy + dy[i] * j
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 벽인 경우 멈춤
                if graph[nx][ny] == -1:
                    break
                # 나무 없는 경우 그 칸 까지만 제초
                if graph[nx][ny] == 0 or graph[nx][ny] < -1:
                    graph[nx][ny] = -(c+2)
                    break
                result += graph[nx][ny]
                graph[nx][ny] = -(c+2) # 제초제 남아있는 년도
    # print("제초", num,'번쩨')
    # for i in graph:
    #     print(i)
    # print(max_delete_tree,result)
    # print()

    m -= 1
    if not m:
        break
    num += 1


print(result)