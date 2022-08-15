import sys
input = sys.stdin.readline

n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))
r.sort(reverse=True)

ans = 0
for i in range(n):
    ans = max(ans, r[i] * (i+1))
print(ans)