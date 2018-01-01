from copy import deepcopy
from random import *
from math import ceil

# implementation of local searches like hill climbing and an implementation of genetic algorithm.

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
        result = hill_climber(problem, optType, totalFitness, searchType)
        if result == 0:
            break
        if result < min_res:
            min_res = result
    print("The best fitness is : ")
    print(min_res)


def hill_climber(problem, optType, totalFitness, searchType):
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


def genetic_algorithm(problem, gen_num, population_num, generation_num, crossover_rate, mutation_rate):

    # first population
    population = []
    for p in range(population_num):
        member = []
        for g in range(gen_num):
            member.append(randint(0, 10))
        population.append(member)
        # print(problem.fitness(member))

    count = 0
    while count != generation_num:

        # Round Wheel Selection
        total = 0
        for m in range(population_num):
            member_f = problem.fitness(population[m])
            total += member_f

        member_prob = []
        for t in range(population_num):
            member_prob.append((problem.fitness(population[t])) / total)

        fitness_sum = []
        sum_of_fitness = 0
        for n in range(population_num):
            sum_of_fitness += member_prob[n]
            fitness_sum.append(sum_of_fitness)

        counter = 0
        selected_population = []
        while counter != population_num:
            selector = uniform(0, 1)
            for k in range(len(fitness_sum)):
                if (selector >= fitness_sum[k]) and (selector <= fitness_sum[k+1]):
                    selected_population.append(population[k+1])
                    break
            counter += 1

        # parent selection
        p = 0
        parents = []
        positions = []
        while p < len(selected_population):
            r = uniform(0, 1)
            if r < crossover_rate:
                parents.append(selected_population[p])
                positions.append(p)
            p += 1

        # doing crossover!
        for x in range(len(parents) - 1):
            for y in range(x + 1, len(parents)):
                child = problem.crossover(parents[x], parents[y])
                selected_population[positions[x]] = deepcopy(child)

        # mutation
        total_gen = population_num * gen_num
        mutation_num = int(ceil(mutation_rate * population_num))
        for m in range(mutation_num):
            mutation_chance = randint(1, total_gen)
            if mutation_chance / 4 == 0:
                member_num = 0
            else:
                member_num = int(mutation_chance / 4) - 1
            if mutation_chance % 4 == 0:
                gen = 3
            else:
                gen = int(mutation_chance % 4) - 1
            selected_population[member_num][gen] = randint(0, 10)

        # generation counter
        count += 1

    # selecting best member after some generations!
    best_f = 0.0
    best = []
    for c in range(population_num):
        mem_f = problem.fitness(selected_population[c])
        if mem_f > best_f:
            best_f = mem_f
            best = deepcopy(selected_population[c])
    print("best member in 10 generations is : ")
    for t in range(4):
        print(best[t])
    print("best f is :")
    print(best_f)







    





