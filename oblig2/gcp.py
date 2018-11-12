import numpy as np
import random


def calculateFitness(e):
    fitness = 0
    for i in range(len(e)):
        for j in range(len(e)):
            if (graph[i][j] == 1):
                if (e[i] == e[j]):
                    fitness += 1
    
    return fitness


def generateGraph(numberOfNodes, graph):
    for i in range(0, numberOfNodes):
        rand = random.randint(1, 3)
        for j in range(rand):
            neighbour = random.randint(0, numberOfNodes-1)
            while (neighbour == i):
                neighbour = random.randint(0, numberOfNodes-1)
            graph[i][neighbour] = 1
            graph[neighbour][i] = 1


def generateInitPopulation(numberOfNodes, populationSize):
    population = []
    for i in range(populationSize):
        nChromosone = np.zeros(numberOfNodes, dtype='int32')
        for j in range(numberOfNodes):
            color = random.randint(0, 2)
            nChromosone[j] = color
        population.append(nChromosone)
    
    return population


def makePairs(population):
    pairs = []

    while (len(pairs) < len(population)):
        node1 = random.randint(0, len(population) - 1)
        node2 = random.randint(0, len(population) - 1)
        while (node1 in pairs):
            node1 = random.randint(0, len(population) - 1)

        pairs.append(node1)        

        while (node2 in pairs):
            node2 = random.randint(0, len(population) - 1)
            
        pairs.append(node2)

    return pairs


def mutate(chromosome):
    index = random.randint(0, len(chromosome) - 1)
    value = random.randint(0, 2)

    chromosome[index] = value


def onePoint(population):
    pairs = makePairs(population)

    for i in range(len(pairs)):
        if (i >= len(pairs) / 2):
            break
        swapIndex = random.randint(0, len(population[0]) - 1)
        child1 = np.array(population[pairs[i*2]], dtype='int32', copy=True)
        child2 = np.array(population[pairs[i*2 + 1]], dtype='int32', copy=True)
        new1 = child1[swapIndex]
        new2 = child2[swapIndex]

        child1[swapIndex] = new2
        child2[swapIndex] = new1

        rand = random.uniform(0, 1)
        if (rand < 0.1):
            mutate(child1)
        
        rand = random.uniform(0, 1)
        if (rand < 0.1):
            mutate(child2)

        population.append(child1)
        population.append(child2)


def twoPoint(population):
    pairs = makePairs(population)

    for i in range(len(pairs)):
        if (i >= len(pairs) / 2):
            break
        point1 = random.randint(0, len(population[0]) - 1)
        point2 = random.randint(0, len(population[0]) - 1)
        child1 = np.array(population[pairs[i*2]], dtype='int32', copy=True)
        child2 = np.array(population[pairs[i*2 + 1]], dtype='int32', copy=True)

        if (point1 > point2):
            index1 = point2
            index2 = point1
        else:
            index1 = point1
            index2 = point2

        for j in range(index1, index2):
            new1 = child1[j]
            new2 = child2[j]

            child1[j] = new2
            child2[j] = new1

        population.append(child1)
        population.append(child2)


def trimPopulation(pop, populationSize):
    pop.sort(key=calculateFitness)
    for i in range(populationSize):
        pop.pop()

numberOfNodes = 150
graph = np.zeros((numberOfNodes, numberOfNodes), dtype='int32')
populationSize = 20
population = generateInitPopulation(numberOfNodes, populationSize)

pop1 = list.copy(population)
pop2 = list.copy(population)

generateGraph(numberOfNodes, graph)

for i in range(20):
    onePoint(pop1)
    trimPopulation(pop1, populationSize)
    
print('one point')

fitness = calculateFitness(pop1[0])
print(fitness)


for i in range(20):
    twoPoint(pop2)
    trimPopulation(pop2, populationSize)
    

print('two point')

fitness = calculateFitness(pop2[0])
print(fitness)