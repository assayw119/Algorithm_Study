n,m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

def binary_search(target, start, end, data):
    mid = (start + end) // 2
    if start > end:
        return mid

    total = 0
    for i in data:
        if i <= mid:
            pass
        else:
            total += i - mid
    if total == target:
        # print(start, end, mid, total)
        return mid
    elif total < target:
        # print(start,end, mid, total)
        end = mid - 1
    else:
        # print(start,end, mid, total)
        start = mid + 1

    return binary_search(target, start, end, data)

print(binary_search(m, 0, max(h), h))