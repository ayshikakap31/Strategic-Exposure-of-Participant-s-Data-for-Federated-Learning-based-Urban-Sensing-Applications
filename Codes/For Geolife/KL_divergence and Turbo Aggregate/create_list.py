import os
import pickle


def create_list(distance_file, grids_file):
    open_distance_file = open(distance_file, "rb")
    distance_list = pickle.load(open_distance_file)
    open_distance_file.close()
    open_grids_file = open(grids_file, "rb")
    grids_list = pickle.load(open_grids_file)
    open_grids_file.close()
    return distance_list, grids_list