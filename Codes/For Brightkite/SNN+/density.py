# Calculate SNN density of each point
def density(x, eps, count):
    numPoints=0
    for temp1 in range(0,count):
        if x[temp1] >= eps:
            numPoints += 1
    return numPoints