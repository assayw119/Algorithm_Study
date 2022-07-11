paper = []
for _ in range(6):
    paper.append(int(input()))

result = paper[5]

# 5번 색종이에 들어갈 1번 색종이
while paper[4] > 0:
    result += 1
    if paper[0] > 11:
        paper[0] -= 11
    else:
        paper[0] = 0
    paper[4] -= 1
    # print(paper, result, '5->1')

# 4번 색종이에 들어갈 2번 색종이
while paper[3] > 0:
    result += 1
    if paper[1] > 5:
        paper[1] -= 5
    else:
        # paper[1] = 0
        # 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
        if paper[0] > (5-paper[1])*4:
            paper[0] -= (5-paper[1])*4
        else:
            paper[0] = 0
        paper[1] = 0

        paper[3] -= 1
    # print(paper, result, '4->2')

# 3번 색종이끼리 묶임
while paper[2] > 0:
    result += 1
    if paper[2] > 4:
        paper[2] -= 4
    else:
        # 3번 색종이 다 찬후 -> 남은 자리에 들어갈 2번 색종이
        # 남은 3번 색종이가 1개일 경우 -> 2번 색종이 5개 들어감
        if paper[2] == 1:
            if paper[1] > 5:
                paper[1] -= 5
            else:
                # 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
                if paper[0] > 27 - paper[1] * 4:
                    paper[0] -= 27 - paper[1] * 4
                else:
                    paper[0] = 0
                paper[1] = 0
        # 남은 3번 색종이가 2개일 경우 -> 2번 색종이 3개 들어감
        if paper[2] == 2:
            if paper[1] > 3:
                paper[1] -= 3
            else:
                # 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
                if paper[0] > 18 - paper[1] * 4:
                    paper[0] -= 18 - paper[1] * 4
                else:
                    paper[0] = 0
                paper[1] = 0
        # 남은 3번 색종이가 3개일 경우 -> 2번 색종이 1개 들어감
        if paper[2] == 3:
            if paper[1] > 1:
                paper[1] -= 1
            else:
                # 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
                if paper[0] > 9 - paper[1] * 4:
                    paper[0] -= 9 - paper[1] * 4
                else:
                    paper[0] = 0
                paper[1] = 0
        paper[2] = 0
    # print(paper, result, '3->3')
# 여기까지 왔는데도 남은 2번 색종이랑 1번 색종이
while paper[1] > 0:
    result += 1
    if paper[1] > 9:
        paper[1] -= 9
    else:
        # 2번 색종이 다 차고 남은 자리에 들어갈 1번 색종이
        if paper[0] > 36 - paper[1] * 2:
            paper[0] = 36 - paper[1] * 2
        else:
            paper[0] = 0
        paper[1] = 0
    # print(paper, result, '2->1')

# 여기까지 왔는데도 남은 1번 색종이
while paper[0] > 0:
    result += 1
    if paper[0] > 36:
        paper[0] -= 36
    else:
        paper[0] = 0
print(result)

