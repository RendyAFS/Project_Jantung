import pandas as pd
from scipy.spatial.distance import cdist

# Membaca data dari file tes.csv
data = pd.read_csv("tes.csv")

# Mendapatkan koordinat S1 dan S2
s1_coordinates = data[['S1_x', 'S1_y']].values
s2_coordinates = data[['S2_x', 'S2_y']].values

# Menghitung mean jarak S1-S1
s1_s1_distances = cdist(s1_coordinates, s1_coordinates, metric='euclidean')
mean_s1_s1_distance = s1_s1_distances.mean()

# Menghitung mean jarak S1-S2
s1_s2_distances = cdist(s1_coordinates, s2_coordinates, metric='euclidean')
mean_s1_s2_distance = s1_s2_distances.mean()

# Menghitung mean jarak S2-S2
s2_s2_distances = cdist(s2_coordinates, s2_coordinates, metric='euclidean')
mean_s2_s2_distance = s2_s2_distances.mean()

# Menampilkan hasil
print("Mean Jarak S1-S1: ", mean_s1_s1_distance)
print("Mean Jarak S1-S2: ", mean_s1_s2_distance)
print("Mean Jarak S2-S2: ", mean_s2_s2_distance)
