import csv
import numpy as np

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Simple Square Integral
integral_s1_s1 = np.sum(np.square([float(row['s1']) for row in data]))
integral_s2_s2 = np.sum(np.square([float(row['s2']) for row in data]))
integral_s1_s2 = np.sum(np.square([float(row['s1']) - float(row['s2']) for row in data]))

# Menampilkan hasil
print("Simple Square Integral s1-s1:", integral_s1_s1)
print("Simple Square Integral s2-s2:", integral_s2_s2)
print("Simple Square Integral s1-s2:", integral_s1_s2)
