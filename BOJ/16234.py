from collections import deque

def dfs(x,y,con, lst=[]):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 다음 노드 조건 보고 dfs 재귀호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # print(abs(con[x][y] - con[nx][ny]) )
            if l <= abs(con[x][y] - con[nx][ny]) <= r:
                lst.append(con[x][y])
                dfs(nx, ny, con)
                # print(x,y,con[x][y],con[nx][ny])
                print(lst)
            return True

    return False


n, l, r = map(int, input().split())


con = []
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    con.append(arr)
graph = [[0] * n for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        # 현재 위치에서 dfs 실행
        if dfs(i,j,con) == True:
            result += 1
print(result)

