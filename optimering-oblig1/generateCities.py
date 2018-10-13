import random
import numpy
import csv
import coordinate

def makeGraph(numberOfCities, coordinates):

    for i in range(numberOfCities):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)

        nCoordinate = coordinate.Coordinate(x=x, y=y)
        coordinates.append(nCoordinate)
        """ for j in range(i, numberOfCities):
            if i == j:
                distance = -1
                graph[i][j] = distance
            else:
                distance = random.randint(1,10)
                graph[i][j] = distance
                graph[j][i] = distance """


numberOfCities = 1000
coordinates = []
makeGraph(numberOfCities, coordinates)
print (coordinates)

with open('cities_1000.csv', 'w',newline='') as csvfile:
    writer = csv.writer(
        csvfile, 
        delimiter=','
    )
    for i in range(numberOfCities):
        row = [coordinates[i].x, coordinates[i].y]
        writer.writerow(row)
    
    csvfile.close()