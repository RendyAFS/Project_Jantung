import csv
import math

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Kurtosis Amplitudo
kurtosis_amplitudo_s1_s1 = 0
kurtosis_amplitudo_s2_s2 = 0
kurtosis_amplitudo_s1_s2 = 0

mean_s1_s1 = sum(float(row['s1']) for row in data) / len(data)
mean_s2_s2 = sum(float(row['s2']) for row in data) / len(data)
mean_s1_s2 = sum(float(row['s1']) - float(row['s2']) for row in data) / len(data)

for row in data:
    kurtosis_amplitudo_s1_s1 += (float(row['s1']) - mean_s1_s1) ** 4
    kurtosis_amplitudo_s2_s2 += (float(row['s2']) - mean_s2_s2) ** 4
    kurtosis_amplitudo_s1_s2 += ((float(row['s1']) - float(row['s2'])) - mean_s1_s2) ** 4

kurtosis_amplitudo_s1_s1 /= len(data)
kurtosis_amplitudo_s2_s2 /= len(data)
kurtosis_amplitudo_s1_s2 /= len(data)

# Menampilkan hasil
print("Kurtosis Amplitudo s1-s1:", kurtosis_amplitudo_s1_s1)
print("Kurtosis Amplitudo s2-s2:", kurtosis_amplitudo_s2_s2)
print("Kurtosis Amplitudo s1-s2:", kurtosis_amplitudo_s1_s2)
