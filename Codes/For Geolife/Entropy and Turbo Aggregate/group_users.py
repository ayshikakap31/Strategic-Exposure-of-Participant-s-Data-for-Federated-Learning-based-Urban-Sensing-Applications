import pandas as pd, numpy as np
import random
from group_available_users import group_available_users

def group_users(total_users, user_each_group, avail_users):
    if (total_users%user_each_group) == 0:
        num_groups = int(total_users/user_each_group)
    else:
        num_groups = int(total_users/user_each_group)+1
    user_list = avail_users
    random.shuffle(user_list)
    users_groups_partition = []
    count = 0
    for partition in range(num_groups-1):
        users = []
        for u in range(user_each_group):
            users.append(user_list[count])
            count += 1
        users_groups_partition.append(users)
    if (int(total_users%user_each_group)) != 0:
        users=[]
        for temp in range(int(total_users%user_each_group)):
            users.append(user_list[count+temp])
        users_groups_partition.append(users)
    if len(user_list) < user_each_group:
        users_index = random.sample(user_list, int(len(user_list)))
    else:
        users_index = random.sample(user_list, user_each_group)
    users_groups_partition.append(users_index)
    return users_groups_partition