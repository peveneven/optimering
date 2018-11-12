import random
import numpy
import csv
import coordinate
import math

def generateCoordinates(numberOfCities, coordinates):

    for i in range(numberOfCities):
        x = random.randint(1, 10000)
        y = random.randint(1, 10000)

        nCoordinate = coordinate.Coordinate(x=x, y=y)
        coordinates.append(nCoordinate)

def calculateDistance(numberOfCities, graph, coordinates):
    for i in range(numberOfCities):
        for j in range(i, numberOfCities):
            if i == j:
                distance = -1
                graph[i][j] = distance
            else:
                deltaX = abs(coordinates[i].x - coordinates[j].x)
                deltaY = abs(coordinates[i].y - coordinates[j].y)
                distance = math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2))
                graph[i][j] = distance
                graph[j][i] = distance
            


#citySize = [1000, 5000, 10000]
citySize = [100]

for size in citySize:
    
    coordinates = []
    generateCoordinates(size, coordinates)
    distanceMatrix = numpy.zeros((size,size), dtype = 'int32')
    calculateDistance(size, distanceMatrix, coordinates)

    with open('./data/city_coordinates_' + str(size) + '.csv', 'w',newline='') as csvfile:
        writer = csv.writer(
            csvfile, 
            delimiter=','
        )
        for i in range(size):
            row = [coordinates[i].x, coordinates[i].y]
            writer.writerow(row)

        csvfile.close()

    with open('./data/distance_' + str(size) + '.csv', 'w', newline='') as file:
        writer = csv.writer(
            file, 
            delimiter=','
        )
        for row in distanceMatrix:
            writer.writerow(row)