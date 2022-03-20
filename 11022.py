a = int(input())

for i in range(a):
    b, c = input().split()
    print('Case #{}: {} + {} = {}'.format(i+1, b, c, int(b)+int(c)))