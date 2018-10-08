import random
import numpy
import sys

def calculateCost(tour, graph):
    cost = 0
    prevCity = tour[0]
    for i in range(1,len(tour)):
        currCity = tour[i]
        cost += graph[prevCity][currCity]
        prevCity = currCity

    return cost;
            
    
def randomAlgorithm(graph):
    visited = numpy.zeros((len(graph)), dtype='bool')
    tour = []

    startingNode = random.randint(0,len(graph) -1)
    visited[startingNode] = True
    tour.append(startingNode)

    while (len(tour) < len(graph)):
        nextNode = random.randint(0,len(graph) -1)
        if (visited[nextNode]):
            continue
        visited[nextNode] = True
        tour.append(nextNode)
    
    return tour

def iterativeRandom(graph, numberOfTries):
    
    bestTour = []
    iterations = 0

    while (iterations < numberOfTries):
        currTour = randomAlgorithm(graph)
        if (iterations == 0):
            bestTour = numpy.array(currTour, copy=True)
            iterations += 1
            continue

        if (calculateCost(currTour, graph) < calculateCost(bestTour, graph)):
            bestTour = numpy.array(currTour, copy=True)

        iterations += 1

    return bestTour

def greedyMethod(graph):
    tour = []
    visited = numpy.zeros((len(graph)), dtype='bool')

    startingNode = random.randint(0,len(graph) - 1)
    visited[startingNode] = True
    tour.append(startingNode)
    prevNode = startingNode

    while (len(tour) < len(graph)):
        lowestCost = sys.maxsize
        nearestNode = -1

        for i in range(0,len(graph)):
            if (visited[i]):
                continue
            if (graph[prevNode][i] < lowestCost):
                lowestCost = graph[prevNode][i]
                nearestNode = i
        
        if (nearestNode == -1):
            print('Something went wrong in greedy')

        visited[nearestNode] = True
        prevNode = nearestNode
        tour.append(nearestNode)
    
    return tour

def swapPlaces(tour, index1, index2):
    node1 = tour[index1]
    node2 = tour[index2]

    tour[index1] = node2
    tour[index2] = node1

def greedyImprovement(initialTour, graph, numberOfTries):
    iterations = 0
    newTour = numpy.array(initialTour, copy=True)

    while (iterations < numberOfTries):
        index1 = random.randint(0, len(initialTour) - 1)
        index2 = random.randint(0, len(initialTour) - 1)
        currTour = numpy.array(newTour, copy=True)
        
        swapPlaces(currTour, index1, index2)
        
        oldCost = calculateCost(newTour, graph)
        newCost = calculateCost(currTour, graph)

        if (newCost < oldCost):
            newTour = currTour
        
        iterations += 1

    return newTour

def greedyRandomImprovement(initialTour, graph, maxTries, poa):
    bestTour = numpy.array(initialTour, copy=True)
    bestCost = calculateCost(bestTour, graph)

    while (poa > 0.000001):
        oldTour = numpy.array(initialTour, copy=True)
        oldCost = calculateCost(oldTour, graph)

        for i in range(maxTries):
            newTour = numpy.array(oldTour, copy=True)
            index1 = random.randint(0, len(initialTour) - 1)
            index2 = random.randint(0, len(initialTour) - 1)

            swapPlaces(newTour, index1, index2)
            newCost = calculateCost(newTour, graph)

            if (newCost < oldCost):
                oldCost = newCost
                oldTour = numpy.array(newTour, copy=True)
                if (newCost < bestCost):
                    bestCost = newCost
                    bestTour = numpy.array(newTour, copy=True)
            else:
                rnd = random.uniform(0,1)
                
                if (rnd < poa):
                    oldCost = newCost
                    oldTour = numpy.array(newTour, copy=True)
            
        poa = 0.9 * poa
    
    return bestTour
