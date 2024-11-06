from itertools import groupby
import time
import pickle
from convert_long_lat_to_XY import convert_long_lat_to_XY
from assign_grid_indices import assign_grid_indices
from grid_partitions import grid_partitions
from calculate_entropy import calculate_entropy
from turbo_aggregate import turbo_aggregate
from group_available_users import group_available_users 
from create_list import create_list
def main():
    time_s = '11:00:15'
    entropy_file = "entropy_data.pkl"
    grids_file = "grids_data.pkl"
    grids_index = assign_grid_indices()
    X,Y,Z = grid_partitions()
    entropy_of_all_users, grid_index_info_all_users = create_list(entropy_file, grids_file)
    start_time = time.time()
    users_available, users_coords = group_available_users(time_s)
    users_for_TA = []
    for temp_loop in range(len(users_available)):
        frequency_of_grids = []
        found_at = 0
        participant = users_available[temp_loop]
        participant_coords = convert_long_lat_to_XY(users_coords[temp_loop][1], users_coords[temp_loop][0])
        p_lat = participant_coords[1]
        p_long = participant_coords[0]
        p_time = (sum(int(x) * 60 ** i for i, x in enumerate(reversed(time_s.split(':')))))/3600
        
        for t in range(24):
            if ((p_time>Z[t] and p_time<Z[t+1]) or (p_time==Z[t]) or (p_time==0)):
                for yax in range(10):
                    if (((p_lat>Y[yax]) and (p_lat<Y[yax+1])) or (p_lat==Y[yax])):
                        for xax in range(10):
                            if (((p_long>X[xax]) and (p_long<X[xax+1])) or (p_long==X[xax])):
                                found_at = grids_index[xax,yax,t]
                                #print("Found point of "+ str(participant)+" in :"+str(found_at))
                                break
        grid_index_info_all_users[participant] += [found_at]
        
        frequency_of_grids = [len(list(group)) for key, group in groupby(grid_index_info_all_users[participant])]
        current_entropy = calculate_entropy(frequency_of_grids)
        if (entropy_of_all_users[participant] < current_entropy):
            entropy_of_all_users[participant] = current_entropy
        else:
            users_for_TA += [participant]
        entropy_of_all_users[participant] = current_entropy
    if len(users_for_TA)>0:
        turbo_aggregate(len(users_for_TA), 3, users_for_TA)
    end_time = time.time()
    print('Duration: {}'.format((end_time - start_time))) 
    open_entropy_file = open(entropy_file,"wb")
    pickle.dump(entropy_of_all_users, open_entropy_file)
    open_entropy_file.close()
    open_grids_file = open(grids_file,"wb")
    pickle.dump(grid_index_info_all_users, open_grids_file)
    open_grids_file.close()
    
# Call to main function to run the program
if __name__ == "__main__":
    main()
    
with open("grids_data.pkl", 'rb') as f:
    file_content = pickle.load(f) # deserialize using load()