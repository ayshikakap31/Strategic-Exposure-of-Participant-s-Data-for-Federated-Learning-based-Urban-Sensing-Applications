import pandas as pd
import matplotlib.pyplot as plt
import os
plotdata = pd.DataFrame({
    "Traditional scheme":[86,83,88,87,88,86,87,83,83,88,75,79,80,76,75,77,80,81,84,81,77,82,81,73,78,77,76,82,84,80,77,79,74,78,77],
    "Proposed scheme 1: Spatial-Temporal Entropy":[86,76,81,73,72,75,3,6,11,20,22,27,56,55,53,60,59,61,61,1,1,6,9,7,11,20,22,28,33,47,50,0,1,4,7],
    "Proposed scheme 2: Histogram distance measurement using KL divergence":[86,76,82,77,78,78,3,5,6,16,18,22,57,60,58,61,62,63,69,1,1,3,1,1,2,6,14,14,25,21,23,0,0,3,2]},
    index = ["11:00:00","11:05:00","11:10:00","11:15:00","11:20:00","11:25:00",
             "11:30:00","11:35:00","11:40:00","11:45:00","11:50:00","11:55:00",
             "12:00:00","12:05:00","12:10:00","12:15:00","12:20:00","12:25:00",
             "12:30:00","12:35:00","12:40:00","12:45:00","12:50:00","12:55:00",
             "13:00:00","13:05:00","13:10:00","13:15:00","13:20:00","13:25:00",
             "13:30:00","13:35:00","13:40:00","13:45:00","13:50:00"])
plotdata.plot(kind="bar",figsize=(150, 70))
plt.ylim(0,100)
plt.yticks(fontsize=140)
plt.xticks(fontsize=110, rotation=90)
plt.xlabel("Time",fontsize=150)
plt.legend(fontsize=120)
plt.ylabel("Number of users",fontsize=150)
plt.savefig("Result_1_5_min.pdf",format='pdf')