import csv
import os
import time
subtotal = []
def utama():
 print ("*" *41)
 print ("** Hallo Selamat Datang **")
 print ("** Di Baby Care and Baby Supplies **")
 print ("*" *41) # Menu Awal
def menu_awal():
 utama()
 print("\t \t MENU LOGIN \t \t")
 dict_akses = {'a': "\t\t[1] Admin" , 'b': "\t\t[2] Pelanggan" ,
'c': "\t\t[0] Keluar"}
 print(dict_akses ['a'])
 print(dict_akses ['b'])
 print(dict_akses ['c'])
 print("\n")
 while True:
 try:
 selected = int(input("Masukkan Pilihan Anda : "))
 break
 except:
 print("Pilihan Berupa Angka!")
 print("\n")
 if selected == 1:
 login()
 elif selected == 2:
 show_barang()
 beli()
 elif selected == 0:
 print ("--Anda Keluar Dari Aplikasi--")
 time.sleep(5)
 exit()
 else:
 print("Anda memilih pilihan yang salah")
 kembali_menu_awal()
def kembali_menu_awal():
 print("\n")

 input("Tekan Enter untuk kembali...")
 menu_awal()
#Login Sebagai...
def login():
 username = 'admin'
 password = 12345
 while True:
 try:
 a = str(input("Masukkan Username anda : ")).lower()
 break
 except:
 print ("Inputan Berupa Huruf !")
 while True:
 try:
 b = int(input("Masukkan Password anda : "))
 break
 except:
 print ("Inputan Berupa Angka !") 
 if a!= username and b!= password:
 print("Username dan Password anda salah")
 return login()
 elif a== username and b== password:
 showmenu()
 else:
 balik_login()
def balik_login():
 print("\n")
 print("Username dan Password yg anda masukkan salah")
 login()
csv_filename = r"C:\Users\hp\Downloads\punya indah\Baby Care & Suppl
ies\toko.csv"
def bersihkan_layar():
 os.system("cls" if os.name == "nt" else "clear")
#Menu Admin
def showmenu ():
 bersihkan_layar()
 Brg = []
 with open(csv_filename, mode = "r") as csv_file:

 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 row_count = sum(1 for row in Brg)
 utama()
 print(" Info total barang :", row_count)
 print("=====================")
 print("[1] Lihat Daftar")
 print ("[2] Tambah Daftar")
 print ("[3] Edit Daftar")
 print ("[4] Hapus Daftar")
 print ("[5] Cari Daftar")
 print ("[6] Urutkan Daftar")
 print ("[0] Keluar \n")
 print ("========================")
 while True :
 try:
 pilih = int(input ("Pilih Menu >"))
 break
 except:
 print ("Inputan Berupa Angka !") 
 if pilih == 1:
 show_barang()
 kembali()
 elif pilih == 2:
 tambah_barang()
 elif pilih == 3:
 edit_barang()
 elif pilih == 4:
 hapus_barang()
 elif pilih == 5:
 cari_barang()
 elif pilih == 6:
 sorting()
 elif pilih == 0:
 print ("Anda telah keluar")
 kembali_menu_awal()
 else:
 print ("Memilih Menu salah")
 kembali()
def kembali():
 print("\n")

 input ("Tekan Enter Untuk Kembali...")
 showmenu()
def kembali_k():
 print("\n")
 input ("Tekan Enter Untuk Kembali...")
 kasir()
 
def show_barang():
 bersihkan_layar()
 Brg = []
 with open(csv_filename, mode = "r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 print("="*120)
 print("\t\t\t\t\t\tDaftar Stok Barang Toko")
 print("="*120)
 print("Kode \t NAMA \t\t\t HARGA \t\t Stok \t Jenis \t\t Bahan/K
andungan \t Kelebihan")
 print("="*120)
 #looping mengeluarkan data
 for data in Brg:
 print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARG
A']} \t {data['Stok']} \t {data['Jenis']} \t {data['Bahan/Kandungan'
]} \t\t {data['Kelebihan']} \t")
 print("=" * 120)
 
 
 
