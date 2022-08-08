import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n == 0:
        break

    pages = input().split(',')
    result = 0
    visited = [0 for _ in range(n+1)]
    for page in pages:
        if '-' in page:
            a,b = page.split('-')
            if int(b) > n:
                b = n
            if int(a) <= int(b):
                for i in range(int(a),int(b)+1):
                    visited[i] = 1
        else:
            if int(page)<=n:
                visited[int(page)] = 1
    print(sum(visited))