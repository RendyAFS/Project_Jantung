import numpy as np

def mean_distance(set1, set2):
    distances = np.abs(np.subtract.outer(set1, set2))
    mean = np.mean(distances)
    return mean

# Data set
S1 = [1, 3, 5]
S2 = [1, 6, 2]

# Mean Jarak S1 - S1
mean_s1_s1 = mean_distance(S1, S1)
print("Mean Jarak S1 - S1:", mean_s1_s1)

# Mean Jarak S1 - S2
mean_s1_s2 = mean_distance(S1, S2)
print("Mean Jarak S1 - S2:", mean_s1_s2)

# Mean Jarak S2 - S2
mean_s2_s2 = mean_distance(S2, S2)
print("Mean Jarak S2 - S2:", mean_s2_s2)