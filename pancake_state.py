

class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str

        #you may add data stractures to improve the search


    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors = []
        state_len = len(self.state_str)-1
        commas = state_len//2
        for i in range(state_len-commas):
            ps = pancake_state(self.rotate_state(i*2))
            neighbors += [(ps, 0)]
        return neighbors


    #you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str

    def rotate_state(self, index1):
        to_rotate = self.state_str;
        rotated_part =  to_rotate[index1:]
        return  to_rotate[:index1] + rotated_part[::-1]


