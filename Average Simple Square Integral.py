import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Average Simple Square Integral
avg_ssi_s1_s1 = 0
avg_ssi_s2_s2 = 0
avg_ssi_s1_s2 = 0

for i in range(len(data)):
    s1_s1_squared = float(data[i]['s1']) ** 2
    s2_s2_squared = float(data[i]['s2']) ** 2
    s1_s2_squared = (float(data[i]['s1']) - float(data[i]['s2'])) ** 2

    avg_ssi_s1_s1 += s1_s1_squared
    avg_ssi_s2_s2 += s2_s2_squared
    avg_ssi_s1_s2 += s1_s2_squared

avg_ssi_s1_s1 /= len(data)
avg_ssi_s2_s2 /= len(data)
avg_ssi_s1_s2 /= len(data)

# Menampilkan hasil
print("Average Simple Square Integral s1-s1:", avg_ssi_s1_s1)
print("Average Simple Square Integral s2-s2:", avg_ssi_s2_s2)
print("Average Simple Square Integral s1-s2:", avg_ssi_s1_s2)