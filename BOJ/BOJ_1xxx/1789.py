import math
s = int(input())
for i in range(s,0,-1):
    if i <= 2:
        print(1)
        break
    if int(math.sqrt(1+8*i)) == math.sqrt(1+8*i):
        max_num = int((-1+math.sqrt(1+8*i))/2)
        print(max_num)
        break