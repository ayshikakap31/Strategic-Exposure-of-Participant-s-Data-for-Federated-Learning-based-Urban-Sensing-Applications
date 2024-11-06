import os
import pickle


def create_list(entropy_file, grids_file):
    open_entropy_file = open(entropy_file, "rb")
    entropy_list = pickle.load(open_entropy_file)
    open_entropy_file.close()
    open_grids_file = open(grids_file, "rb")
    grids_list = pickle.load(open_grids_file)
    open_grids_file.close()
    return entropy_list, grids_list