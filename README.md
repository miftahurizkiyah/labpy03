# labpy03
Repository ini dibuat untuk memenuhi tugas bahasa pemrograman pertemuan ke-7 pada Modul Praktikum 3.

***Nama : Miftahu Rizkiyah***
 
***NIM : 312010014***

***Kelas : TI.20.B.1***

* Pada repository ini saya mendapatkan tugas dari Dosen Bahasa Pemrograman, untuk program yang ada pada latihan 1, latihan 2 dan program 1.
untuk tugas-tugas tersebut bisa dilihat pada link berikut : <br>
1. [link_latihan1](latihan1.py)
2. [link_latihan2](latihan2.py)
3. [link_program1](program1.py)
<br>



Pertama saya akan membahas tentang tugas latihan 1 yaitu menampilakn (n) bilangan acak yang lebih kecil dari 0.5.
diprogram ini saya menggunakan source code seperti dibawah ini : <br>
![Tugas_latihan1](pict/Tugas_latihan1.PNG)
``` python
n=int(input('Masukan Nilai N : '))

import random

for a in  list(range(1, n+1, 1)) :
    print("Data ke : ",a, "=>",random.uniform(0, 0.5))

print("Selesai")
```
Pada source code tersebut saya menggunakan kombinasi random dan uniform, sehingga menghasilkan output seperti dibawah ini : <br>
![Output_latihan1](pict/Output_latihan1.PNG)

* Note : <br>
fungsi random() akan menghasilkan angka yang memiliki tipe data float dan berada pada rentang 0,0 hingga 1,0. Pada fungsi ini tidak perlu menambahkan argument. <br>
uniform sendiri berfungsi untuk menampilkan bilangan float random dengan batas awal bilangan dan batas akhir.







