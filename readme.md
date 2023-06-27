Berikut analisis algorithm untuk mengevaluasi, Worst case, Best case, dan Average case pada bubble sort dan insertion sort:

Bubble Sort:
1. Worst Case: Dalam kasus terburuk, Bubble Sort memiliki kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam array. Hal ini terjadi ketika array dalam kondisi terbalik secara terbalik, yang memerlukan perbandingan dan pertukaran elemen pada setiap iterasi.
2. Best Case: Dalam kasus terbaik, Bubble Sort memiliki kompleksitas waktu O(n), di mana n adalah jumlah elemen dalam array. Ini terjadi ketika array sudah terurut secara menaik, dan tidak ada pertukaran yang diperlukan selama iterasi.
3. Average Case: Dalam kasus rata-rata, Bubble Sort memiliki kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam array. Bubble Sort akan melakukan perbandingan dan pertukaran elemen pada setiap pasangan elemen yang tidak berurutan.

Insertion Sort:
1. Worst Case: Dalam kasus terburuk, Insertion Sort memiliki kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam array. Hal ini terjadi ketika array dalam kondisi terbalik secara terbalik, dan setiap elemen perlu dipindahkan ke posisi yang benar, dengan memindahkan elemen sebelumnya satu per satu.
2. Best Case: Dalam kasus terbaik, Insertion Sort memiliki kompleksitas waktu O(n), di mana n adalah jumlah elemen dalam array. Ini terjadi ketika array sudah terurut secara menaik, sehingga tidak ada pemindahan elemen yang diperlukan selama iterasi.
3. Average Case: Dalam kasus rata-rata, Insertion Sort memiliki kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam array. Insertion Sort akan melakukan pemindahan elemen pada setiap elemen yang belum terurut selama iterasi.
  
Berikut analisis algorithm untuk mengevaluasi, Worst case, Best case, dan Average case pada sortest path:
1. Algoritma TSP (Brute Force):
Worst Case: Dalam kasus terburuk, algoritma TSP (Brute Force) memiliki kompleksitas waktu O(n!), di mana n adalah jumlah simpul dalam graf. Ini terjadi karena algoritma menguji setiap kemungkinan permutasi dari simpul-simpul yang ada.
Best Case: Dalam kasus terbaik, algoritma TSP (Brute Force) memiliki kompleksitas waktu O(n!), di mana n adalah jumlah simpul dalam graf. Ini karena algoritma harus memeriksa setiap kemungkinan permutasi.
Average Case: Dalam kasus rata-rata, algoritma TSP (Brute Force) juga memiliki kompleksitas waktu O(n!), di mana n adalah jumlah simpul dalam graf. Algoritma ini memeriksa setiap kemungkinan permutasi, yang menghasilkan kompleksitas waktu yang tinggi.

2. Algoritma Dijkstra:
Worst Case: Dalam kasus terburuk, algoritma Dijkstra memiliki kompleksitas waktu O((V + E) log V), di mana V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges) dalam graf. Ini terjadi ketika semua simpul dalam graf dihubungkan secara lengkap dan memiliki bobot tepi yang berbeda.
Best Case: Dalam kasus terbaik, algoritma Dijkstra memiliki kompleksitas waktu O((V + E) log V), di mana V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges) dalam graf. Ini terjadi ketika hanya ada sedikit simpul dan tepi dalam graf.
Average Case: Dalam kasus rata-rata, algoritma Dijkstra juga memiliki kompleksitas waktu O((V + E) log V), di mana V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges) dalam graf. Kompleksitas ini berlaku saat graf memiliki sejumlah simpul dan tepi dengan bobot yang beragam.
