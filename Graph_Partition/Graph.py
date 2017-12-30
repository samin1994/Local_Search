from Algorithms import simulated_annealing
from random import randint
from copy import deepcopy


class Graph:

    def __init__(self):
        self.graph_matrix = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
        #each partition of graph is either 1 or two and each state is ana array of 1 and 2s which are the positions of each vertex!
        self.CurrentState = []
        self.expanded = 0
        for x in range(12):
            self.CurrentState.append(randint(1, 2))

    def neighbours(self, state):
        neighbours = []
        for j in range(12):
            currentN = deepcopy(state)
            if currentN[j] == 2:
                currentN[j] = 1
            elif currentN == 1:
                currentN[j] = 2
            neighbours.append(currentN)
        return neighbours

    def fitness(self, state):
        fitness_one = 0
        fitness_two = 0
        for m in range(11):
            for n in range(m+1, 12):
                if state[m] != state[n] and self.graph_matrix[m][n] == 1:
                    fitness_one += 1
        counter = 0
        for k in range(12):
            if state[k] == 1:
                counter += 1
        twos = 12 - counter
        fitness_two = abs(twos - counter)
        curr_fitness = fitness_two + fitness_one

        return curr_fitness


if __name__ == '__main__':

    G = Graph()
    print("path to best fitness is : ")
    simulated_annealing(G, 0.2, 'linear')
    print("expanded nodes : ")
    print(G.expanded)



