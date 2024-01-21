

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
    sum = 0
    for pancake in pancakesList:
        if int(pancake) != num_of_pancakes:
            InOrder = True
        if InOrder:
            sum += int(pancake)
        num_of_pancakes -= 1

    return sum + 1


