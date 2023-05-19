import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Zero Cross Rate
zero_cross_rate_s1_s1 = 0
zero_cross_rate_s2_s2 = 0
zero_cross_rate_s1_s2 = 0

for i in range(1, len(data)):
    if float(data[i]['s1']) * float(data[i-1]['s1']) < 0:
        zero_cross_rate_s1_s1 += 1

    if float(data[i]['s2']) * float(data[i-1]['s2']) < 0:
        zero_cross_rate_s2_s2 += 1

    if (float(data[i]['s1']) - float(data[i]['s2'])) * (float(data[i-1]['s1']) - float(data[i-1]['s2'])) < 0:
        zero_cross_rate_s1_s2 += 1

# Menampilkan hasil
print("Zero Cross Rate s1-s1:", zero_cross_rate_s1_s1)
print("Zero Cross Rate s2-s2:", zero_cross_rate_s2_s2)
print("Zero Cross Rate s1-s2:", zero_cross_rate_s1_s2)
