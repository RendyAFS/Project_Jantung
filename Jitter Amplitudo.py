import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung jitter amplitudo
jitter_amplitudo_s1_s1 = []
jitter_amplitudo_s2_s2 = []
jitter_amplitudo_s1_s2 = []

for i in range(len(data) - 1):
    s1_s1_diff = abs(float(data[i+1]['s1']) - float(data[i]['s1']))
    s2_s2_diff = abs(float(data[i+1]['s2']) - float(data[i]['s2']))
    s1_s2_diff = abs(float(data[i]['s1']) - float(data[i]['s2']))

    jitter_amplitudo_s1_s1.append(s1_s1_diff)
    jitter_amplitudo_s2_s2.append(s2_s2_diff)
    jitter_amplitudo_s1_s2.append(s1_s2_diff)

# Menampilkan hasil
print("Jitter Amplitudo s1-s1:", jitter_amplitudo_s1_s1)
print("Jitter Amplitudo s2-s2:", jitter_amplitudo_s2_s2)
print("Jitter Amplitudo s1-s2:", jitter_amplitudo_s1_s2)
