name = list(input())


dic = {}
for i in name:
    dic[i] = 0
for i in name:
    dic[i] += 1

lst = sorted(dic.items(), key=lambda x:x[1], reverse=True)

even = True
idx = 0
result = ['0']*len(name)
if len(name)%2 == 0:
    even = False

odd_check = 0
# for i in range(len(lst)):
while 1:

    if even:
        if lst[idx][1] % 2 == 1:
            print("I'm Sorry Hansoo")
            break

        for i in range(lst[idx][1]/2):
            result[i] = lst[idx][0]
            result[-i] = lst[idx][0]
    else:
        r_idx = len(lst)-idx-1
        if lst[r_idx][1]%2 == 1:
            odd_check += 1
            lst[len(lst)//2] = lst[r_idx][0]
            lst[r_idx][1] -= 1

        if odd_check > 1:
            print("I'm Sorry Hansoo")
            break

        for i in range(lst[r_idx][1]/2):
            



    # if not flag:
    #     print("I'm Sorry Hansoo")
    #     break


