import pandas as pd, numpy as np
from convert_long_lat_to_XY import convert_long_lat_to_XY

def find_boundary_grid_points():
    min_lats_list = []
    max_lats_list = []
    min_longs_list = []
    max_longs_list = []
    for temp_1 in range(0,182,1):
        if temp_1>=0 and temp_1<10:
            path = pd.read_csv("User_00"+str(temp_1)+".csv", encoding='utf-8')
        
        elif temp_1>=10 and temp_1<100:
            path = pd.read_csv("User_0"+str(temp_1)+".csv", encoding='utf-8')
        elif temp_1>=100 and temp_1<182:
            path = pd.read_csv("User_"+str(temp_1)+".csv", encoding='utf-8')
        coords = path[['Latitude', 'Longitude']].to_numpy()
        lats = coords[:,0]
        longs = coords[:,1]
        size1 = lats.shape
        size_coords = size1[0]
        coords_XY = []
        for i in range(size_coords):
          p_xy = convert_long_lat_to_XY(longs[i],lats[i])
          coords_XY.append(p_xy)
        coords_conv_xy = np.array(coords_XY)
        lats_xy = coords_conv_xy[:,1]
        longs_xy = coords_conv_xy[:,0]
        lats_index_min = np.argmin(lats_xy)
        lats_index_max = np.argmax(lats_xy)
        longs_index_min = np.argmin(longs_xy)
        longs_index_max = np.argmax(longs_xy)
        min_lats_list.append(lats_xy[lats_index_min])
        max_lats_list.append(lats_xy[lats_index_max])
        min_longs_list.append(longs_xy[longs_index_min])
        max_longs_list.append(longs_xy[longs_index_max])
    min_lat_point = min(min_lats_list)
    max_lat_point = max(max_lats_list)
    min_long_point = min(min_longs_list)
    max_long_point = max(max_longs_list)
    return min_lat_point, max_lat_point, min_long_point, max_long_point

p1, p2, p3, p4 = find_boundary_grid_points()
