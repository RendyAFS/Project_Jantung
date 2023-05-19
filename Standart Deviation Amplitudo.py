import csv
import math

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung jarak s1-s1
s1_s1_distances = []
for i in range(len(data)-1):
    s1_s1_distance = float(data[i+1]['s1']) - float(data[i]['s1'])
    s1_s1_distances.append(s1_s1_distance)

# Menghitung jarak s2-s2
s2_s2_distances = []
for i in range(len(data)-1):
    s2_s2_distance = float(data[i+1]['s2']) - float(data[i]['s2'])
    s2_s2_distances.append(s2_s2_distance)

# Menghitung jarak s1-s2
s1_s2_distances = []
for i in range(len(data)):
    s1_s2_distance = float(data[i]['s2']) - float(data[i]['s1'])
    s1_s2_distances.append(s1_s2_distance)

# Menghitung standar deviasi
s1_s1_stddev = math.sqrt(sum((distance - sum(s1_s1_distances)/len(s1_s1_distances))**2 for distance in s1_s1_distances) / len(s1_s1_distances))
s2_s2_stddev = math.sqrt(sum((distance - sum(s2_s2_distances)/len(s2_s2_distances))**2 for distance in s2_s2_distances) / len(s2_s2_distances))
s1_s2_stddev = math.sqrt(sum((distance - sum(s1_s2_distances)/len(s1_s2_distances))**2 for distance in s1_s2_distances) / len(s1_s2_distances))

# Menampilkan hasil
print(f"Standar Deviasi jarak s1-s1: {s1_s1_stddev}")
print(f"Standar Deviasi jarak s2-s2: {s2_s2_stddev}")
print(f"Standar Deviasi jarak s1-s2: {s1_s2_stddev}")
