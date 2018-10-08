import numpy
import random

import tsp

def makeGraph(numberOfCities, graph):

    for i in range(numberOfCities):
        for j in range(i, numberOfCities):
            if i == j:
                distance = -1
                graph[i][j] = distance
            else:
                distance = random.randint(1, 100)
                graph[i][j] = distance
                graph[j][i] = distance

numberOfCities = 1000
graph = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')

makeGraph(numberOfCities, graph)

randTour = tsp.randomAlgorithm(graph)
iterTour = tsp.iterativeRandom(graph, 10)
greedyTour = tsp.greedyMethod(graph)


print('Cost rand:', tsp.calculateCost(randTour, graph))
print('Cost iter:', tsp.calculateCost(iterTour, graph))
print('Cost Greedy:', tsp.calculateCost(greedyTour, graph))

