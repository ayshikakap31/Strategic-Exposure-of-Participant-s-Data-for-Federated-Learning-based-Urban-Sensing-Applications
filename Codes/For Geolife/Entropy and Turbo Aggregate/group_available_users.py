import pandas as pd, numpy as np

def group_available_users(time_val):
    group_users = []
    lat_lon = []
    for temp_1 in range(0,182,1):
        if temp_1>=0 and temp_1<10:
            path = pd.read_csv("D:/Codes/Privacy_geolife/Geolife Converted to csv dataset/User 00"+str(temp_1)+
                             "/Trajectory/Merged Data/User_00"+str(temp_1)+".csv", encoding='utf-8')
        elif temp_1>=10 and temp_1<100:
            path = pd.read_csv("D:/Codes/Privacy_geolife/Geolife Converted to csv dataset/User 0"+str(temp_1)+
                             "/Trajectory/Merged Data/User_0"+str(temp_1)+".csv", encoding='utf-8')
        else:
            path = pd.read_csv("D:/Codes/Privacy_geolife/Geolife Converted to csv dataset/User "+str(temp_1)+
                             "/Trajectory/Merged Data/User_"+str(temp_1)+".csv", encoding='utf-8')
        
        time_user = (path[['Time']].to_numpy()).tolist()
        coords = (path[['Latitude', 'Longitude']].to_numpy()).tolist()
        for temp_2 in range(len(time_user)):
            time_extract = time_user[temp_2][0]
            if str(time_extract) == time_val:
                group_users.append(temp_1)
                lat_lon.append([coords[temp_2][0],coords[temp_2][1]])
                break
    return group_users, lat_lon