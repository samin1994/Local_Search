
class Queen:

    def __init__(self, init):
        self.state = init
        self.visited = 0
        self.expanded = 0
        self.path = [[]]
        self.currentNeighbours = [[]]
        self.currentFitness = 28

    def neighbours(self, state):
        for i in range(1, 8):
            for j in range(1, 8):
                if state[i] == j:
                    pass
                else:
                    self.visited += 1
                    state[i] = j
                    self.currentNeighbours.append(state)
        return self.currentNeighbours

    def fitness(self, state):
        threats = 0

        for i in range(1, 7):
            for j in range(i, 8):
                if state[i] == state[j]:
                    threats += 1

        for col in range(1, 8):
            for o in range(1, (6-col) + 2):
                if state[col + o] == state[col] + o or state[col + o] == state[col] - o:
                    threats += 1
        return threats




