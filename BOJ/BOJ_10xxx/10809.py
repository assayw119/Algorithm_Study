from string import ascii_lowercase

alpha = list(ascii_lowercase)

a = input()
for i in ascii_lowercase:
    if i in a:
        print(a.index(i))
    else:
        print(-1)

