n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0
num = 0
while num <= len(p):
    for i in range(num):
        result += p[i]
    num += 1
print(result)