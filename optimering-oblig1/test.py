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
                distance = random.randint(1, 10)
                graph[i][j] = distance
                graph[j][i] = distance

numberOfCities = 1000
graph = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')

makeGraph(numberOfCities, graph)

randTour = tsp.randomAlgorithm(graph)
iterTour = tsp.iterativeRandom(graph, 10)
greedyTour = tsp.greedyMethod(graph)

""" randImpr = tsp.greedyImprovement(randTour, graph, 5000)
iterImpr = tsp.greedyImprovement(iterTour, graph, 5000)
greedImpr = tsp.greedyImprovement(greedyTour, graph, 5000) """

randImpr = tsp.greedyRandomImprovement(randTour, graph, 100, 0.9)

print('Cost rand:', tsp.calculateCost(randTour, graph))
print('Cost rand Impro:', tsp.calculateCost(randImpr, graph))
""" print('Cost iter:', tsp.calculateCost(iterTour, graph))
print('Cost iter impro:', tsp.calculateCost(iterImpr, graph))
print('Cost greed:', tsp.calculateCost(greedyTour, graph))
print('Cost greed impro:', tsp.calculateCost(greedImpr, graph))
 """