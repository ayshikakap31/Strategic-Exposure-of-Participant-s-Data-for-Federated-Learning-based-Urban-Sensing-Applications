# To compute Spatial-Temporal Distance
def eucledian_dist(lat1,lon1,time1,lat2, lon2,time2):
    return ((0.5*(abs(float(lat2)-float(lat1))**2+abs(float(lon2)-float(lon1))**2)**0.5)+(0.5*abs(float(time2)-float(time1))))

