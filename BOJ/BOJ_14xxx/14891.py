topni = [list(input()) for _ in range(4)]

k = int(input())
turn = [list(map(int, input().split())) for _ in range(k)]

def rotate(lst, dir):
    if dir == 1:
        lst.insert(0, lst[-1])
    else:
        a = lst[0]
        del lst[0]
        lst.append(a)
    return lst
for i in range(k):

    num, direction = turn[i][0], turn[i][1]

    left_sn = topni[num][6]
    right_sn = topni[num][2]

    # 회전
    topni[num] = rotate(topni[num], direction)
    




