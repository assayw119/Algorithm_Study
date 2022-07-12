n,k = map(int, input().split())
color = [i for i in input()]
def check(color):
    color_ = color.copy()
    for i in range(n):
        now = i
        back = i-1
        front = i+1
        if front == n:
            front = 0
        check_color = [color_[back], color_[now], color_[front]]
        if len(list(set(check_color))) == 1 or len(list(set(check_color))) == 3:
            color[now] = 'B'
            # print(color_)
        else:
            red = check_color.count('R')
            green = check_color.count('G')
            blue = check_color.count('B')
            if (red == 2 and green == 1) or (green == 2 and blue == 1) or (blue == 2 and red == 1):
                color[now] = 'R'
            else:
                color[now] = 'G'
            # print(color_)
for _ in range(k):
    check(color)
print(color.count('R'),color.count('G'),color.count('B'))