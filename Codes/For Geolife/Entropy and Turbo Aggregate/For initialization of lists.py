import pickle

entropy_of_all_users = [0]*181
grid_index_info_all_users = [[] for Null in range(182)]
entropy_file = "entropy_data.pkl"
open_entropy_file = open(entropy_file,"wb")
pickle.dump(entropy_of_all_users, open_entropy_file)
open_entropy_file.close()
grids_file = "grids_data.pkl"
open_grids_file = open(grids_file,"wb")
pickle.dump(grid_index_info_all_users, open_grids_file)
open_grids_file.close()