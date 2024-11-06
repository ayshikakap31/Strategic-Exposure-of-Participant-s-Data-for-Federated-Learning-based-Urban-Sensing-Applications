import pickle

distance_of_all_users = [0]*181
grid_index_info_all_users = [[] for Null in range(182)]
distance_file = "distance_data.pkl"
open_distance_file = open(distance_file,"wb")
pickle.dump(distance_of_all_users, open_distance_file)
open_distance_file.close()
grids_file = "grids_data.pkl"
open_grids_file = open(grids_file,"wb")
pickle.dump(grid_index_info_all_users, open_grids_file)
open_grids_file.close()