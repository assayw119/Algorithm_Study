from collections import deque

def dfs(x,y):
    global arr
    global l
    global r
    global people
    global lst
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x,y))

    temp = []
    temp.append((x,y))
    people = arr[x][y]

    visited[x][y] = 1

    while q:
        q_x, q_y = q.popleft()

        for i in range(4):
            nx = q_x + dx[i]
            ny = q_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l <= abs(arr[q_x][q_y] - arr[nx][ny]) <= r and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                # print(arr[nx][ny], '추가!', (nx,ny), visited[q_x][q_y])
                temp.append((nx, ny))
                people += arr[nx][ny]
    if len(temp) > 1:
        lst.append(temp)
        people_list.append(people)

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

while True:
    visited = [[0] * n for _ in range(n)]
    lst = []
    people_list = []
    people = 0

    for i in range(n):
        for j in range(n):
            # print(arr[i][j], '시작')
            if visited[i][j] == 1:
                continue
            dfs(i,j)
    # print(lst, people_list)

    if len(lst) == 0:
        break

    for k in range(len(people_list)):
        for a in range(len(lst[k])):
            arr[lst[k][a][0]][lst[k][a][1]] = people_list[k] // len(lst[k])
    # print(arr)
    result += 1

print(result)

