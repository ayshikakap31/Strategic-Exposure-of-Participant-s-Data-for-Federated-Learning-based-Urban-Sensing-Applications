# If two core points are within eps radius they belong to the same cluster
def findCoreNeighbors(p,corePoints,sharednearestN,eps):
    coreNeighbors=[]
    p2=None
    
    for temp1 in range(0,len(corePoints)):
        p2 = corePoints[temp1]
        # If two core points share more than eps neighbors make the core point core nearest neighbor of other
        if(p!=p2 and sharednearestN[p][p2]>=eps):
            coreNeighbors.append(p2)
    return coreNeighbors