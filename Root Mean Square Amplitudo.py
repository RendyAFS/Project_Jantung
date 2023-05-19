import csv
import math

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Root Mean Square (RMS) Amplitudo
rms_amplitudo_s1_s1 = math.sqrt(sum(float(row['s1'])**2 for row in data) / len(data))
rms_amplitudo_s2_s2 = math.sqrt(sum(float(row['s2'])**2 for row in data) / len(data))
rms_amplitudo_s1_s2 = math.sqrt(sum((float(row['s1']) - float(row['s2']))**2 for row in data) / len(data))

# Menampilkan hasil
print("Root Mean Square (RMS) Amplitudo s1-s1:", rms_amplitudo_s1_s1)
print("Root Mean Square (RMS) Amplitudo s2-s2:", rms_amplitudo_s2_s2)
print("Root Mean Square (RMS) Amplitudo s1-s2:", rms_amplitudo_s1_s2)
