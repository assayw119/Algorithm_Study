import sys
input = sys.stdin.readline

n = int(input())

input_car = [input() for _ in range(n)]
output_car = [input() for _ in range(n)]

result = 0
for i in range(1,n):
    input_front = input_car[:i]
    output_front = output_car[:output_car.index(input_car[i])]
    if set(input_front)&set(output_front) != set(input_front):
        result += 1
print(result)