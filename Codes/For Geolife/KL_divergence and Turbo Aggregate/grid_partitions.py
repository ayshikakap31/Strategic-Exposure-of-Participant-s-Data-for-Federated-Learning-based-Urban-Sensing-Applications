import numpy as np
#from find_boundary_grid_points import find_boundary_grid_points

def grid_partitions():
    min_lat_point, max_lat_point = 115434.57962502548, 7181531.439742012
    min_long_point, max_long_point = 166459.56142786378, 833631.2062675562
    X = np.linspace(min_long_point,max_long_point,10)
    Y = np.linspace(min_lat_point,max_lat_point, 10)
    Z = np.linspace(0,24,24)
    return X,Y,Z