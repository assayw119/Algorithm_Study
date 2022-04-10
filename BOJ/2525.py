a, b = input().split()
c = input()

d = int(b) + int(c)
if d >= 60:
    minite = d % 60
    hour = int(a) + d // 60
else:
    minite = int(b) + int(c)
    hour = int(a)
if hour >= 24:
    hour -= 24
print(hour, minite)