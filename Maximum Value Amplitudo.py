import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Maximum Value Amplitudo
max_amplitudo_s1_s1 = max(float(row['s1']) for row in data)
max_amplitudo_s2_s2 = max(float(row['s2']) for row in data)
max_amplitudo_s1_s2 = max(abs(float(row['s1']) - float(row['s2'])) for row in data)

# Menampilkan hasil
print("Maximum Value Amplitudo s1-s1:", max_amplitudo_s1_s1)
print("Maximum Value Amplitudo s2-s2:", max_amplitudo_s2_s2)
print("Maximum Value Amplitudo s1-s2:", max_amplitudo_s1_s2)
