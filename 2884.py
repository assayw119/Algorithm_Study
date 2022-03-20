a,b = input().split()
time = int(a)*60 + int(b)
c = time-45
hour = c // 60
minite = c % 60

if hour < 0:
    hour = hour + 24
print(hour, minite)