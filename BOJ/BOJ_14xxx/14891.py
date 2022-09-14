import sys
input = sys.stdin.readline

topni = [list(input()) for _ in range(4)]
# 0 = N극!!
# 1 = S극!!
k = int(input())
# turn = [list(map(int, input().split())) for _ in range(k)]

def rotate(lst, dir):
    if dir == 1: # 시계방향 회전
        lst.insert(0, lst[-1])
        del lst[-1]
    elif dir == -1: # 반시계방향 회전
        a = lst[0]
        del lst[0]
        lst.append(a)
    else:
        pass
    return lst
for _ in range(k):

    num, direction = map(int, input().split())

    left_sn = topni[num-1][6]
    right_sn = topni[num-1][2]

    rotate_how = {}
    rotate_how[num-1] = direction

    for i in range(1,4):
        if num + i <= k: # 오른쪽에 있는 톱니바퀴들
            left_sn_next2 = topni[num+i-1][6]
            right_sn_next1 = topni[num+i-2][2]

            if right_sn_next1 == left_sn_next2:
                rotate_how[num+i-1] = 0
            else:
                rotate_how[num+1-i] = -direction

        if num - i > 0:
            right_sn_next2 = topni[num-i-2][6]
            left_sn_next1 = topni[num-i-1][2]

            if right_sn_next2 == left_sn_next1:
                rotate_how[num-i-1] = 0
            else:
                rotate_how[num-i-1] = -direction

    for k in range(4):

        # 회전
        # topni[num-1] = rotate(topni[num-1], direction)
        topni[k] = rotate(topni[k], rotate_how[k])
        print(topni[k])





