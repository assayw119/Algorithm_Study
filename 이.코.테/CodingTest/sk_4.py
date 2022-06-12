from collections import deque
import heapq

def solution(grid, k):
    def bfs(start, k):
        graph = [list(g) for g in grid]
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        N = len(graph)
        M = len(graph[0])
        visited1 = [[False]*M for _ in range(N)]
        visited1[0][0] = True
        q1 = []
        heapq.heappush(q1, [0, start[0], start[1]])
        while q1:
            # print(q1)
            visited2 = [[False]*M for _ in range(N)]
            ya_young, a, b = heapq.heappop(q1)
            visited2[a][b] = True
            q2 = deque()
            q2.append([a, b])
            while q2:
                # print(q2)
                a2, b2 = q2.popleft()
                # print(a2, b2)
                for i in range(4):
                    nx = a2 + dx[i]
                    ny = b2 + dy[i]
                    if nx >= 0 and ny >= 0 and nx < N and ny < M:
                        if not visited2[nx][ny] and graph[nx][ny] in [".", "F"]:
                            visited2[nx][ny] = True
                            if abs(a-nx) + abs(b-ny) <= k:
                                q2.append([nx, ny])
                                if graph[nx][ny] == "." and not visited1[nx][ny]:
                                    visited1[nx][ny] = True
                                    q1.append([ya_young + 1, nx, ny])
                                    if [nx,ny] == [N-1,M-1]:
                                        return ya_young

    result = bfs([0,0],k)
    # print(result)
    return result
# print(solution(["..FF", "###F", "###."], 4))
print(solution(["..FF", "###F", "###."], 5))