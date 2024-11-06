import pandas as pd, numpy as np
import random
import time
from group_users import group_users
from group_available_users import group_available_users 
def generate_number(l,u):
  n = random.randint(l,u)
  return n
def func_zero_sum(n):
    if n%2==0:
        r1 = int(n/2)
    else:
        r1 = int((n-1)/2)
    r2 = n-r1
    c=0
    sum_final = 0
    y=[]
    # To generate positive numbers
    for j in range(r1):
      a = generate_number(25,75)
      y.insert(c,a)
      sum_final += y[c]
      c = c+1
    #To generate negative numbers
    for k in range(r2):
      if c>k and c<n-1:
        s2 = sum_final-1
        b = generate_number(-s2,0)
        y.insert(c,b)
      elif c == n-1:
        d = -sum_final
        y.insert(c,d)
      sum_final += y[c]
      c=c+1
    return y

def turbo_aggregate(total_available_users, users_each_group, avail_users):
    groups_partition = group_users(total_available_users, users_each_group, avail_users)
    U = []
    R = []
    x_tilde = []
    S = []
    x=[]
    for group in range(len(groups_partition)-1):
        u_l = []
        x_tilde_i_l = []
        if group+1 <= len(groups_partition):
            r_i_l = func_zero_sum(len(groups_partition[group+1]))
            if (len(groups_partition[group+1])) < users_each_group:
                r_i_l.append(0)
            R.append(r_i_l)
        for user in range(len(groups_partition[group])):
            x_tilde_i_j_l = []
            x_i_l = np.random.randint(32,75)
            u_i_l = np.random.randint(25,100)
            x.append(x_i_l)
            u_l.append(u_i_l)
            for next_group_user in range(len(r_i_l)):
                r_i_j_l = r_i_l[next_group_user]
                x_tilde_i_j = x_i_l + u_i_l + r_i_j_l
                x_tilde_i_j_l.append(x_tilde_i_j)
            x_tilde_i_l.append(x_tilde_i_j_l)
        U.append(u_l)   
        x_tilde.append(x_tilde_i_l)
        s_i_l = []
        if group == 0:
            for user in range(len(groups_partition[group])):
                s_i_l.append(0) 
            S.append(s_i_l)
        else:
            for user in range(len(groups_partition[group])):
                first_agg = (sum(S[group-1]))/len(groups_partition[group-1])
                sec_agg = 0
                for agg in range(len(groups_partition[group-1])) :
                    sec_agg += x_tilde[group-1][agg][user]
                #total_agg.append(first_agg + sec_agg)
                s_i_l.append(first_agg + sec_agg)
            S.append(s_i_l)
    # Final stage
    s_final = []
    for user in range(len(groups_partition[-1])):
        s_final_second_part = 0
        if total_available_users == users_each_group:
            s_final_first_part = sum(S[0])/len(groups_partition[-1])
        else:
            s_final_first_part = sum(S[-1])/len(groups_partition[-2])
        
        for temp in range(len(groups_partition[-2])):
            s_final_second_part += x_tilde[-1][temp][user]
        s_final.append(s_final_first_part + s_final_second_part)    
    # Removal of random masks from aggregate
    sum_u_l = 0
    total_agg = sum(s_final)/len(s_final)
    for temp in range(len(groups_partition)-1):
        for temp_2 in range(len(groups_partition[temp])):
            sum_u_l += U[temp][temp_2]
            
    final_agg = (total_agg - sum_u_l)
 
time_s = '11:00:00'

users_available, users_coords = group_available_users(time_s)
start_time = time.time()
turbo_aggregate(len(users_available), 3, users_available)
end_time = time.time()
print('Duration: {}'.format((end_time - start_time)*1000))