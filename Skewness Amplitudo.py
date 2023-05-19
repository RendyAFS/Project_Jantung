import csv
import math

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung skewness untuk kolom "s1-s1", "s2-s2", dan "s1-s2"
s1_s1_differences = [float(data[i+1]['s1']) - float(data[i]['s1']) for i in range(len(data)-1)]
s2_s2_differences = [float(data[i+1]['s2']) - float(data[i]['s2']) for i in range(len(data)-1)]
s1_s2_differences = [float(data[i]['s1']) - float(data[i]['s2']) for i in range(len(data))]

# Menghitung mean
mean_s1_s1 = sum(s1_s1_differences) / len(s1_s1_differences)
mean_s2_s2 = sum(s2_s2_differences) / len(s2_s2_differences)
mean_s1_s2 = sum(s1_s2_differences) / len(s1_s2_differences)

# Menghitung standar deviasi
std_dev_s1_s1 = math.sqrt(sum((x - mean_s1_s1) ** 2 for x in s1_s1_differences) / len(s1_s1_differences))
std_dev_s2_s2 = math.sqrt(sum((x - mean_s2_s2) ** 2 for x in s2_s2_differences) / len(s2_s2_differences))
std_dev_s1_s2 = math.sqrt(sum((x - mean_s1_s2) ** 2 for x in s1_s2_differences) / len(s1_s2_differences))

# Menghitung skewness
skewness_s1_s1 = sum((x - mean_s1_s1) ** 3 for x in s1_s1_differences) / (len(s1_s1_differences) * std_dev_s1_s1 ** 3)
skewness_s2_s2 = sum((x - mean_s2_s2) ** 3 for x in s2_s2_differences) / (len(s2_s2_differences) * std_dev_s2_s2 ** 3)
skewness_s1_s2 = sum((x - mean_s1_s2) ** 3 for x in s1_s2_differences) / (len(s1_s2_differences) * std_dev_s1_s2 ** 3)

# Menampilkan hasil
print("Skewness s1-s1:", skewness_s1_s1)
print("Skewness s2-s2:", skewness_s2_s2)
print("Skewness s1-s2:", skewness_s1_s2)
