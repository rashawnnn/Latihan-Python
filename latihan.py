# print("Hello World")
# print (50+50)

# apel = 20
# jeruk = 25
# print(apel + jeruk)

# hutang = 5000000
# bayar = 5000000
# sisa_hutang = hutang - bayar
# print("Sisa Hutang Anda =", sisa_hutang)

# panjang = 8
# lebar = 4
# luas = panjang * lebar
# print("Luas Persegi Panjang =", luas)

# bilangan1 = 10
# bilangan2 = 5
# hasil = bilangan1 % bilangan2
# print("Sisa bagi dari Bilangan", bilangan1, "dan", bilangan2, "adalah", hasil)

# bilangan3 = 5
# bilangan4 = 2
# hasil = bilangan3 ** bilangan4
# print ("Hasil dari", bilangan3, "pangkat", bilangan4, "adalah", hasil)

# bil1 = input("Masukkan Bilangan 1: ")
# bil2 = input("Masukkan Bilangan 2: ")
# jumlah = int(bil1) + int(bil2)
# print("Hasil dari", bil1, "+", bil2, "adalah", jumlah)

# bil1 = float(input("Masukkan Bilangan 1: "))
# bil2 = float(input("Masukkan Bilangan 2: "))
# jumlah = (bil1) + (bil2)
# print("Hasil dari", bil1, "+", bil2, "adalah", jumlah)

# Konversi Tipe Data
# String
# bil1 = "10"
# # Integer
# bil2 = int(bil1)
# # float
# bil3 = float(bil2)
# print(bil3)

# # Variabel
# # namaMahasiswa = "Rizky"
# # snake_case = untuk nama variabel dan function
# nama_mahasiswa = "Rizky"
# # PascalCase = untuk nama class
# NamaMahasiswa = "Rizky"
# # UPPERCASE : untuk nama constant
# PI = 3.14

# Operator String
# teks = "Python"
# print(teks[0])
# print(teks[-1])
# print(teks[3:5])

# List
# buah = ["apel", "jeruk","mangga", "durian"]
# (0(1))
# salin = buah
# salin.append("anggur")
# print(buah)

# buah = ["apel", "jeruk","mangga", "durian"]
# extend menambahkan lebih dari 1 item diakhir
# buah.extend("anggur", "kiwi")
# print(buah)

# Tuple
# warna = ("merah", "kuning", "hijau")
# print(warna[0])

# ubah warna
# warna = ("merah", "kuning", "hijau")
# ubah = list(warna)
# ubah[0] = "biru"
# warna = tuple(ubah)
# print(warna)

# warna = ("warna",)
# print(type(warna))

# Set
# angka = {1, 2, 3, 4, 5}
# angka.append(6)
# print(angka)

# menambahkan nilai yang sama
# angka = [1, 2, 3, 4, 5]
# angka.append(2)
# print(angka)

# dictionary
# mahasiswa = {
#     "nama": "Rizky",
#     "umur": 20,
#     "nim": "123",
#     "alamat": "Bandung"
# }
# print(mahasiswa["nama"])

# mahasiswa = {}
# mahasiswa["Jurusan"] = "Informatika"
# print(mahasiswa)

# data = {(1,2): "Angka"}
# print(data)

# array
# data = [1, 2, 3, 4, 5]
# akses index pertama
# print(data[0]) # O(N)
# tambah elemen
# data.append(6) # tambah elemen
# print(data)

# Akses Elemen
# buah = ["apel", "mangga", "jeruk"]
# print(buah[1])      # Output: Mangga
# buah[2] = "pisang"  # ubah elemen
# print(buah)

# Operasi Linear : Kompleksitas O(n) untuk implementasi pencarian linear
# def cari_elemen(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return i
#     return -1
    
# angka = [10, 20, 30, 40]
# print(cari_elemen(angka, 30)) # data yang ada di index ke 2

# def cari_huruf(teks, target):
#     for i in range(len(teks)):
#         if teks[i] == target:
#             return i
#     return -1
    
# kata = list("python")
# print(cari_huruf(kata, "t"))

# def cari_maksimum(data, target):
#      for i in range(len(data)):
#          if data[i] == target:
#              return i
#      return -1
    
# angka = [15, 20, 65, 10, 45]
# nilai_terbesar = max(angka)
# print(nilai_terbesar)

# def cari_maksimum(data, target):
#       for i in range(len(data)):
#           if data[i] == target:
#               return i
#       return -1
    
# angka = [15, 20, 65, 10, 45]
# nilai_terbesar = max(angka)
# print(nilai_terbesar)

# def cari_genap(data):
#       for i in range(len(data)):
#           if data[i] % 2 == 0:
#               return data[i]
#       return -1
    
# angka = [15, 21, 65, 10, 45]
# print(cari_genap(angka))

# def cari_kapital(teks):
#       for i in range(len(teks)):
#           if teks[i].isupper():
#               return teks[i]
#       return -1
    
