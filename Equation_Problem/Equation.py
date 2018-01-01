from Algorithms import genetic_algorithm
from random import randint

# finding the optimum solution (the best) to this equation : x + 2y + 3w + 4z = 30


class Equation:

    def __init__(self):

        self.bestFitness = 0

    # best fitness is the solution and is equal to 1.0
    def fitness(self, member):
        s = 0
        s += member[0] + 2*member[1] + 3*member[2] + 4*member[3]
        d = 30 - s
        diff = abs(d)
        fitness_num = 1/(1 + diff)
        return fitness_num

    def crossover(self, state1, state2):
        state3 = []
        gen_num = randint(0, 2)
        for i in range(gen_num + 1):
            state3.append(state1[i])
        for j in range(gen_num + 1, 4):
            state3.append(state2[j])

        return state3


if __name__ == '__main__':

    eq = Equation()
    genetic_algorithm(eq, 4, 30, 10, 0.2, 0.1)
