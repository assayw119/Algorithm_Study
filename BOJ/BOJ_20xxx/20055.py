import sys
input = sys.stdin.readline
n,k = map(int, input().split())
lst = list(map(int, input().split()))

stage = 0
zero_num = 0
robot = [0]*n
while 1:
    # print('stage: ', stage+1)

    ## 한바퀴 회전
    lst.insert(0,lst[-1])
    del lst[-1]
    # if len(robot)>0:
    # robot = [x+1 for x in robot] ## 로봇 위치도 이동
    robot.insert(0,robot[-1])
    del robot[-1]
    # print('회전한 후: ', lst)
    # print('회전한 로봇 위치: ', robot)

    ## 로봇 내리기
    if robot[-1] == 1:

        # print(robot[0], '번째 로봇 내렸다~')
        robot[-1] = 0

    ## 로봇 이동하기, 내릴 수 있으면 바로 내리기
    for i in range(n-1,0,-1):
        if robot[i-1] == 1 and robot[i] == 0 and lst[i] > 0: ## 다음 칸으로 로봇 이동 가능하면
            robot[i] = 1 # 로봇 이동
            robot[i-1] = 0
            lst[i] -= 1 ## 이동한 곳 내구력 1 감소

    if robot[-1] == 1: ## 내리는 위치에 로봇 있으면 즉시 내림
        robot[-1] = 0
        # print('로봇 내렸다!! 이동하면 바로 내려지거든')
    # print('로봇 이동한 후: ', lst)
    # print('이동한 후 로봇 위치: ', robot)

    ## 올리는 곳 내구도 0 아니면 로봇 올림
    if lst[0] > 0:
        lst[0] -= 1
        robot[0] = 1
    # print('로봇 올린 후:', lst)
    # print('올린 로봇 위치:', robot)
    zero_num = lst.count(0)
    stage += 1
    # print(stage, '차 끝, 0의 개수: ',zero_num )

    ## 내구도 0인 칸 k개면 멈춤
    if zero_num >= k:
        break
    # print()
print(stage)
