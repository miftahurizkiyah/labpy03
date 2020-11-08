# Tugas Praktikum 3 - latihan 1

n=int(input('Masukan Nilai N : '))
print("\n")
import random

for a in  list(range(1, n+1, 1)) :
    print("Data ke : ",a, "=>",random.uniform(0, 0.5))

print("Selesai")

