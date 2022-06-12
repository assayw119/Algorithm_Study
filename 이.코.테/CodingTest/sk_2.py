def solution(periods, payments, estimates):
    people = [0] * len(periods)

    for i in range(len(periods)):
        next_periods = 0
        next_payments = 0

        # 이번달 vip가 아닌 사람
        if (periods[i] < 24) or (periods[i] < 60 and sum(payments[i]) < 900000) or sum(payments[i]) < 600000:
            # 그 중 다음달 vip가 될 사람 = 1
            next_periods = periods[i] + 1
            next_payments = sum(payments[i][1:]) + estimates[i]
            if (next_periods == 60 and next_payments >= 600000) or (next_periods >= 24 and next_payments >= 900000):
                people[i] = 1

        # 이번달 vip인 사람
        if (periods[i] >= 60 and sum(payments[i]) >= 600000) or (periods[i] >= 24 and sum(payments[i]) >= 900000):
            # 그 중 다음달 vip가 아닌 사람 = 2
            next_periods = periods[i] + 1
            next_payments = sum(payments[i][1:]) + estimates[i]
            if (next_periods < 60 and next_payments < 900000) or next_payments < 600000:
                people[i] = 2
    answer = [people.count(1), people.count(2)]
    return answer

print(solution([20,23,24],[[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],[350000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000]],[100000,100000,100000]))
