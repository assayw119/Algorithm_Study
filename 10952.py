while True:
    a, b = input().split()
    num_a = int(a)
    num_b = int(b)

    if num_a==0 and num_b==0:
        break
    print(num_a + num_b)
