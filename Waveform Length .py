import csv

# Membaca data dari file CSV
data = []
with open('data audio.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Menghitung Waveform Length
waveform_length_s1_s1 = sum(abs(float(data[i+1]['s1']) - float(data[i]['s1'])) for i in range(len(data)-1))
waveform_length_s2_s2 = sum(abs(float(data[i+1]['s2']) - float(data[i]['s2'])) for i in range(len(data)-1))
waveform_length_s1_s2 = sum(abs((float(data[i+1]['s1']) - float(data[i+1]['s2'])) - (float(data[i]['s1']) - float(data[i]['s2']))) for i in range(len(data)-1))

# Menampilkan hasil
print("Waveform Length s1-s1:", waveform_length_s1_s1)
print("Waveform Length s2-s2:", waveform_length_s2_s2)
print("Waveform Length s1-s2:", waveform_length_s1_s2)
