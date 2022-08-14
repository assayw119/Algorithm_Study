import sys

input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
for i in range(max(arr)):
    dic[i+1] = 0

result = []
start, end = 0,0
result = 0

while end < n:
    if dic[arr[end]] < k:
        dic[arr[end]] += 1
        end += 1
        # print(dic)
    else:
        dic[arr[start]] -= 1
        start += 1
        # print(dic)
    result = max(end-start, result)

print(result)

