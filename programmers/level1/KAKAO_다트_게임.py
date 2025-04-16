def solution(dartResult):
    bonus = {bonus : idx + 1 for idx, bonus in enumerate(["S", "D", "T"])}
    scores = []
    score = ""

    for result in dartResult:
        if result.isdecimal():
            score += result

        else:

            if len(score):
                scores.append(int(score))
                score = ""

            if result == "*":
                scores[-2:] = list(map(lambda x : x * 2, scores[-2:]))

            elif result == "#":
                scores[-1] = scores[-1] * -1

            else:
                scores[-1] = scores[-1] ** bonus[result]
        
    return sum(scores)