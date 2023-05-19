import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Minimum Value Amplitudo
min_amplitudo_s1_s1 = min(float(row['s1']) for row in data)
min_amplitudo_s2_s2 = min(float(row['s2']) for row in data)
min_amplitudo_s1_s2 = min(abs(float(row['s1']) - float(row['s2'])) for row in data)

# Menampilkan hasil
print("Minimum Value Amplitudo s1-s1:", min_amplitudo_s1_s1)
print("Minimum Value Amplitudo s2-s2:", min_amplitudo_s2_s2)
print("Minimum Value Amplitudo s1-s2:", min_amplitudo_s1_s2)
