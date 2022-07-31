import re

sik = input()
sign = []

k = re.split(r"\+|\-", sik)
result = int(k[0])

if len(k) != 1:
    i = 0
    for a in sik:
        if a == '+':
            sign.append('+')
        elif a == '-':
            sign.append('-')
    while True:
        if sign[i] == '+':
            i += 1
            result += int(k[i])
            if i == len(sign):
                break
        elif sign[i] == '-':
            for num in k[i+1:]:
                result -= int(num)
            break
print(result)