

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
    InOrder = False
    sumDouble = False
    max_not_in_order = 0
    sum = 0
    for pancake in pancakesList:
        if int(pancake) != num_of_pancakes:
            max_not_in_order = num_of_pancakes;
            InOrder = True
        if InOrder:
            sum += int(pancake)
            if max_not_in_order == int(pancake):
                sumDouble = True
            if sumDouble:
                sum += int(pancake)
        num_of_pancakes -= 1

    return sum


