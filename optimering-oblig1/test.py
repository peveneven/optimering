import numpy
import random
import time
import matplotlib.pyplot as plot
import coordinate as crdClass
import csv
import math

import tsp


def makeGraph(numberOfCities, graph, x, y):

    with open('cities_' + str(numberOfCities) + '.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        for index, row in enumerate(reader):
            x[index] = int(row[0])
            y[index] = int(row[1])

        csvFile.close()
    start = time.time()
    for i in range(numberOfCities):
        for j in range(i, numberOfCities):
            if i == j:
                distance = -1
                graph[i][j] = distance
            else:
                deltaX = abs(x[i] - x[j])
                deltaY = abs(y[i] - y[j])
                distance = math.sqrt(math.pow(deltaX,2) + math.pow(deltaY, 2))
                graph[i][j] = distance
                graph[j][i] = distance
    end = time.time()
    print('Time : ', end-start)

numberOfCities = 1000

distanceMatrix = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')
x = numpy.zeros(numberOfCities, dtype='int32')
y = numpy.zeros(numberOfCities, dtype='int32')

makeGraph(numberOfCities, distanceMatrix, x, y)

#randTour = tsp.randomAlgorithm(distanceMatrix)
#iterTour = tsp.iterativeRandom(graph, 10)
greedyTour = tsp.greedyMethod(distanceMatrix)

plot.scatter(x=x,y=y)
for index, line in enumerate(greedyTour):
    if (index == len(greedyTour) - 2):
        break
    
    xs = [x[greedyTour[index]], x[greedyTour[index+1]]]
    ys = [y[greedyTour[index]], y[greedyTour[index+1]]]
    plot.plot(xs, ys, '-k')

plot.show()

""" greegy improvement """
#randImpr = tsp.greedyImprovement(randTour, graph, 5000)
#iterImpr = tsp.greedyImprovement(iterTour, graph, 5000)
#greedImpr = tsp.greedyImprovement(greedyTour, graph, 5000)

""" greegy random improvement """
#randImpr = tsp.greedyRandomImprovement(randTour, graph, 100, 0.9)

#print('Cost rand:', tsp.calculateCost(randTour, graph))
#print('Cost rand Impro:', tsp.calculateCost(randImpr, graph))
#print('Cost iter:', tsp.calculateCost(iterTour, graph))
#print('Cost iter impro:', tsp.calculateCost(iterImpr, graph))
#print('Cost greed:', tsp.calculateCost(greedyTour, graph))
#print('Cost greed impro:', tsp.calculateCost(greedImpr, graph))
