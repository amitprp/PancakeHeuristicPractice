

def base_heuristic(_pancake_state):
    pancakesList = _pancake_state.get_state_str().split(',')
    num_of_pancakes = len(pancakesList)
    InOrder = False
    sum = 0
    for pancake in pancakesList:
        if int(pancake) != num_of_pancakes:
            InOrder = True
        if InOrder:
            sum += int(pancake)
        num_of_pancakes -= 1

    return sum

def advanced_heuristic(_pancake_state):
    pancakesList = _pancake_state.get_state_str().split(',')
    num_of_pancakes = len(pancakesList)
    sum1 = 0
    sum2 = 0
    InOrder = False
    first_time = True
    for i in range(len(pancakesList)-1):
        if int(pancakesList[i]) != num_of_pancakes:
            InOrder = True
        if int(pancakesList[i]) + 1 == int(pancakesList[i+1]) and InOrder:
            if first_time:
                sum1 += (int(pancakesList[i]) + int(pancakesList[i+1]))*0.5
                first_time = False
            else:
                sum1 += int(pancakesList[i+1])*0.5
        elif InOrder:
            first_time = True
            sum1 += int(pancakesList[i])*2
        if int(pancakesList[i]) - 1 == int(pancakesList[i + 1]) and InOrder:
            if first_time:
                sum2 += int(pancakesList[i]) + int(pancakesList[i + 1])*0.5
                first_time = False
            else:
                sum2 += int(pancakesList[i + 1])*0.5
        elif InOrder:
            first_time = True
            sum2 += int(pancakesList[i]) * 2
        num_of_pancakes -= 1
    return min(sum1, sum2)

