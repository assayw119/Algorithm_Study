import sys

input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate(arr, cnt):
    new_arr = [[0]*m for _ in range(n)]
    for k in range(int(min(n,m)/2)):
        # 윗변 아랫변
        for i in range(1+k,m-k):
            new_arr[k][i-1] = arr[k][i]
            new_arr[n-1-k][i] = arr[n-1-k][i-1]
        # 옆면
        for j in range(1+k,n-k):
            new_arr[j][k] = arr[j-1][k]
            new_arr[j-1][m-1-k] = arr[j][m-1-k]
    if cnt > 1:
        return rotate(new_arr, cnt-1)
    else:
        return new_arr

result = rotate(graph, r)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()