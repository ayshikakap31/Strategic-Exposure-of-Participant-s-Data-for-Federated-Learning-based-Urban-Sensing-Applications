import numpy as np

def calculate_entropy(freq):
    Probabilities = []
    sum_of_all_freq=0
    for ele in range(0, len(freq)):
        sum_of_all_freq = sum_of_all_freq + freq[ele]
    max_size = len(freq)
    for i in range(max_size):
      Prob = freq[i]/sum_of_all_freq
      Probabilities.append(Prob)
    entropy_of_loc = -np.sum(Probabilities*np.log2(Probabilities))
    return entropy_of_loc