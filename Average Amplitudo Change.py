import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Average Amplitudo Change
avg_amplitudo_change_s1_s1 = 0
avg_amplitudo_change_s2_s2 = 0
avg_amplitudo_change_s1_s2 = 0

for i in range(len(data) - 1):
    s1_s1_diff = abs(float(data[i+1]['s1']) - float(data[i]['s1']))
    s2_s2_diff = abs(float(data[i+1]['s2']) - float(data[i]['s2']))
    s1_s2_diff = abs(float(data[i]['s1']) - float(data[i]['s2']))

    avg_amplitudo_change_s1_s1 += s1_s1_diff
    avg_amplitudo_change_s2_s2 += s2_s2_diff
    avg_amplitudo_change_s1_s2 += s1_s2_diff

avg_amplitudo_change_s1_s1 /= len(data) - 1
avg_amplitudo_change_s2_s2 /= len(data) - 1
avg_amplitudo_change_s1_s2 /= len(data)

# Menampilkan hasil
print("Average Amplitudo Change s1-s1:", avg_amplitudo_change_s1_s1)
print("Average Amplitudo Change s2-s2:", avg_amplitudo_change_s2_s2)
print("Average Amplitudo Change s1-s2:", avg_amplitudo_change_s1_s2)
