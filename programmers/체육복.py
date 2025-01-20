def solution(n, lost, reserve):
    temp = [1] * (n + 1)
    
    for _lost in lost:
        temp[_lost] = 0
        
    for _reserve in reserve:
        temp[_reserve] += 1
    

    for i in range(1, n+1):
        if temp[i] == 2:
            if i-1 > 0 and temp[i-1] == 0:
                temp[i-1] += 1

            elif i+1 < n+1 and temp[i+1] == 0:
                temp[i+1] += 1
            else:
                continue
                
            temp[i] -= 1
    

    answer = 0
    for i in range(1, len(temp)):
        if temp[i] > 0:
            answer += 1
    
    return answer