from collections import Counter
n = int(input())

for _ in range(n):

    clo = int(input())
    clothes = []
    dic = {}
    for _ in range(clo):
        cloth, label = map(str, input().split())
        clothes.append(label)
    count_clothes = Counter(clothes).values()
    count = list(count_clothes)

    result = 1
    for i in range(len(count)):
        result *= (count[i]+1)
    print(result-1)
