import numpy as np
from itertools import groupby
import time
import pickle
from convert_long_lat_to_XY import convert_long_lat_to_XY
from assign_grid_indices import assign_grid_indices
from grid_partitions import grid_partitions
from turbo_aggregate import turbo_aggregate
from group_available_users import group_available_users 
from create_list import create_list
from math import log
from scipy.special import kl_div

time_s = '12:00:15'
distance_file = "distance_data.pkl"
grids_file = "grids_data.pkl"
grids_index = assign_grid_indices()
X,Y,Z = grid_partitions()
distance_of_all_users, grid_index_info_all_users = create_list(distance_file, grids_file)
users_available, users_coords = group_available_users(time_s)
users_for_TA = []
for temp_loop in range(len(users_available)):
    found_at = 0
    flat_hist = np.ones((1,2400))
    d=1
    point_count_inside_grid = np.zeros((1,2400))
    participant = users_available[temp_loop]
    participant_coords = convert_long_lat_to_XY(users_coords[temp_loop][1], users_coords[temp_loop][0])
    p_lat = participant_coords[1]
    p_long = participant_coords[0]
    kl_pq = np.zeros((1,len(users_coords)))
    p_time = (sum(int(x) * 60 ** i for i, x in enumerate(reversed(time_s.split(':')))))/3600
    
    for t in range(24):
        if ((p_time>Z[t] and p_time<Z[t+1]) or (p_time==Z[t]) or (p_time==0)):
            for yax in range(10):
                if (((p_lat>Y[yax]) and (p_lat<Y[yax+1])) or (p_lat==Y[yax])):
                    for xax in range(10):
                        if (((p_long>X[xax]) and (p_long<X[xax+1])) or (p_long==X[xax])):
                            found_at = grids_index[xax,yax,t]
                            break
    grid_index_info_all_users[participant] += [found_at]
    for i in range(len(grid_index_info_all_users[participant])):
        l = grid_index_info_all_users[participant]
        point_count_inside_grid[:, int(l[i])] += 1
    normalizedData = (point_count_inside_grid-np.min(point_count_inside_grid))/(np.max(point_count_inside_grid)-np.min(point_count_inside_grid))
    distance = sum(kl_div(normalizedData[0,:], flat_hist[0,:]))
    
    if t > 0:
        if distance < distance_of_all_users[participant]:
            distance_of_all_users[participant] = distance
        else:
           users_for_TA += [participant]
    distance_of_all_users[participant] = distance
# if len(users_for_TA)>3:
#     turbo_aggregate(len(users_for_TA), 3, users_for_TA)
open_distance_file = open(distance_file,"wb")
pickle.dump(distance_of_all_users, open_distance_file)
open_distance_file.close()
open_grids_file = open(grids_file,"wb")
pickle.dump(grid_index_info_all_users, open_grids_file)
open_grids_file.close()                            
