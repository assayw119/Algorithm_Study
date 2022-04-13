from collections import deque

# 아무도 없는 자리일 경우 1 반환
def count_pos(x, y):
    # if x < 0 or x >= a or y < 0 or y >= a:
    #     return 0

    if graph[x][y] == 'X':
        return 1

    return 0

# 근처에 좋아하는 학생 있을 경우 True 반환
def near_fri(x, y):
    if x < 0 or x >= a or y < 0 or y >= a:
        return False
    if graph[x][y] != 'X':
        if graph[x][y] in dic[std]:
            return True
    return False

a = int(input())

# dic = {}
graph = [['X'] * a] * a
std = []
data = []
for i in range(a*a):
    data.append(list(map(int, input().split())))


for i in range(a):
    for j in range(a):


        # 해당 학생, 좋아하는 학생 리스트, x좌표, y좌표, 2번 만족, 3번 만족
        std.append((data[i+j+i*2][0], data[i+j+i*2][1:], 0, 0, 0, 0))


dic = {}
for i in range(a*a):
    q = deque(std[i])
    print(q)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        v = q.popleft()
        x = v[2]
        y = v[3]
        x_count = v[4]
        fri_count = v[5]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or nx >= a or ny < 0 or ny >= a:
                continue

            # if near_fri(nx, ny) == True:
            #     fri_count += 1
            if graph[nx][ny] in q[1]:
                fri_count += 1

            x_count += count_pos(nx, ny)

        q.append(q[0],q[1], nx, ny, x_count, fri_count)
        print(q)




# q = deque(data)
# while q:
#     v = q.popleft()
#
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     x,y = (0,0)
#     count = 0
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= a or ny < 0 or ny >= a:
#             continue
#         if graph[nx][ny] == 'X':
#             # 이동하는 곳이 비어있는 경우
#             try:
#                 for i in range(4):
#                     if graph[nx+dx[i]][ny+dy[i]] == 'X':
#                         count += 1
#                         graph[nx + dx[i]][ny + dy[i]] = q[0]
#             except:
#                 continue
#         print(q)
