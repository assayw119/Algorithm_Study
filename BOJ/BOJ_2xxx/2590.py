paper = []
for _ in range(6):
    paper.append(int(input()))

result = paper[5]

# 5번 색종이에 들어갈 1번 색종이
while paper[4] > 0:
    result += 1
    if paper[0] >= 11:
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
        # 4번 색종이 하나에 2번 색종이 5개 들어감
        # 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
        if paper[0] > (5-paper[1])*4:
            paper[0] -= (5-paper[1])*4
        else:
            paper[0] = 0
        paper[1] = 0

    paper[3] -= 1
    # print(paper, result, '4->2')

# 3번 색종이끼리 묶이는 경우
while paper[2] > 0:
    result += 1
    if paper[2] >= 4:
        paper[2] -= 4
    else:
        # 3번 색종이 다 찬후 -> 남은 자리에 들어갈 2번 색종이
        # 남은 3번 색종이가 1개일 경우 -> 2번 색종이 5개 들어감
        # 남은 3번 색종이가 2개일 경우 -> 2번 색종이 3개 들어감
        # 남은 3번 색종이가 3개일 경우 -> 2번 색종이 1개 들어감
        if paper[1] >= 7 - paper[2]*2:
            paper[1] -= 7 - paper[2]*2
            # 3번과 2번 들어가고 남은 자리에 1번
            if paper[0] >= 7:
                paper[0] -= 7
            else:
                paper[0] = 0
        else:
            # 3번과 2번 색종이 다 찬 후 -> 남은 자리에 들어갈 1번 색종이
            if paper[0] >= 36 - paper[2]*9 - paper[1]*4:
                paper[0] -= 36 - paper[2]*9 - paper[1]*4
            else:
                paper[0] = 0
            paper[1] = 0
        paper[2] = 0
    # print(paper, result, '3->3')
# 여기까지 왔는데도 남은 2번 색종이랑 1번 색종이
while paper[1] > 0:
    result += 1
    if paper[1] >= 9:
        paper[1] -= 9
    else:
        # 2번 색종이 다 차고 남은 자리에 들어갈 1번 색종이
        if paper[0] >= 36 - paper[1] * 4:
            paper[0] -= 36 - paper[1] * 4
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

