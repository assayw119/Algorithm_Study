from copy import deepcopy
n,k = map(int, input().split())
color = [i for i in input()]
color_ = deepcopy(color)
if n>=3:
    for _ in range(k):
        for i in range(n):
            if i == n-1:
                i=i-n
            check_color = [color[i-1], color[i], color[i+1]]
            if len(list(set(check_color))) == 1 or len(list(set(check_color))) == 3:
                color_[i] = 'B'
                # print(color_)
            else:
                red = check_color.count('R')
                green = check_color.count('G')
                blue = check_color.count('B')
                if (red == 2 and green == 1) or (green == 2 and blue == 1) or (blue == 2 and red == 1):
                    color_[i] = 'R'
                else:
                    color_[i] = 'G'
                # print(color_)
else:
    color_ = ['G']*n
print(color_.count('R'),color_.count('G'),color_.count('B'))