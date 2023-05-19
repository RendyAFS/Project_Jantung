import csv
from statistics import mode

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung modus untuk kolom "s1-s1", "s2-s2", dan "s1-s2"
s1_s1_distances = [abs(float(data[i+1]['s1']) - float(data[i]['s1'])) for i in range(len(data)-1)]
s2_s2_distances = [abs(float(data[i+1]['s2']) - float(data[i]['s2'])) for i in range(len(data)-1)]
s1_s2_distances = [abs(float(data[i]['s1']) - float(data[i]['s2'])) for i in range(len(data))]

# Menghitung modus
mode_s1_s1 = mode(s1_s1_distances)
mode_s2_s2 = mode(s2_s2_distances)
mode_s1_s2 = mode(s1_s2_distances)

# Menampilkan hasil
print("Modus jarak s1-s1:", mode_s1_s1)
print("Modus jarak s2-s2:", mode_s2_s2)
print("Modus jarak s1-s2:", mode_s1_s2)
