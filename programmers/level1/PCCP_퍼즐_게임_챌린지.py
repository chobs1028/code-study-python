def calculate(level, diffs, times):
    time_cur = 0
    time_prev = 0
    
    for i in range(len(diffs)):

        if diffs[i] > level:
            time_cur += (time_prev + times[i]) * (diffs[i] - level) + times[i]

        else:
            time_cur += times[i]

        time_prev = times[i]
    
    return time_cur

def solution(diffs, times, limit):
    
    start = 1
    end = max(diffs)
    answer = end
    
    while start <= end:
        level = (start + end) // 2

        calculated_time = calculate(level, diffs, times)

        if calculated_time > limit:
            start = level + 1

        else:
            end = level - 1
            answer = level

    return answer
