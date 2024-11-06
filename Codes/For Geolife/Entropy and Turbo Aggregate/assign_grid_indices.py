import numpy as np

def assign_grid_indices():
    d=1
    grids_index = np.zeros((10,10,24))
    for t in range(24):
        for yax in range(10):
            for xax in range(10):
                 grids_index[xax,yax,t]=int(d)
                 d=d+1
    return grids_index