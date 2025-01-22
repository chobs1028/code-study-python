def solution(N, stages):
    stages.sort()

    stage_dict = {i+1 : 0 for i in range(N)}
    stack = []
    count = 0
    for stage in stages:
        if len(stack):
            if stack[-1] != stage:
                ratio = len(stack) / (len(stages) - count)
                stage_dict[stack[-1]] = ratio
                count += len(stack)
                stack = []
        
        stack.append(stage)

    if len(stack):
        if stack[-1] in stage_dict:
            ratio = len(stack) / (len(stages) - count)
            stage_dict[stack[-1]] = ratio
            
    return [key for key, _ in sorted(stage_dict.items(), key=lambda x:x[1], reverse=True)]

