# Mencari mean jarak s1-s1 
array1 = [1, 3, 5, 10]

result1 = sum(array1[i] - array1[i-1] for i in range(1, len(array1))) / (len(array1) - 1)

print(f"Hasil mean Jarak s1-s1 \n {sum(array1[i] - array1[i-1] for i in range(1, len(array1)))}/{(len(array1) - 1)} = {result1}\n")

# Mencari mean jarak s2-s2 
array2 = [2, 4, 6, 10, 12]

result2 = sum(array2[i] - array2[i-1] for i in range(1, len(array2))) / (len(array2) - 1)

print(f"Hasil mean Jarak s2-s2 \n {sum(array2[i] - array2[i-1] for i in range(1, len(array2)))}/{(len(array2) - 1)} = {result2}\n")

# Mencari mean jarak s1-s2
s1 = [1, 3, 1, 7]
s2 = [2, 5, 3, 10]

result3 = sum(s2[i] - s1[i] for i in range(len(s1))) / len(s1)

print(f"Hasil mean Jarak s1-s2 \n {sum(s2[i] - s1[i] for i in range(len(s1)))}/{len(s1)} = {result3}")