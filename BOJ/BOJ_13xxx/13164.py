n,k = map(int, input().split())
h = list(map(int,input().split()))
sub = []
for i in range(1,len(h)):
    sub.append(h[i]-h[i-1])
sub.sort()

print(sum(sub[:n-k]))
