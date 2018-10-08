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
    nodesVisited = 1

    while (nodesVisited < len(graph)):
        nextNode = random.randint(0,len(graph) -1)
        if (visited[nextNode]):
            continue
        visited[nextNode] = True
        tour.append(nextNode)
        nodesVisited += 1
    
    return tour

def iterativeRandom(graph, numberOfTries):
    
    bestTour = []
    iterations = 0

    while (iterations < numberOfTries):
        currTour = randomAlgorithm(graph)
        if (iterations == 0):
            bestTour = currTour
            iterations += 1
            continue

        if (calculateCost(currTour, graph) < calculateCost(bestTour, graph)):
            bestTour = currTour

        iterations += 1

    return bestTour

def greedyMethod(graph):
    tour = []
    visited = numpy.zeros((len(graph)), dtype='bool')

    startingNode = random.randint(0,len(graph))
    visited[startingNode] = True
    tour.append(startingNode)
    nodesVisited = 1
    prevNode = startingNode

    while (nodesVisited < len(graph)):
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
        nodesVisited +=1
    
    return tour