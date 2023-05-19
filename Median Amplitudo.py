import csv
import statistics

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung jarak antara kolom "s1-s1", "s2-s2", dan "s1-s2"
s1_s1_distances = [abs(float(data[i+1]['s1']) - float(data[i]['s1'])) for i in range(len(data)-1)]
s2_s2_distances = [abs(float(data[i+1]['s2']) - float(data[i]['s2'])) for i in range(len(data)-1)]
s1_s2_distances = [abs(float(data[i]['s1']) - float(data[i]['s2'])) for i in range(len(data))]

# Menghitung median
median_s1_s1 = statistics.median(s1_s1_distances)
median_s2_s2 = statistics.median(s2_s2_distances)
median_s1_s2 = statistics.median(s1_s2_distances)

# Menampilkan hasil
print("Median jarak s1-s1:", median_s1_s1)
print("Median jarak s2-s2:", median_s2_s2)
print("Median jarak s1-s2:", median_s1_s2)
