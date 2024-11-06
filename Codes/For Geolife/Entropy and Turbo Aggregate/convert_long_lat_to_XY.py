import utm

def convert_long_lat_to_XY(input_lon,input_lat):
  x, y, zone, ut = utm.from_latlon(input_lat, input_lon)
  return x,y