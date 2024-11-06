import numpy as np
# Function to compute K-Nearest neighbors of points
def findKNN(distanceMatrix, k):
    count = len(distanceMatrix)
    global similarityMatrix #List to store k similar points to any point
    #similarityMatrix = [[0 for i in range(k)] for j in range(count)]
    similarityMatrix = np.zeros((count,k))
    for temp1 in range(count):
        # Sort each row of distanceMatrix based on spatial-temporal distance(value)
        #sortedMatrix = sorted(distanceMatrix[temp1])#, key=lambda x:x[1])
        sortedMatrix = [i[0] for i in sorted(enumerate(distanceMatrix[temp1]), key=lambda x:x[1])]
        sortedMatrix = np.array(sortedMatrix)
        for temp2 in range(k):
            similarityMatrix[temp1][temp2]=(sortedMatrix[temp2])#[0][1])
    return similarityMatrix