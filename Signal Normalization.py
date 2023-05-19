import csv
import numpy as np

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Mengambil amplitudo dari kolom "s1-s1", "s2-s2", dan "s1-s2"
amplitudo_s1_s1 = [float(row['s1']) for row in data]
amplitudo_s2_s2 = [float(row['s2']) for row in data]
amplitudo_s1_s2 = [float(row['s1']) - float(row['s2']) for row in data]

# Signal normalization
normalized_s1_s1 = (amplitudo_s1_s1 - np.mean(amplitudo_s1_s1)) / np.std(amplitudo_s1_s1)
normalized_s2_s2 = (amplitudo_s2_s2 - np.mean(amplitudo_s2_s2)) / np.std(amplitudo_s2_s2)
normalized_s1_s2 = (amplitudo_s1_s2 - np.mean(amplitudo_s1_s2)) / np.std(amplitudo_s1_s2)

# Menampilkan hasil
print("Normalized s1-s1:", normalized_s1_s1)
print("Normalized s2-s2:", normalized_s2_s2)
print("Normalized s1-s2:", normalized_s1_s2)
