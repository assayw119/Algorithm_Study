n, k = map(int,input().split())
s = list(map(int, input().split()))

start, end = 0,0
max_even = 0
while end < n:
    even = 0
    odd = 0
    for i in range(start, end+1):
        if s[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    max_even = max(max_even, even)
    end += 1
    if end-start > k + even:
        start += 1
print(max_even)
