import random
import time


from search import search
from pancake_state import pancake_state
from heuristics import *


if __name__ == '__main__':
     # goal_state = "6,5,4,3,2,1"
     # pancake_input = "6,4,2,5,3,1"
     # pancake_state = pancake_state(pancake_input)
     # search_result = search(pancake_state, base_heuristic, goal_state)
     for i in range(100):
         # numbers = [3, 1, 4, 2]
         # goal_state = "4,3,2,1"
         numbers = list(range(9, 0, -1))
         goal_state = ','.join(map(str, numbers))
         random.shuffle(numbers)
         print(numbers)
         start_string = ','.join(map(str, numbers))
         start_state = pancake_state(start_string)
         start_time = time.time()
         search_result = search(start_state, base_heuristic, goal_state)
         end_time = time.time()
         print(end_time - start_time)
         start_time = time.time()
         search_result = search(start_state, advanced_heuristic, goal_state)
         end_time = time.time()
         print(end_time - start_time)

    # [2, 5, 9, 8, 7, 3, 4, 1, 6], 2, 5, 6, 1, 4, 3, 7, 8, 9,] 9, 8, 7, 3, 4, 1, 6, 5, 2,] 9, 8, 7, 3, 4, 1, 2, 5, 6, ]9, 8,
    #  7, 6, 5, 2, 1, 4, 3], 9, 8, 7, 6, 5, 2, 1, 3, 4], 9, 8, 7, 6, 5, 4, 3, 1, 2,] 9, 8, 7, 6, 5, 4, 3, 2, 1]