def solution(queue1, queue2):
    if sum(queue1)>sum(queue2):
        return popinsert(queue2,queue1)
    elif sum(queue2)>sum(queue1):
        return popinsert(queue1, queue2)
    else:
        return -1

def popinsert(q1, q2): # sum(q1) < sum(q2)
    answer = 0
    while sum(q1)<sum(q2):
        q1.append(q2[0])
        del q2[0]
        answer += 1

    for i in range(1,len(q1)):
        if sum(q1[:i])+sum(q2) < sum(q1[i:]):
            answer += 1
            continue
        elif sum(q1[:i]) + sum(q2) == sum(q1[i:]):
            answer += 1
            return answer
        else:
            q1.append(q2[0])
            del q2[0]
        # if i == len(q1)-1:
        return -1
a = [3,2,7,2]
b = [4,6,5,1]
print(solution(a,b))