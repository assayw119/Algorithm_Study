import sys
input = sys.stdin.readline

n,m = map(int, input().split())
x,y,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

turn_cnt = 0 # 회전횟수 (4번 넘으면 초기화)
total_cnt = 1
graph[x][y] = 2 # 처음 위치 청소

def turn(x,y,d):
    if d == 0: # 북
        nx,ny = x, y-1
    elif d == 1: # 동
        nx,ny = x-1, y
    elif d == 2: # 남
        nx,ny = x, y+1
    else: # 서
        nx,ny = x+1, y
    return nx,ny

while 1:

    nx,ny = turn(x,y,d)

    direction = [0,1,2,3]

    # 청소할 수 있는 경우
    if graph[nx][ny] == 0:
        d = direction[d-1] # 그 방향으로 회전
        graph[nx][ny] = 2 # 청소상태로 변경
        x,y = nx,ny # 전진
        turn_cnt = 0 # 회전 횟수 초기화
        total_cnt += 1
    else:
        d = direction[d-1] # 그 방향으로 회전
        turn_cnt += 1
        if turn_cnt == 4: # 한곳에서 회전 4번하면
            turn_cnt = 0
            x,y = turn(x,y,direction[d-1]) # 후진

            # 후진할 곳이 없으면 break
            if x<0 or x>=n or y<0 or y>=m or graph[x][y] == 1:
                break
    # print(x, y)

print(total_cnt)
