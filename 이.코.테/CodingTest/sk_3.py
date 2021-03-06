def solution(n, plans, clients):
    result = []
    p = {}
    temp = []
    for pl in plans:
        key = 0
        for idx, t in enumerate(pl.split()):
            if idx == 0:
                p[int(t)] = []
                key = int(t)
            else:
                temp.append(int(t))

        for t in temp:
            p[key].append(t)
    for c in clients:
        c_money = 0
        c_service = []
        for idx, i in enumerate(c.split()):
            if idx == 0:
                c_money = int(i)
            else:
                c_service.append(int(i))
        flag = False
        for index, k in enumerate(p):
            cnt = 0
            if c_money <= k:
                for cs in c_service:
                    if cs in p[k]:
                        cnt += 1
                if cnt == len(c_service):
                    result.append(index + 1)
                    flag = True
                    break
        if not flag:
            result.append(0)
    return result