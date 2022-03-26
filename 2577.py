a = int(input())
b = int(input())
c = int(input())

data = a*b*c

for i in range(10):
    print(str(data).count(str(i)))