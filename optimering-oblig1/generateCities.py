import random
import numpy
import csv

def makeGraph(numberOfCities, graph):

    for i in range(numberOfCities):
        for j in range(i, numberOfCities):
            if i == j:
                distance = -1
                graph[i][j] = distance
            else:
                distance = random.randint(1,10)
                graph[i][j] = distance
                graph[j][i] = distance


numberOfCities = 10
graph = numpy.zeros((numberOfCities,numberOfCities), dtype = 'int32')
makeGraph(numberOfCities, graph)

with open('cities.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for i in range(numberOfCities):
        for j in range(numberOfCities):
            writer.writerow([graph[i][j]])