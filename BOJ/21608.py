# 아무도 없는 자리일 경우 1 반환
def count_pos(x, y):
    # if x < 0 or x >= a or y < 0 or y >= a:
    #     return 0

    if graph[x][y] == 'X':
        return 1

    return 0

# 근처에 있는 좋아하는 학생 수 반환
def near_fri(x, y, s):
    count = 0
    # if x < 0 or x >= a or y < 0 or y >= a:
    #     pass
    if graph[x][y] in std[s]:
        count += 1

    return count

def search(student):
    count_dic = {}

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

    fri_count_max = 0
    x_count_max = 0

    # 좋아하는 학생이 인접한 수가 가장 많은 것 거르기
    for i in count_list:
        if fri_count_max < i[3]:
            fri_count_max = i[3]
    count_dic[student][0] = fri_count_max

    # 그 중 비어 있는 칸 가장 많은 것 거르기
    for i in count_list:
        if i[3] == fri_count_max:
            if x_count_max < i[4]:
                x_count_max = i[4]
    count_dic[student][1] = x_count_max

    # 그 중 가장 작은 x, y좌표 거르기
    for i in count_list:
        if i[3] == fri_count_max:
            if i[4] == x_count_max:
                x = i[1]
                y = i[2]
                break

    graph[x][y] = student
    # print(count_dic)
    return graph

a = int(input())

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

graph = []
for i in range(a):
    graph.append(['X'] * a)

# 최종 그래프 변수
for i in std.keys():
    result = search(i)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
for x in range(a):
    for y in range(a):
        num = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 장외 탈락
            if nx < 0 or nx >= a or ny < 0 or ny >= a:
                continue

            if result[nx][ny] in std[result[x][y]]:
                num += 1
        if num == 1:
            total += 1
        elif num == 2:
            total += 10
        elif num == 3:
            total += 100
        elif num == 4:
            total += 1000
print(total)