#Tambah Barang
def tambah_barang():
 bersihkan_layar()
 with open(csv_filename, mode= 'a', newline = '') as csv_file:
 fieldnames = ['Kode', 'NAMA', 'HARGA', 'Stok', 'Jenis', 'Bah
an/Kandungan', 'Kelebihan']
 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 print("==========================================")

 print("============Tambah Barang=================")
 print("==========================================\n")
 while True:
 try:
 kode = str (input("Kode: ")).upper()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True :
 try:
 nama = str (input("Nama Barang: ")).capitalize()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True :
 try:
 har = int (input ("Harga Barang: "))
 break
 except:
 print ("Inputan Berupa Angka !") 
 while True:
 try:
 stok = int (input("Stok Barang: "))
 break
 except:
 print ("Inputan Berupa Angka !") 
 while True:
 try:
 jen = str(input ("Jenis Barang: ")).capitalize()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True:
 try:
 Bahan = str (input("Bahan/Kandungan Barang: ")).capi
talize()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True:
 try:
 kel = str(input("Kelebihan Barang: ")).capitalize()
 break
 except:

 print ("Inputan Berupa Huruf !") 
 print ("============================================")
 writer.writerow({'Kode': kode, 'NAMA': nama, 'HARGA': har, '
Stok':stok, 'Jenis': jen, 'Bahan/Kandungan' : Bahan, 'Kelebihan' : k
el} )
 kembali()
#Metode Pencarian
def linearSearch(array, n, x):
 for i in range(0, n):
 if (array[i]["Kode"] == x):
 return i
 return -1
#Cari Daftar Barang
def cari_barang():
 bersihkan_layar()
 Brg =[]
 with open(csv_filename, mode = "r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 print("="*120)
 print("\t\t\t\t\t\tDaftar Stok Barang Toko")
 print("="*120)
 print("Kode \t NAMA \t\t\t HARGA \t\t Stok \t Jenis \t\t Bahan/K
andungan \t Kelebihan")
 print("="*120)
 #looping mengeluarkan data
 for data in Brg:
 print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARG
A']} \t {data['Stok']} \t {data['Jenis']} \t {data['Bahan/Kandungan'
]} \t\t {data['Kelebihan']} \t")
 print("=" * 120)
 
 while True:
 try:
 kode = str(input("Cari berdasarkan Kode> ")).upper()
 break

 except:
 print("Inputan Berupa Huruf !")
 n = len(Brg)
 result = linearSearch(Brg, n, kode)
 if(result == -1):
 print("MAAF DAFTAR TIDAK DITEMUKAN")
 else:
 print("Data DITEMUKAN: ")
 print(f"NAMA : {Brg[result]['NAMA']}")
 print(f"HARGA : Rp.{Brg[result]['HARGA']}")
 print(f"Stok : {Brg[result]['Stok']}")
 print(f"Jenis : {Brg[result]['Jenis']}")
 print(f"Bahan/Kandungan : {Brg[result]['Bahan/Kandungan']}")
 print(f"Kelebihan Barang : {Brg[result]['Kelebihan']}")
 kembali()
#Edit daftar barang
def edit_barang():
 bersihkan_layar()
 Brg = []
 with open(csv_filename, mode = "r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 print("="*120)
 print("\t\t\t\t\t\tDaftar Stok Barang Toko")
 print("="*120)
 print("Kode \t NAMA \t\t\t HARGA \t\t Stok \t Jenis \t\t Bahan/K
andungan \t Kelebihan")
 print("="*120)
 #looping mengeluarkan data
 for data in Brg:
 print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARG
A']} \t {data['Stok']} \t {data['Jenis']} \t {data['Bahan/Kandungan'
]} \t\t {data['Kelebihan']} \t")
 print("=" * 120)
 print("==========================================")
 print("============Edit Barang===================")

 print("==========================================\n")
 while True:
 try:
 kode = str (input("Pilih Kode Barang: ")).upper()
 break
 except:
 print ("Inputan Berupa Huruf !")
 n = len(Brg)
 result = linearSearch(Brg, n, kode)
 if(result == -1):
 print("MAAF KODE YANG DIINPUT SALAH")
 else:
 while True:
 try :
 kod = str (input("Kode Barang Baru: ")).upper()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True:
 try:
 nama = str (input("Nama Barang Baru: ")).capitalize
()
 break
 except:
 print ("Inputan Berupa Huruf !")
 while True:
 try: 
 har = int (input ("Harga Barang Baru: "))
 break
 except:
 print ("Inputan Berupa Angka !") 
 while True:
 try:
 stok = int (input("Stok Barang Baru: "))
 break
 except:
 print ("Inputan Berupa Angka !") 
 while True:
 try:
 jen = str(input ("Jenis Barang Baru: ")).capitalize( )
 break
 except:

 print ("Inputan Berupa Huruf !")
 while True:
 try: 
 Bahan = str (input("Bahan/Kandungan Barang Baru: "))
.capitalize()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 while True:
 try:
 kel = str(input("Kelebihan Barang Baru: ")).capitali
ze()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 indeks = 0
 for data in Brg :
 if data['Kode'] == kode:
 Brg[indeks]['Kode'] = kod
 Brg[indeks]['NAMA'] = nama
 Brg[indeks]['HARGA'] = har
 Brg[indeks]['Stok'] = stok
 Brg[indeks]['Jenis'] = jen
 Brg[indeks]['Bahan/Kandungan'] = Bahan
 Brg[indeks]['Kelebihan'] = kel
 indeks = indeks + 1
 #tulis yang baru
 with open(csv_filename, mode = 'w') as csv_file:
 fieldnames = ['Kode', 'NAMA', 'HARGA', 'Stok', 'Jenis',
'Bahan/Kandungan', 'Kelebihan'] 
 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 writer.writeheader()
 for data_baru in Brg:
 writer.writerow({'Kode': data_baru['Kode'], 'NAMA':
data_baru['NAMA'], 'HARGA': data_baru['HARGA'], 'Stok':data_baru['St
ok'], 'Jenis': data_baru['Jenis'], 'Bahan/Kandungan' : data_baru['Ba
han/Kandungan'], 'Kelebihan' : data_baru['Kelebihan']})
 kembali()
 
#Hapus Barang
def hapus_barang():
 bersihkan_layar()
 Brg = []
 with open(csv_filename, mode = "r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 print("="*120)
 print("\t\t\t\t\t\tDaftar Stok Barang Toko")
 print("="*120)
 print("Kode \t NAMA \t\t\t HARGA \t\t Stok \t Jenis \t\t Bahan/K
andungan \t Kelebihan")
 print("="*120)
 #looping mengeluarkan data
 for data in Brg:
 print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARG
A']} \t {data['Stok']} \t {data['Jenis']} \t {data['Bahan/Kandungan'
]} \t\t {data['Kelebihan']} \t")
 print("=" * 120)
 print("------------------------------")
 while True:
 try:
 kode = str(input("Hapus Barang Dengan KODE : ")).upper()
 break
 except:
 print ("Inputan Berupa Huruf !") 
 n = len(Brg)
 result = linearSearch(Brg, n, kode)
 if(result == -1):
 print("MAAF DAFTAR TIDAK DITEMUKAN")
 else:
 indeks = 0
 for data in Brg :
 if (data['Kode'] == kode):
 Brg.remove(Brg[indeks])
 indeks = indeks + 1
 with open(csv_filename, mode = 'w') as csv_file:
 fieldnames = ['Kode', 'NAMA', 'HARGA', 'Stok', 'Jenis',
'Bahan/Kandungan', 'Kelebihan'] 

 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 writer.writeheader()
 for data_baru in Brg:
 writer.writerow({'Kode': data_baru['Kode'], 'NAMA':
data_baru['NAMA'], 'HARGA': data_baru['HARGA'], 'Stok':data_baru['St
ok'], 'Jenis': data_baru['Jenis'], 'Bahan/Kandungan' : data_baru['Ba
han/Kandungan'], 'Kelebihan' : data_baru['Kelebihan']})
 print("Data Berhasil Dihapus")
 kembali()
 
def sorting():
 print("Mengurutkan Daftar Barang")
 sorting = "NAMA"
 print ("=============================================")
 print("Pilih Metode Pengurutan Nama Barang :\n [1] A ke Z \n [2]
Z ke A")
 while True:
 try:
 pilih = int(input("Masukkan Pilihan Metode :"))
 break
 except:
 print ("Inputan Berupa Angka !") 
 
 order = ""
 if pilih == 1:
 order = "Ascending"
 elif pilih == 2:
 order = "Descending"
 else:
 print("---Pilihan Yang Anda Masukkan Salah---")
 kembali()
 barang = []
 with open(csv_filename, mode="r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 barang.append(row)
 if len(barang) < 1:
 print("Error: Tidak ada daftar tersedia !")
 kembali()
 else:
 urut = []
 indeks = 0

 for data in barang:
 if sorting == "NAMA":
 urut.append([data["NAMA"], indeks]) 
 indeks += 1
 if sorting == "NAMA":
 insertionSort(urut, order)
 old_akun = barang.copy()
 barang.clear()
 for i in range(len(urut)):
 barang.append({"Kode": old_akun[urut[i][1]]["Kode"], "NA
MA": old_akun[urut[i][1]]["NAMA"],"HARGA": old_akun[urut[i][1]]["HAR
GA"],"Stok": old_akun[urut[i][1]]["Stok"], "Jenis": old_akun[urut[i] [1]]["Jenis"], "Bahan/Kandungan": old_akun[urut[i][1]]["Bahan/Kandun
gan"],"Kelebihan": old_akun[urut[i][1]]["Kelebihan"]})
 with open(csv_filename, mode = 'w') as csv_file:
 fieldnames = ['Kode', 'NAMA', 'HARGA', 'Stok', 'Jenis',
'Bahan/Kandungan', 'Kelebihan'] 
 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 writer.writeheader()
 for data_baru in barang:
 writer.writerow({'Kode': data_baru['Kode'], 'NAMA':
data_baru['NAMA'], 'HARGA': data_baru['HARGA'], 'Stok':data_baru['St
ok'], 'Jenis': data_baru['Jenis'], 'Bahan/Kandungan' : data_baru['Ba
han/Kandungan'], 'Kelebihan' : data_baru['Kelebihan']})
 print("Sukses: Daftar Barang berhasil diurutkan ") 
 
 kembali()
def insertionSort(array, order):
 for step in range(1, len(array)):
 key = array[step]
 j = step - 1
 if order == "Ascending":
 while j >= 0 and key < array[j]:
 array[j + 1] = array[j]
 j = j - 1
 array[j + 1] = key
 elif order == "Descending":
 while j >= 0 and key > array[j]:
 array[j + 1] = array[j]
 j = j - 1
 array[j + 1] = key

#Pelanggan
def kasir():
 bersihkan_layar()
 Brg =[]
 with open(csv_filename, mode = "r") as csv_file:
 csv_reader = csv.DictReader(csv_file)
 for row in csv_reader:
 Brg.append(row)
 print("="*120)
 print("\t\t\t\t\t\tDaftar Stok Barang Toko")
 print("="*120)
 print("Kode \t NAMA \t\t\t HARGA \t\t Stok \t Jenis \t\t Bahan/K
andungan \t Kelebihan")
 print("="*120)
 #looping mengeluarkan data
 for data in Brg:
 print(f"{data['Kode']} \t {data['NAMA']} \t\t Rp.{data['HARG
A']} \t {data['Stok']} \t {data['Jenis']} \t {data['Bahan/Kandungan'
]} \t\t {data['Kelebihan']} \t")
 print("=" * 120)
 
 
 totalharga = 0
 indeks = 0
 while True:
 try:
 kode = str (input("Kode Barang Yang Dibeli: ")).upper()
 break
 except:
 print ("Inputan Berupa Huruf !")
 n = len(Brg)
 result = linearSearch(Brg, n, kode)
 if(result == -1):
 print("MAAF NAMA YANG DIINPUTKAN SALAH")
 else:
 while True:

 try:
 jumlah = int(input ("Masukkan Banyak Barang :"))
 break
 except:
 print ("Inputan Berupa Angka !")
 for data in Brg :
 if data['Kode'] == kode:
 b= Brg[indeks]['HARGA']
 harga = int(b)
 a= Brg[indeks]['Stok']
 stok = int(a) - jumlah
 Brg[indeks]['Kode'] = Brg[indeks]['Kode']
 Brg[indeks]['NAMA'] = Brg[indeks]['NAMA']
 Brg[indeks]['HARGA'] = Brg[indeks]['HARGA']
 Brg[indeks]['Stok'] = stok
 Brg[indeks]['Jenis'] = Brg[indeks]['Jenis']
 Brg[indeks]['Bahan/Kandungan'] = Brg[indeks]['Bahan/
Kandungan']
 Brg[indeks]['Kelebihan'] = Brg[indeks]['Kelebihan']
 indeks = indeks + 1
 
 
 
 if jumlah <=int(a):
 subtot = harga*jumlah
 
 print("Subtotal Pembayaran adalah = ",subtot)
 print("Sisa stok kami saat ini : ",stok)
 print ("Subtotal Harga :",subtot)
 subtotal.append(subtot)
 for i in range(len(subtotal)):
 totalharga = subtotal[i]+totalharga
 print("Total Harga :",totalharga)
 with open(csv_filename, mode = 'w') as csv_file:
 fieldnames = ['Kode', 'NAMA', 'HARGA', 'Stok', 'Jeni
s', 'Bahan/Kandungan', 'Kelebihan'] 
 writer = csv.DictWriter(csv_file, fieldnames=fieldna
mes)
 writer.writeheader()
 for data_baru in Brg:

 writer.writerow({'Kode': data_baru['Kode'], 'NAM
A': data_baru['NAMA'], 'HARGA': data_baru['HARGA'], 'Stok':data_baru
['Stok'], 'Jenis': data_baru['Jenis'], 'Bahan/Kandungan' : data_baru
['Bahan/Kandungan'], 'Kelebihan' : data_baru['Kelebihan']})
 ulang()
 else:
 print("Mohon maaf anda melebihi batas stok kami saat ini
")
 kembali_k()
 
 
 x = 1
 while (x==1):
 try:
 print("Total Harga :",totalharga)
 bayar = float(input("Pembayaran : "))
 except ValueError:
 kembali_k()
 if(bayar >= totalharga):
 kembalian = bayar-totalharga
 print("Kembalian: Rp.",kembalian)
 x = 0
 Terimakasih()
 subtotal.clear()
 kembali_menu_awal()
 else:
 print("---
Maaf Uang Yang Dimasukkan Tidak Mencukupi ---")
 x = 1
 kembali_k() 
 
 
def ulang():
 jawab=str (input("Ingin Melakukan Pembelian Lagi ? (ya/tidak)"))
 if jawab == 'ya':
 kasir()
 elif jawab == 'tidak':
 print("-"* 45)
 else:
 print("--- Pilihan hanya ya/tidak ---")
 ulang()
def Terimakasih():
 print ("===============================")

 print ("| Terima kasih Telah Berbelanja |")
 print ("===============================")
def beli():
 beli = str (input("Apakah Anda Ingin Malakukan Pembelian ? (ya/t
idak)"))
 if beli == 'ya':
 kasir()
 elif beli == 'tidak':
 kembali_menu_awal()
 else:
 print("--- Pilihan hanya ya/tidak ---")
 ulang()
menu_awal()