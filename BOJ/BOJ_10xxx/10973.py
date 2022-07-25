n = int(input())
lst = list(map(int, input().split()))

i=n-1
j=n-1
while True:
    if len(lst) == 1 or i == 0:
        print(-1)
        break
    if lst[i-1] > lst[i]: # 왼쪽 > 오른쪽 인 경우
        num = lst[i-1]
        if lst[j] < num: # 오른쪽부터 그 왼쪽 숫자보다 작은 숫자 찾아서 바꾸기
            lst[i-1], lst[j] = lst[j], lst[i-1]
            lst = lst[:i] + sorted(lst[i:], reverse=True) # 왼쪽 숫자 이후 정렬
            for k in lst:
                print(k, end=' ')
            break
        else:
            j -= 1
    else:
        i -= 1
