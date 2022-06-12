def solution(p):
    answer = [0] * len(p)
    return_count = 0
    for _ in range(len(p)):
        return_tf = False
        idx = 0
        min_num = p[return_count]
        for i in range(return_count+1, len(p)):
            if p[i] < min_num:
                min_num = p[i]
                return_tf = True
                idx = i
        if return_tf == True:
            answer[idx] += 1
            answer[return_count] += 1
            p[idx] = p[return_count]
            p[return_count] = min_num
            return_count += 1
        else:
            return_count += 1
    return answer

print(solution([1,2,3,4,5,6,7]))
