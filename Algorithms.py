from copy import deepcopy
from random import randint

import sys
sys.setrecursionlimit(100000)
bestFitness = 0


def simulated_annealing(problem, cooling_rate, strategy):

    temperature = 1000
    while temperature > 1:
        newState = []
        for i in range(12):
            newState.append(randint(1, 2))

        decision_num = randint(0, 1000)

        if problem.fitness(newState) >= problem.fitness(problem.CurrentState):
            if decision_num < temperature:
                problem.CurrentState = deepcopy(newState)
                problem.expanded += 1
            else:
                pass
        elif problem.fitness(newState) < problem.fitness(problem.CurrentState):
            if decision_num > temperature:
                problem.CurrentState = deepcopy(newState)
                problem.expanded += 1
            else:
                pass

        for h in range(12):
            print(problem.CurrentState[h])
        print('\n')

        if strategy == 'linear':
            temperature -= cooling_rate
        elif strategy == 'exponential':
            temperature = (1-cooling_rate) * temperature

    print("best fitness is : ")
    print(problem.fitness(problem.CurrentState))

def hill_climbing(problem, random_restart, optType, totalFitness, searchType):

    min_res = 100
    print("path to best state is : ")
    for i in range(random_restart):
        for col in range(8):
            problem.CurrentState[col] = randint(0, 7)
        result = solver(problem, optType, totalFitness, searchType)
        if result == 0:
            break
        if result < min_res:
            min_res = result
    print("The best fitness is : ")
    print(min_res)


def solver(problem, optType, totalFitness, searchType):
    current = deepcopy(problem.CurrentState)
    neighbours = problem.neighbours(current)
    minimum = 100000
    bestState = []

    while True:

        currentFitness = problem.fitness(problem.CurrentState)

        if searchType == 'simple':

            isBetterFound = False
            for f in neighbours:
                nf = problem.fitness(f)
                if nf < currentFitness:
                    if nf < minimum:
                        minimum = nf
                        bestState = deepcopy(f)
                        isBetterFound = True

            if isBetterFound:
                for i in range(8):
                    print(bestState[i])
                print('\n')
                problem.CurrentState = deepcopy(bestState)
                problem.path.append(problem.CurrentState)
                return problem.fitness(problem.CurrentState)

            else:
                return problem.fitness(problem.CurrentState)

        if searchType == 'stochastic':

            better = []
            isBetterFound = False
            for n in neighbours:
                nf = problem.fitness(n)
                if nf < currentFitness:
                    better.append(n)
                    isBetterFound = True

            if isBetterFound:
                random_n = randint(0, len(better) - 1)
                problem.CurrentState = deepcopy(better[random_n])
                for i in range(8):
                    print(better[random_n][i])
                print('\n')

            else:
                return problem.fitness(problem.CurrentState)








