import csv
import numpy as np

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Variance Amplitudo
variance_s1_s1 = np.var([float(row['s1']) for row in data])
variance_s2_s2 = np.var([float(row['s2']) for row in data])
variance_s1_s2 = np.var([float(row['s1']) - float(row['s2']) for row in data])

# Menampilkan hasil
print("Variance Amplitudo s1-s1:", variance_s1_s1)
print("Variance Amplitudo s2-s2:", variance_s2_s2)
print("Variance Amplitudo s1-s2:", variance_s1_s2)
