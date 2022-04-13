from collections import deque

# 아무도 없는 자리일 경우 1 반환
def count_pos(x, y):
    # if x < 0 or x >= a or y < 0 or y >= a:
    #     return 0

    if graph[x][y] == 'X':
        return 1

    return 0

# 근처에 좋아하는 학생 있을 경우 True 반환
def near_fri(x, y, s):
    count = 0
    # if x < 0 or x >= a or y < 0 or y >= a:
    #     pass
    if graph[x][y] in std[s]:
        count += 1

    return count

a = int(input())

# dic = {}
# graph = [['X'] * a] * a
std = []
data = []
for i in range(a*a):
    data.append(list(map(int, input().split())))

std = {}
for i in range(a*a):
    # 해당 학생, 좋아하는 학생 리스트, x좌표, y좌표, 2번 만족, 3번 만족
    std[data[i][0]] = data[i][1:]
# print(2 in std[4])
# print(std)
dic = {}
# for i in range(a*a):
#     q = deque(std[i])
#     print(q)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     while q:
#         # v = q.popleft()
#         # print(v)
#
#         x = q[2]
#         y = q[3]
#         x_count = q[4]
#         fri_count = q[5]
#         if x == 2 and y == 2:
#             break
#         if graph[x][y] == 'X':
#             count_list = []
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 # 장외 탈락
#                 if nx < 0 or nx >= a or ny < 0 or ny >= a:
#                     continue
#
#                 # if near_fri(nx, ny) == True:
#                 #     fri_count += 1
#
#                 # 좋아하는 친구 근처에 얼마나 있는지
#                 if graph[nx][ny] in q[1]:
#                     fri_count += 1
#                 else:
#                     fri_count = 0
#
#                 # 근처에 비어있는 자리 얼마나 있는지
#                 x_count += count_pos(nx, ny)
#
#                 count_list.append([nx, ny, fri_count, x_count])
#
#         # max_fri_count = max(count_list[:][2])
#         # max_x_count = max(count_list[:][3])
#         for i, j in enumerate(count_list):
#             if j[2] == max(count_list[:][2]) and j[3] == max(count_list[:][3]):
#                 x_ = count_list[i][0]
#                 y_ = count_list[i][1]
#                 q = [q[0], q[1], x_, y_, j[3], j[2]]
#         break
# graph = [['X'] * a] * a
graph = []
for i in range(a):
    graph.append(['X'] * a)
def search(student):
    count_dic = {}
    # for student in std.keys():

    # 근처 친구 수, 근처 비어있는 자리, x좌표, y좌표
    count_dic[student] = [0, 0, 0, 0]
    count_list = []
    for i in range(a):
        for j in range(a):

            fri_count = 0
            x_count = 0
            if graph[i][j] != 'X':
                continue
            else:
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]


                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 장외 탈락
                    if nx < 0 or nx >= a or ny < 0 or ny >= a:
                        continue

                    fri_count += near_fri(nx, ny, student)
                    x_count += count_pos(nx, ny)
                # print(student, i, j, fri_count, x_count)
                count_list.append([student, i, j, fri_count, x_count ])
    # print(count_list)
    # if count_dic[student][1] <= x_count:
    #     if count_dic[student][1] == x_count:
    #         continue
    #     elif count_dic[student][0] <= fri_count:
    #         if count_dic[student][0] == fri_count:
    #             pass
    #         count_dic[student] = [fri_count, x_count, i, j]

    fri_count_max = 0
    x_count_max = 0

    # 좋아하는 학생이 인접한 수가 가장 많은 것 거르기
    for i in count_list:
        if fri_count_max < i[3]:
            fri_count_max = i[3]

        # if x_count_max < i[4]:
        #     x_count_max = i[4]

    count_dic[student][0] = fri_count_max
    # count_dic[student][1] = x_count_max

    # 그 중 비어 있는 칸 가장 많은 것 거르기
    for i in count_list:
        if i[3] == fri_count_max:
            if x_count_max < i[4]:
                x_count_max = i[4]


    # 가장 작은 x, y좌표 거르기
    for i in count_list:
        if i[3] == fri_count_max:
            if i[4] == x_count_max:
                x = i[1]
                y = i[2]
                break

    # x = count_dic[student][2]
    # y = count_dic[student][3]
    graph[x][y] = student
    # print(count_dic)
    return graph

# print(search(4))
# print(search(3))
for i in std.keys():
    print(search(i))
