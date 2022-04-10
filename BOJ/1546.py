a = int(input())
b = list(map(int, input().split()))

result = 0
for i in range(a):
    result += b[i]/max(b)*100/a
print(result)
