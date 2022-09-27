def solution(tickets):

    answer = []

    t = {} # {출발지 : 도착지}
    for ticket in tickets:
        if ticket[0] in t.keys():
            t[ticket[0]].append(ticket[1])
            # 도착지 알파벳 순 정렬
            t[ticket[0]] = sorted(t[ticket[0]])
        else:
            t[ticket[0]] = [ticket[1]]
    print(t)
    startpoint = 'ICN'
    answer = [startpoint]
    while 1:

        new_start = t[startpoint][0]
        # print(new_start)
        del t[startpoint][0]

        startpoint = new_start
        answer.append(startpoint)
        if len(answer) == len(tickets) + 1:
            break
        print(t)
        print(answer)
        print()

    return answer



# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))
# print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))



def solution(ticktes):
    start = ticktes.keys()
    end = ticktes.values()


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)