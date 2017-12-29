from Algorithms import hill_climbing
from copy import deepcopy


class Queen:

    def __init__(self, initial):
        self.visited = 0
        self.expanded = 0
        self.path = [initial]
        self.CurrentNeighbours = []
        self.CurrentState = initial
        # state is an 8 digit array of each queen's row and first row is 0
        self.CurrentFitness = 28
        self.bestFitness = 0
        self.threats = 0

    def neighbours(self, state):
        for i in range(8):
            for j in range(8):
                if state[i] != j:
                    self.visited += 1
                    temp_state = deepcopy(state)
                    temp_state[i] = j
                    self.CurrentNeighbours.append(temp_state)
        return self.CurrentNeighbours

    def fitness(self, state):
        self.threats = 0
        for i in range(7):
            for j in range(i + 1, 8):
                if state[i] == state[j]:
                    self.threats += 1

        for col in range(7):
            for o in range(1, (6-col) + 2):
                if state[col + o] == (state[col] + o) or state[col + o] == (state[col] - o):
                    self.threats += 1
        return self.threats

    def final_result(self):
        print('Algorithm : simple hill climbing ' + 'path : ')


if __name__ == '__main__':
    first = [2, 1, 0, 0, 3, 7, 5, 7]
    q = Queen(first)
    hill_climbing(q, 50, 'min', 0, 'stochastic')



