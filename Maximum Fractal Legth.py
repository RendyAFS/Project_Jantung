import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Maximum Fractal Length
max_fractal_length_s1_s1 = 0
max_fractal_length_s2_s2 = 0
max_fractal_length_s1_s2 = 0

for i in range(len(data)):
    amplitude_s1_s1 = abs(float(data[i]['s1']))
    amplitude_s2_s2 = abs(float(data[i]['s2']))
    amplitude_s1_s2 = abs(float(data[i]['s1']) - float(data[i]['s2']))

    # Menghitung panjang fraktal
    fractal_length_s1_s1 = 0
    fractal_length_s2_s2 = 0
    fractal_length_s1_s2 = 0

    while amplitude_s1_s1 > 0:
        amplitude_s1_s1 /= 2
        fractal_length_s1_s1 += 1

    while amplitude_s2_s2 > 0:
        amplitude_s2_s2 /= 2
        fractal_length_s2_s2 += 1

    while amplitude_s1_s2 > 0:
        amplitude_s1_s2 /= 2
        fractal_length_s1_s2 += 1

    if fractal_length_s1_s1 > max_fractal_length_s1_s1:
        max_fractal_length_s1_s1 = fractal_length_s1_s1

    if fractal_length_s2_s2 > max_fractal_length_s2_s2:
        max_fractal_length_s2_s2 = fractal_length_s2_s2

    if fractal_length_s1_s2 > max_fractal_length_s1_s2:
        max_fractal_length_s1_s2 = fractal_length_s1_s2

# Menampilkan hasil
print("Maximum Fractal Length s1-s1:", max_fractal_length_s1_s1)
print("Maximum Fractal Length s2-s2:", max_fractal_length_s2_s2)
print("Maximum Fractal Length s1-s2:", max_fractal_length_s1_s2)
