n = int(input())
m = int(input())
s = list(input())

k = 2*n+1
result = 0
def check(x):
    global s, n, result, k

    # print(s[x:x+k], x)
    if s[x:x+k] == ['I'] + ['O', 'I']*n:
        result += 1

for i in range(m-k):
    check(i)
print(result)
