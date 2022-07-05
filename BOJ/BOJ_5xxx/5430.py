import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline()[1:-2]
    # print(x)
    if n != 0:
        x = list(map(int, x.split(',')))
    else:
        x = []

    q = deque(x)
    reverse = 0
    error = False
    for i in p:
        if i == 'R':
            if reverse == 1:
                reverse = 0
            else:
                reverse = 1
        elif i == 'D':
            if len(q) == 0:
                error = True
                break
            if reverse == 0:
                q.popleft()
            else:
                q.pop()

    if error:
        print('error')
    else:
        if reverse == 0:
            result = list(q)
        else:
            result = list(reversed(list(q)))
        print(str(result).replace(' ', ''))
