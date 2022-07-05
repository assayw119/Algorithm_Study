import sys

def change(graph, n):
    if graph[n] == 0:
        graph[n] = 1
    else:
        graph[n] = 0

num = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())
for _ in range(student_num):
    s, switch = map(int, sys.stdin.readline().split())
    if s == 1:
        mok = num // switch
        for i in range(1,mok+1):
            change(status, i * switch-1)
        # print(status)

    else:
        change(status, switch-1)
        for i in range(1,num+1):
            if switch-1-i < 0 or switch-1+i >= num:
                break

            if status[switch-1-i] == status[switch-1+i]:
                change(status, switch-1-i)
                change(status, switch-1+i)
            else:
                break
        # print(status)
for i in range(0, len(status), 20):
    print(*status[i:i+20])

