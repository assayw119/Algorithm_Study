a = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = a
for i in range(a):
    # 총감독관 배치
    student[i] -= b
    if student[i] < 0:
        student[i] = 0

    # 부감독관 배치
    if student[i] % c != 0:
        cnt += student[i] // c + 1
    else:
        cnt += student[i] // c
print(cnt)