def solution(n, times):
    times.sort()
    start = min(times)
    end = max(times) * n

    while start <= end:
        middle = (start + end) // 2
        num_sum = 0
        for i in times:
            num_sum += middle // i

        if num_sum >= n:
            end = middle - 1
            answer = middle
        else:
            start = middle + 1

    return answer