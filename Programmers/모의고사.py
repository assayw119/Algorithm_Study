def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    idx = 0
    ans = [0,0,0]
    while 1:

        if s1[idx%5] == answers[idx]:
            ans[0] += 1
        if s2[idx%8] == answers[idx]:
            ans[1] += 1
        if s3[idx%10] == answers[idx]:
            ans[2] += 1
        idx += 1
        if idx == len(answers):
            break

    for i,v in enumerate(ans):
        if v == max(ans):
            answer.append(i+1)

    return answer

a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(solution(a))