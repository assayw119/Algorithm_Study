from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def close(graph, direction,x,y):
    # 가장 가까운 숫자 위치 반납
    if direction == 'up':
        for i in range(1,x+1):
            if graph[x-i][y] == 0:
                continue
            return x-i
        return 'nothing' # 위에 있는게 모두 0인 경우
    if direction == 'down':
        for i in range(1,n-x):
            if graph[x+i][y] == 0:
                continue
            return x+i
        return 'nothing' # 아래에 있는게 모두 0인 경우
    if direction == 'left':
        for i in range(1,y+1):
            if graph[x][y-i] == 0:
                continue
            return y-i
        return 'nothing' # 왼쪽에 있는게 모두 0인 경우
    if direction == 'right':
        for i in range(1,n-y):
            if graph[x][y+i] == 0:
                continue
            return y+i
        return 'nothing' # 오른쪽에 있는게 모두 0인 경우

def up(graph):
    changed = [[0] * n for _ in range(n)]
    for i in range(1,n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            close_x = close(graph, 'up', i, j)
            # print(close_x)
            if close_x == 'nothing': # 위에 아무것도 없을 때
                graph[0][j] = graph[i][j]
                graph[i][j] = 0
            elif graph[i][j] == graph[close_x][j] and changed[close_x][j] == 0: # 가장 가까이 있는 숫자가 같을 때
                graph[close_x][j] *= 2
                graph[i][j] = 0
                changed[close_x][j] = 1
            else: # 가까이 있는 숫자가 다를 때
                if i - close_x > 1:
                    graph[close_x + 1][j] = graph[i][j]
                    graph[i][j] = 0
    return graph


def down(graph):
    changed = [[0] * n for _ in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            close_x = close(graph, 'down', i, j)
            # print(close_x)
            if close_x == 'nothing': # 아래에 아무것도 없을 때
                graph[n-1][j] = graph[i][j]
                graph[i][j] = 0
            elif graph[i][j] == graph[close_x][j] and changed[close_x][j] == 0: # 가장 가까이 있는 숫자가 같을 때
                graph[close_x][j] *= 2
                graph[i][j] = 0
                changed[close_x][j] = 1
            else: # 가까이 있는 숫자가 다를 때
                if close_x - i > 1:
                    graph[close_x - 1][j] = graph[i][j]
                    graph[i][j] = 0
    return graph


def left(graph):
    changed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(1,n):
            if graph[i][j] == 0:
                continue
            close_y = close(graph, 'left', i, j)
            # print(close_x)
            if close_y == 'nothing': # 왼쪽에 아무것도 없을 때
                graph[i][0] = graph[i][j]
                graph[i][j] = 0
            elif graph[i][j] == graph[i][close_y] and changed[i][close_y] == 0: # 가장 가까이 있는 숫자가 같을 때
                graph[i][close_y] *= 2
                graph[i][j] = 0
                changed[i][close_y] = 1
            else: # 가까이 있는 숫자가 다를 때
                if j - close_y > 1:
                    graph[i][close_y + 1] = graph[i][j]
                    graph[i][j] = 0
    return graph

def right(graph):
    changed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n-2,-1,-1):
            if graph[i][j] == 0:
                continue
            close_y = close(graph, 'right', i, j)
            # print(close_x)
            if close_y == 'nothing':  # 오른쪽에 아무것도 없을 때
                graph[i][n-1] = graph[i][j]
                graph[i][j] = 0
            elif graph[i][j] == graph[i][close_y] and changed[i][close_y] == 0:  # 가장 가까이 있는 숫자가 같을 때
                graph[i][close_y] *= 2
                graph[i][j] = 0
                changed[i][close_y] = 1
            else:  # 가까이 있는 숫자가 다를 때
                if close_y - j > 1:
                    graph[i][close_y - 1] = graph[i][j]
                    graph[i][j] = 0
    return graph

def test(k, graph):
    if k == 0:
        return up(graph)
    elif k == 1:
        return down(graph)
    elif k == 2:
        return left(graph)
    elif k == 3:
        return right(graph)

max_result = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    arr2 = deepcopy(arr)
                    result_arr = test(a, test(b, test(c, test(d, test(e, arr2)))))
                    max_result = max(max(map(max, result_arr)), max_result)

print(max_result)
