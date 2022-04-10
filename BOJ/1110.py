a = int(input())

count = 0
new_a = a

while True:
    if new_a < 10:
        new_a *= 11
        count += 1
        # print(new_a)
    else:
        q1 = list(map(int, str(new_a)))[0]
        q2 = list(map(int, str(new_a)))[1]
        new_a = (q1+q2)%10+10*q2
        # print(new_a)
        count += 1
    if a == new_a:
        break

print(count)