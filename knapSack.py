"""
    Knapsack problem:
        Fitness_function: capacity - sum of (c(i)* s(i))
        Random_selection: using Tournament Selection.
        Reproduce: "Cross over" with random cross over point
        Mutate: Randomly with mutation chance > 0.1

"""


import random
import sys

# Size of initial population filled with some permutation of 0s and 1s
POP_SIZE = 30
# Maximum number of generations the algorithm will run
GEN_MAX = 1000
# Number of Items
ITEMS = 10
# Mutation chance
MUTATION_CHANCE = 0.1


def spawn_individual():
    """
        rtype: list
    """
    return [random.randint(0,1) for x in range (0,ITEMS)]

def spawn_starting_population():
    """
        rtype: list[list]
    """
    return [spawn_individual() for x in range (0,POP_SIZE)]

def isSolution(target,individual, capacity):
    """
        Check if the evolution produce the result?
    """
    _sum = 0
    for i in range(len(target)):
        _sum = _sum + (individual[i]*target[i])
    return _sum == capacity

def fitness_function(item_weights, population, k):
    """
         rtype: int
    """
    _sum = 0
    for i in range(len(item_weights)):
        _sum = _sum + (population[i]*item_weights[i])
    return (k - _sum)*(k- _sum)

def random_selection(item_weights, population, k, parentX):
    """
        rtype: int
        Using tournament selection method
    """
    n = 5
    init_individuals = set()
    rs = sys.maxsize
    i = 0
    while i < n:
        # Randomly pick potential parent. 
        temp = random.randint(0, len(population)-1)
        # print(temp)
        if temp == parentX or temp in init_individuals:
            # To Make sure 1 parent will not get picked twice.. 
            continue
        init_individuals.add(temp)
        i = i+1

    parent = 0
    # Find best parent by passing it to fitness_function
    for i in (init_individuals):
        fit_val = fitness_function(item_weights, population[i], k)
        if fit_val > rs:
            rs = fit_val
            parent = i

    return parent

def crossOver (parentX, parentY, newPopulation):
    """
        Evolution method that produce new children.
        Randomly pick the crossover point. 
    """
    crossover_point = random.randint(0, len(parentX)-1) #randomize the crossover_point
    # print("crossover: ", crossover_point)
    childA, childB = [],[]
    i = 0
    while i < len(parentX):
        if i <= crossover_point:
            childA.append(parentX[i])
            childB.append(parentY[i])
        else:
            childA.append(parentY[i])
            childB.append(parentX[i])
        i = i+1
    if MUTATION_CHANCE > random.random():
        mutate(childA)
        mutate(childB)

    newPopulation.append(childA)
    newPopulation.append(childB)

def mutate(target):
    r = random.randint(0, len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1
   

def runGeneticAlgorithm():

    items = [random.randint(20,100) for x in range (0,ITEMS)]   
    population =  spawn_starting_population()
    capacity = random.randint(100,250) 
    result = []

    found = False
    gen = 0

    print("KnapSack problem: ")
    print("Capacity: ", capacity)
    print("Items: ", items)
    while gen < GEN_MAX:
        newPopulation = []      
        for i in range((int) (len(population)/2)):
            parentX = -1
            parentX = random_selection(items, population, capacity, parentX)
            parentY = random_selection(items, population, capacity, parentX)
            crossOver(population[parentX], population[parentY], newPopulation)
        for individual in newPopulation:
            if (isSolution(individual,items, capacity)):
                # Found solution terminate the algorithm here. 
                found = True
                result = individual
                break
        if (found):
            break
        population = newPopulation  
        gen = gen+1
    
    if len(result) != 0:
        print("Found the result at generation %d," % gen)
        print(result)
    else:
        print("The solution either not exist or the algorithm couldn't find it")

if __name__ == "__main__":
    i = 0
    if len(sys.argv) == 2:
        while i <  int (sys.argv[1]):
            runGeneticAlgorithm()
            print("-------------------------")
            i = i+1
    else:
        print("Usage: py knapSack.py <#number of time you want to run the genetic algorithm >")


    



        






    
    



    




            
