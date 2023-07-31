Batas waktu: 1 detik  
Batas memori: 64 MB
## SOAL
Terdapat N tombol yang dinomori dari 1 hingga N dan sebuah lampu dalam keadaan
mati. Apabila tombol ke-i ditekan, keadaan lampu akan berubah (dari mati menjadi
menyala, atau sebaliknya) apabila N habis dibagi oleh i. Apabila masing-masing
tombol ditekan tepat sekali, bagaimana keadaan lampu pada akhirnya?  
### Format Masukan
Sebuah baris berisi sebuah bilangan, yaitu N.
### Format Keluaran
Sebuah baris berisi:  
• "lampu mati", apabila keadaan akhir lampu adalah mati.  
• "lampu menyala", apabila keadaan akhir lampu adalah menyala.   

Contoh Masukan 1  
> 5

Contoh Keluaran 1  
> lampu mati

Contoh Masukan 2  
> 4

Contoh Keluaran 2  
> lampu menyala  
## ANALISIS
Ketika nilai N adalah genap, maka setiap tombol ditekan 2 kali yaitu pada saat i dan N/i.  
Contoh N = 8 maka nilai i adalah 1, 2, 4, 8.  
Posisi awal lampu: mati  
- saat menekan tombol ke-1 (i = 1) maka lampu akan menyala.
- saat menekan tombol ke-2 (i = 2) maka lampu akan mati.
- saat menekan tombol ke-4 (i = 4) maka lampu akan menyala.
- saat menekan tombol ke-8 (i = 8) maka kampu akan menyala.
Sehingga saat N bernilai genap maka lampu mati.

Ketika nilai N adalah ganjil, maka setiap tombol hanya ditekan satu kali yaitu pada saat i.   
Contoh N = 9 maka nilai i adalah 1, 3, 9.  
Posisi awal lampu: mati  
- saat menekan tombol ke-1 (i = 1) maka lampu akan menyala.
- saat menekan tombol ke-3 (i = 3) maka lampu akan mati.
- saat menekan tombol ke-9 (i = 9) maka lampu akan meyala.
Sehingga saat N bernilai ganjil maka lampu menyala.

## CODE IMPLEMENTATION  
- Python
```python
def lamp_state(N):

  if N % 2 == 0 :
    print("Lampu mati")
  else :
    print("Lampu menyala")

N = int(input("Masukan nilai:"))
print(lamp_state(N))
```
- Golang
```golang
package main

import (
	"fmt"
)

func lampState(N int) {
	if N % 2 == 0 {
		fmt.Println("Lampu mati")
	} else {
		fmt.Println("Lampu menyala")
	}
}

func main() {
	var N int
	fmt.Printf("Masukkan nilai: ")
	fmt.Scanf("%d", &N)
	lampState(N)
}
```
Untuk menyelesaikan ini sebenarnya hanya menggunakan kondisi if - else saja, dengan mengecek nilai N apakah genap atau ganjil. Apabila nilai N habis dibagi 2 maka N adalah genap dan apabila tidak habis dibagi 2 maka N adalah ganjil. Dalam menyelesaikan soal ini, saya menggunakan func lamp_state agar kode lebih terorganisir.

