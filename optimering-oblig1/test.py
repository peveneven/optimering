import numpy
import random
import time
import matplotlib.pyplot as plot
import coordinate as crdClass
import csv
import math

import tsp

numberOfCities = 1000
x = numpy.zeros(numberOfCities, dtype='int32')
y = numpy.zeros(numberOfCities, dtype='int32')

def plotTour(*args):
    fig, ax = plot.subplots(len(args))

    for index, tour in enumerate(args):

        ax[index].scatter(x=x,y=y)

        for i, line in enumerate(tour):
       
            if (i == len(tour) - 1):
                break

            xs = [x[tour[i]], x[tour[i+1]]]
            ys = [y[tour[i]], y[tour[i+1]]]

            if (i == 0):
                ax[index].plot(xs, ys, '-k', c='red')
            else:
                ax[index].plot(xs, ys, '-k')
            
    
    return fig, ax


def makeGraph(numberOfCities, graph, x, y):

    with open('./data/city_coordinates_' + str(numberOfCities) + '.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        for index, row in enumerate(reader):
            x[index] = int(row[0])
            y[index] = int(row[1])

        csvFile.close()
    
    with open('./data/distance_' + str(numberOfCities) + '.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter = ',')
        for index, row in enumerate(reader):
            graph[index] = row
    csvFile.close()


distanceMatrix = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')

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


""" greegy improvement """
start = time.time()
randImpr = tsp.greedyImprovement(randTour, distanceMatrix, 100)
end = time.time()
timeRandImpr = end-start

start = time.time()
iterImpr = tsp.greedyImprovement(iterTour, distanceMatrix, 100)
end = time.time()
timeIterImpr = end-start

start = time.time()
greedImpr = tsp.greedyImprovement(greedyTour, distanceMatrix, 100)
end = time.time()
timeGreedImpr = end-start



""" greegy random improvement """
start = time.time()
randGreedRandImpr = tsp.greedyRandomImprovement(randTour, distanceMatrix, 100, 0.9)
end = time.time()
timeRandGrImpr = end-start

start = time.time()
iterGreedRandImpr = tsp.greedyRandomImprovement(iterTour, distanceMatrix, 100, 0.9)
end = time.time()
timeIterGrImpr = end-start

start = time.time()
greedGreedRandImpr = tsp.greedyRandomImprovement(greedyTour, distanceMatrix, 100, 0.9)
end = time.time()
timeGreedGrImpr = end-start

fig1, ax1 = plotTour(randTour, randImpr, randGreedRandImpr)
fig2, ax2 = plotTour(iterTour, iterImpr, iterGreedRandImpr)
fig3, ax3 = plotTour(greedyTour, greedImpr, greedGreedRandImpr)

""" Set titles """
ax1[0].set_title(
    'Random cost: ' +
    str(tsp.calculateCost(randTour, distanceMatrix)) +
    ' Time: ' +
    str(timeRand)
)

ax1[1].set_title(
    'Greedy cost: ' +
    str(tsp.calculateCost(randImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeRandImpr)
)

ax1[2].set_title(
    'Greedy random cost: ' +
    str(tsp.calculateCost(randGreedRandImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeRandGrImpr)
)

ax2[0].set_title(
    'Iterative Random cost: ' +
    str(tsp.calculateCost(iterTour, distanceMatrix)) +
    ' Time: ' +
    str(timeIter)
)

ax2[1].set_title(
    'Greedy cost: ' +
    str(tsp.calculateCost(iterImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeIterImpr)
)

ax2[2].set_title(
    'Greedy Random cost: ' +
    str(tsp.calculateCost(iterGreedRandImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeIterGrImpr)
)

ax3[0].set_title(
    'Greedy cost: ' +
    str(tsp.calculateCost(greedyTour, distanceMatrix)) +
    ' Time: ' +
    str(timeGreed)
)

ax3[1].set_title(
    'Greedy impr cost: ' +
    str(tsp.calculateCost(greedImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeGreedImpr)
)

ax3[2].set_title(
    'Greedy Random impr cost: ' +
    str(tsp.calculateCost(greedGreedRandImpr, distanceMatrix)) +
    ' Time: ' +
    str(timeGreedGrImpr)
)

fig1.show()
fig2.show()
fig3.show()

plot.show()

