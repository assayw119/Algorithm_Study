n = int(input())
price = []
for i in range(n):
    price.append(int(input()))
price.sort(reverse=True)
for i in range(1,n//3+1):
    price[3*i-1] = 0
print(sum(price))