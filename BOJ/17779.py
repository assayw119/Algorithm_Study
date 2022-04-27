n = int(input())
dp = []
for i in range(n):
    array = list(map(int, input().split()))
    dp.append(array)

def_list = []
# 만들 수 있는 사각형 한 변의 길이(기울기 양수) => 1 ~ n-1
for i in range(1, n-1):
    # 만들 수 있는 사각형 한 변의 길이(기울기 음수) => 1 ~ n-1
    for j in range(1, n-1):
        # 위 꼭지점이 있을 수 있는 x 위치 => 0 ~ n-2
        for x in range(n-2):
            # 위 꼭지점이 있을 수 있는 y 위치 => 1 ~ n-1
            for y in range(1,n-1):
                # 왼쪽 y값이 0보다 작은 경우, 오른쪽 y값이 n보다 크거나 같은 경우, 아래 x값이 n보다 크거나 같은 경우 제외
                if y-i < 0 or y+j >= n or x+i+j >= n:
                    continue
                # print('i,j: ', i,j)
                # print('x,y: ', x,y)
                # 변의 길이가 i, j이고, 위 꼭지점이 (x,y)일 때
                top_x, top_y = x, y
                left_x, left_y = x+i, y-i
                right_x, right_y = x+j, y+j
                bottom_x, bottom_y = right_x+i, right_y-i

                s1 = [] # 왼쪽 위
                s2 = [] # 오른쪽 위
                s3 = [] # 왼쪽 아래
                s4 = [] # 오른쪽 아래
                s5 = [] # 가운데

                for x_ in range(n):
                    for y_ in range(n):
                        # s로 빠지는 곳 False 처리
                        tf = [[True] * n] * n

                        # s1, s4
                        for a in range(i):
                            val1_x = top_x + a
                            val1_y = top_y - a
                            if x_ == val1_x and y_ < val1_y:
                                s1.append(dp[x_][y_])
                                tf[x_][y_] = False
                            val4_x = bottom_x - a
                            val4_y = bottom_y + a
                            if x_ == val4_x and y_ > val4_y:
                                s4.append(dp[x_][y_])
                                tf[x_][y_] = False
                        # s3, s2
                        for b in range(j):
                            val3_x = left_x + b
                            val3_y = left_y + b
                            if x_ == val3_x and y_ < val3_y:
                                s3.append(dp[x_][y_])
                                tf[x_][y_] = False
                            val2_x = right_x - b
                            val2_y = right_y - b
                            if x_ == val2_x and y_ > val2_y:
                                s2.append(dp[x_][y_])
                                tf[x_][y_] = False
                        # s1, s4 남은 부분
                        if x_ < top_x and y_ <= top_y:
                            s1.append(dp[x_][y_])
                            tf[x_][y_] = False
                        elif x_ > bottom_x and y_ >= bottom_y:
                            s4.append(dp[x_][y_])
                            tf[x_][y_] = False
                        # s3, s2 남은 부분
                        elif x_ >= bottom_x and y_ < bottom_y:
                            s3.append(dp[x_][y_])
                            tf[x_][y_] = False
                        elif x_ <= top_x and y_ > top_y:
                            s2.append(dp[x_][y_])
                            tf[x_][y_] = False
                        # s5 : 방문 안한 곳
                        if tf[x_][y_] == True:
                            s5.append(dp[x_][y_])
                # print(i,j,x,y,'/////', sum(s1), sum(s2), sum(s3), sum(s4), sum(s5), tf)
                max_sum = max(sum(s1), sum(s2), sum(s3), sum(s4), sum(s5))
                min_sum = min(sum(s1), sum(s2), sum(s3), sum(s4), sum(s5))
                def_list.append(max_sum - min_sum)
print(min(def_list))