import csv
import numpy as np

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Log Detector
log_detector_s1_s1 = np.log10(np.mean([abs(float(row['s1'])) for row in data]))
log_detector_s2_s2 = np.log10(np.mean([abs(float(row['s2'])) for row in data]))
log_detector_s1_s2 = np.log10(np.mean([abs(float(row['s1']) - float(row['s2'])) for row in data]))

# Menampilkan hasil
print("Log Detector s1-s1:", log_detector_s1_s1)
print("Log Detector s2-s2:", log_detector_s2_s2)
print("Log Detector s1-s2:", log_detector_s1_s2)
