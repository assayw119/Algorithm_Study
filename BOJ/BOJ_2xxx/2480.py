a,b,c = input().split()
lst = [int(a),int(b), int(c)]

if a==b==c:
    print(10000+int(a)*1000)
elif a==b or b==c or a==c:
    if lst.count(int(a)) == 2:
        print(1000+int(a)*100)
    else:
        print(1000+int(b)*100)
else:
    print(max(lst)*100)