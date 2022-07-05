n, k = map(int,input().split())
s = list(map(int, input().split()))

# 홀수는 1로, 짝수는 2로 바꿈
for i in range(len(s)):
    if s[i] % 2 == 1:
        s[i] = 1
    else:
        s[i] = 2

max_num = 0
# 맨앞과 맨뒤에 1을 추가함
s = [1] + s + [1]
# print(s)

# 추가한 1 제외 기존 리스트만 판단
for start in range(1,len(s)-1):
    if s[start:].count(1)-1 < k:
        break
    end = start
    while True:
        if s[start:end].count(1) == k:
            break
        if end >= len(s)-1:
            break
        end += 1  # 끝점 포함시킴

    # start += 1
    # end += 1
    # print(start, end)

    # 시작점 이전 가장 가까운 1값 찾음
    for i in range(1,len(s[:start])):
        if s[start-i] == 1:
            start = start - i
            break
    # 끝점 이후 가장 가까운 1값 찾음
    for j in range(1,len(s[end:])):
        if s[end+j] == 1:
            end = end + j
            break
    # print(start, end)
    # print()
    # (시작점 이전 1값 ~ 끝점 이후 1값) 중 2의 개수
    if max_num < s[start:end].count(2):
        max_num = s[start:end].count(2)
print(max_num)