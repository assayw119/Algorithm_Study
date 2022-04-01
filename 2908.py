a,b = input().split()

a = int(a[2])*100 + int(a[1])*10 + int(a[0])
b = int(b[2])*100 + int(b[1])*10 + int(b[0])
print(max(a,b))