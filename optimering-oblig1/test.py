import numpy
import random
import time
import matplotlib.pyplot as plot
import coordinate as crdClass
import csv
import math

import tsp

def plotTour(tour, x, y, nr):
    fig = plot.figure(nr)
    plot.scatter(x=x,y=y)
    for index, line in enumerate(tour):
        if (index == len(tour) - 1):
            break

        xs = [x[tour[index]], x[tour[index+1]]]
        ys = [y[tour[index]], y[tour[index+1]]]

        if (index == 0):
            plot.plot(xs, ys, '-k', c='red')
        else:
            plot.plot(xs, ys, '-k')
    
    return fig


def makeGraph(numberOfCities, graph, x, y):

    with open('./data/city_coordinates_' + str(numberOfCities) + '.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        for index, row in enumerate(reader):
            x[index] = int(row[0])
            y[index] = int(row[1])

        csvFile.close()
    
    start = time.time()
    with open('./data/distance_' + str(numberOfCities) + '.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        for index, row in enumerate(reader):
            graph[index] = row
    csvFile.close()
    end = time.time()
    print(end-start)

numberOfCities = 100


distanceMatrix = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')
x = numpy.zeros(numberOfCities, dtype='int32')
y = numpy.zeros(numberOfCities, dtype='int32')

makeGraph(numberOfCities, distanceMatrix, x, y)

""" inital solutions """
start = time.time()
randTour = tsp.randomAlgorithm(distanceMatrix)
end = time.time()
timeRand = end-start

start = time.time()
iterTour = tsp.iterativeRandom(distanceMatrix, 10)
end = time.time()
timeIter = end-start

start = time.time()
greedyTour = tsp.greedyMethod(distanceMatrix)
end = time.time()
timeGreed = end-start



fig1 = plotTour(randTour, x, y, 1)
fig2 = plotTour(iterTour, x, y, 2)
fig3 = plotTour(greedyTour, x, y, 3)

""" greegy improvement """
start = time.time()
randImpr = tsp.greedyImprovement(randTour, distanceMatrix, 5000)
end = time.time()
timeRandImpr = end-start

start = time.time()
iterImpr = tsp.greedyImprovement(iterTour, distanceMatrix, 5000)
end = time.time()
timeIterImpr = end-start

start = time.time()
greedImpr = tsp.greedyImprovement(greedyTour, distanceMatrix, 5000)
end = time.time()
timeGreedImpr = end-start



""" greegy random improvement """
#randImpr = tsp.greedyRandomImprovement(randTour, distanceMatrix, 500, 0.9)
#iterImpr = tsp.greedyRandomImprovement(iterTour, distanceMatrix, 500, 0.9)
#greedImpr = tsp.greedyRandomImprovement(greedyTour, distanceMatrix, 500, 0.9)

fig4 = plotTour(randImpr, x, y, 4)
fig5 = plotTour(iterImpr, x, y, 5)
fig6 = plotTour(greedImpr, x, y, 6)

fig1.suptitle(
    'Cost random: ' + 
    str(tsp.calculateCost(randTour, distanceMatrix)) +
    ', Time: ' +
    str(timeRand) 
)

fig2.suptitle(
    'Cost iterative random: ' + 
    str(tsp.calculateCost(iterTour, distanceMatrix)) +
    ', Time: ' +
    str(timeIter)
)

fig3.suptitle(
    'Cost greedy: ' + 
    str(tsp.calculateCost(greedyTour, distanceMatrix)) +
    ', Time: ' +
    str(timeGreed)
)

fig4.suptitle(
    'Cost random: ' + 
    str(tsp.calculateCost(randImpr, distanceMatrix)) +
    ', Time: ' +
    str(timeRandImpr) 
)

fig5.suptitle(
    'Cost iterative random: ' + 
    str(tsp.calculateCost(iterImpr, distanceMatrix)) +
    ', Time: ' +
    str(timeIterImpr)
)

fig6.suptitle(
    'Cost greedy: ' + 
    str(tsp.calculateCost(greedImpr, distanceMatrix)) +
    ', Time: ' +
    str(timeGreedImpr)
)

fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()
plot.show()


#print('Cost rand:', tsp.calculateCost(randTour, graph))
#print('Cost rand Impro:', tsp.calculateCost(randImpr, graph))
#print('Cost iter:', tsp.calculateCost(iterTour, graph))
#print('Cost iter impro:', tsp.calculateCost(iterImpr, graph))
#print('Cost greed:', tsp.calculateCost(greedyTour, graph))
#print('Cost greed impro:', tsp.calculateCost(greedImpr, graph))