# kata = list("pythonIsfun")
# print(cari_kapital(kata))

# def cari_posisi(data, huruf):
#     posisi = []
#     for i in range(len(data)):
#         if data[i] == huruf:
#             posisi.append(i)
#     return posisi

# data = ["a", "b", "a", "c", "a"]
# print(cari_posisi(data, "a"))

# stack = []

# #push: menambah elemen ke puncak (append)
# stack.append(10)    # stack = [10]
# stack.append(20)
# stack.append(30)
# print("Stack sekarang:", stack)

# #pop: menghapus elemen dari puncak
# atas = stack.pop() # atas = 30, stack = [10, 20]
# print("Setelah pop:", atas)
# print("Stack sekarang:", stack)

# #peek: melihat elemen puncak
# puncak = stack[-1] # puncak = 20
# print("Elemen teratas:", puncak)

# #isEmpty: cek apakah kosong type datanya boolean
# if len(stack) == 0:
#     print("Stack kosong")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
#Uji program
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# print("Isi stack:", s.items)
# print("Elemen teratas:", s.peek())
# s.pop()
# print("Setelah pop:", s.items)

#Queue
# from collections import deque

# class RumahSakitQueue:
#     def __init__(self):
#         self.antrian = deque()

#     # def daftar(self, nama_pasien, prioritas=False):
#     #     if prioritas:
#     #         self.antrian.appendleft((nama_pasien, "PRIORITAS"))
#     #     else:
#     #         self.antrian.append((nama_pasien, "UMUM"))

#     def daftar(self, nama_pasien, kategori="UMUM"):
#         # Aturan Prioritas
#         # Prioritas Paling Depan
#         # BPJS di Tengah
#         # Umum Paling Belakang
#         if kategori.upper() == "PRIORITAS":
#             self.antrian.appendleft((nama_pasien, "PRIORITAS"))
#         elif kategori.upper() == "BPJS":
#             # sisipkan BPJS setelah semua PRIORITAS, sebelum UMUM
#             temp = deque()
#             # pindahkan pasien PRIORITAS ke temp
#             while self.antrian and self.antrian[0][1] == "PRIORITAS":
#                 temp.append(self.antrian.popleft())
#             # tambahkan pasien BPJS
#             self.antrian.appendleft((nama_pasien, "BPJS"))
#             #tambahkan kembali pasien PRIORITAS
#             while temp:
#                 self.antrian.appendleft(temp.popleft())
#         else:
#             self.antrian.append((nama_pasien, "UMUM"))

#     def layani(self):
#         if not self.antrian:
#             return "Tidak ada pasien."
#         nama, jenis = self.antrian.popleft()
#         return f"Memanggil: {nama} ({jenis})"
    
#     def sisa_antrian(self):
#         return list(self.antrian)
    
#     #Simulasi
# rs = RumahSakitQueue()
# rs.daftar("Ali");
# rs.daftar("Budi")
# rs.daftar("Citra", "PRIORITAS")
# rs.daftar("Dina", "BPJS")
# rs.daftar("Fajar", "BPJS")
# rs.daftar("Eko", "UMUM")
# print(rs.layani())
# print(rs.layani())
# print(rs.sisa_antrian())

# def linear_search(data, target):
#     """Mencari target dalam list dengan metode Linear Search"""
#     for i in range(len(data)):
#         if data[i] == target:
#             return i # posisi ditemukan
#     return -1 # tidak ditemukan
    
# angka = [ 5, 2, 8, 1, 4, 9, 1]
# print("Posisi angka 1:", linear_search(angka, 1))
# print("Posisi angka 7:", linear_search(angka, 7))

# Uji
# def hitung_huruf(data, target):
#     jumlah = 0 
    
#     for i in range(len(data)):
#         if data[i] == target:
#             jumlah += 1
            
#     return jumlah

# huruf = ["a", "b", "a", "c", "d", "a", "a"]
# print("Jumlah huruf a:", hitung_huruf(huruf, "a"))
# print("Jumlah huruf f:", hitung_huruf(huruf, "f"))

# Coba cari username dari data tersebut
# user = ["admin", "dani", "Totok", "susi"]
# Kemudian untuk mencari apakah user dengan "totok" ada?
# memanfaatkan case sensitive
# def cek(user, target):
#     for i in user:
#         if i.lower() == target.lower():
#             # return "User ditemukan"
#             return False
#         return True
#     # return "User tidak ditemukan"

# print(cek(user, "totok"))

# List terurut untuk Binary Search
data = [2,  4, 6, 8, 10, 12, 14, 16, 18, 20]
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Cek indeks {mid}, nilai {data[mid]}") # debug langkah

        if data[mid] == target:
            return f"{target} ditemukan di indeks {mid}"  # posisi ditemukan
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"{target} tidak ditemukan"
target = int(input("Masukkan angka yang dicari: "))
print(binary_search(data, target))

