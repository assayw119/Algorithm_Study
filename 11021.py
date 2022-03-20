a = int(input())

for i in range(a):
    b, c = input().split()
    print('Case #{}: {}'.format(i+1,int(b)+int(c)))