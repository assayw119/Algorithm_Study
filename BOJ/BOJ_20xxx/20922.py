import sys

input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
s = [0 for _ in range(max(arr)+1)]
idx_list = {}
s[arr[0]] = 1

result = []
start, end = 0,0
cnt = 0 # 연속 중복 숫자 개수
next_start = 0
while True:
    end += 1
    if end == n - 1:
        result.append(end - start + 1)
        break

    s[arr[end]] += 1
    if s[arr[end]] == k:
        idx_list[arr[end]] = end
        
    if s[arr[end]] > k: # 최대 중복 개수를 넘어섬
        print(start,end)
        if cnt == 0:
            next_start = end-k+1 # 처음 부분이 다음 포인터 이동 시 시작 지점
            idx_list[arr[end]] = end
            print(arr[end])
        cnt += 1

        print(start,end)
        result.append(end-start)
        start = idx_list[arr[end]]+1 # 이전에 그 숫자가 있었던 곳 다음을 출발점으로
        print(start, '!!!', arr[end], idx_list)
        cnt = 0 # 연속 중복 숫자 개수 초기화

    # if cnt > k:
    #     print(start,end)
    #     start = next_start
    #     cnt = 0 # 연속 중복 숫자 개수 초기화

print(result)

