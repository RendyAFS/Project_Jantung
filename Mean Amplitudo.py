# MENCARI MEAN JARAK S1-S1
import pandas as pd

# Membaca data dari file tes.csv
data = pd.read_csv("data audio.csv")

# Mendapatkan kolom s1 dari data
s1_values = data["s1"].values

# Menghitung mean jarak S1
mean_s1_distance = sum(s1_values[i] - s1_values[i-1] for i in range(1, len(s1_values))) / (len(s1_values) - 1)

print(f"Mean Jarak S1-S1:\n{sum(s1_values[i] - s1_values[i-1] for i in range(1, len(s1_values)))} / {len(s1_values) - 1} = {mean_s1_distance}")

print("\n")

# MENCARI MEAN JARAK S2-S2
import pandas as pd

# Membaca data dari file tes.csv
data = pd.read_csv("data audio.csv")

# Mendapatkan kolom s1 dari data
s2_values = data["s2"].values

# Menghitung mean jarak S1
mean_s12_distance = sum(s2_values[i] - s2_values[i-1] for i in range(1, len(s2_values))) / (len(s2_values) - 1)

print(f"Mean Jarak S2-S2:\n{sum(s2_values[i] - s2_values[i-1] for i in range(1, len(s2_values)))} / {len(s2_values) - 1} = {mean_s12_distance}")


print("\n")

# MENCARI MEAN JARAK S1-S2
import pandas as pd

# Membaca data dari file tes.csv
data = pd.read_csv("data audio.csv")

# Mendapatkan kolom s1 dari data
s1_values = data["s1"].values
s2_values = data["s2"].values

# Menghitung mean jarak S1
mean_s2_distance = sum(s2_values[i] - s1_values[i-1] for i in range(len(s2_values))) / (len(s2_values))

print(f"Mean Jarak S1-S2:\n{sum(s2_values[i] - s1_values[i-1] for i in range(len(s2_values)))} / {len(s2_values)} = {mean_s2_distance}")