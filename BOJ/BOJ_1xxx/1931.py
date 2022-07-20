import sys
n = int(sys.stdin.readline())
time = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    time.append((a,b))
time.sort(key=lambda x:(x[1],x[0]))

result = 1
b_start, b_end = time[0]
for i in range(1,n):
    start, end = time[i]
    if b_start == start and b_end > start:
        continue
    if b_end > start:
        continue
    b_start, b_end = time[i]
    result += 1

print(result)