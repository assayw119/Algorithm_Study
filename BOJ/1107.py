num = int(input())
m = int(input())
if m == 0:
    a = []
else:
    a = list(map(str, input().split()))

def num_posible(k):
    pos = True
    for i in str(k):
        if i in a:
            pos = False
            break
    return pos

for i in range(500001):
    result = 100
    num_big = num + i
    num_small = num - i

    if num_small < 0:
        num_small = 0

    if num_posible(num_big) == False and num_posible(num_small) == False:
        continue
    elif num_posible(num_small) == True:
        result = num_small
        break
    elif num_posible(num_big) == True:
        result = num_big
        break
first_count = abs(result - num) + len(str(result))
second_count = abs(100 - num)
print(min(first_count, second_count))