import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Mean Cross Rate (MCR)
mcr_s1_s1 = 0
mcr_s2_s2 = 0
mcr_s1_s2 = 0

for i in range(len(data)-1):
    if (float(data[i]['s1']) > 0 and float(data[i+1]['s1']) < 0) or (float(data[i]['s1']) < 0 and float(data[i+1]['s1']) > 0):
        mcr_s1_s1 += 1

    if (float(data[i]['s2']) > 0 and float(data[i+1]['s2']) < 0) or (float(data[i]['s2']) < 0 and float(data[i+1]['s2']) > 0):
        mcr_s2_s2 += 1

    if (float(data[i]['s1']) - float(data[i]['s2'])) * (float(data[i+1]['s1']) - float(data[i+1]['s2'])) < 0:
        mcr_s1_s2 += 1

mcr_s1_s1 /= len(data)-1
mcr_s2_s2 /= len(data)-1
mcr_s1_s2 /= len(data)-1

# Menampilkan hasil
print("Mean Cross Rate (MCR) s1-s1:", mcr_s1_s1)
print("Mean Cross Rate (MCR) s2-s2:", mcr_s2_s2)
print("Mean Cross Rate (MCR) s1-s2:", mcr_s1_s2)
