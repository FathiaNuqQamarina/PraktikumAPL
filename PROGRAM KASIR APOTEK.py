import os
import time

Daftarstock_obat = ["Hufagrip pilek","Adem sari","Antangin JRG cair","Antimo anak","Antimo tablet","Hansaplast","Betadine 5 ml","Bodrek flu batuk","Bodrex Extra",
"Bodrex Migra","Bodrexyn tablet","Decolgen","Diapet","ENTROSTOP","ENTROSTOP Anak","Fatigon","GELIGA balsem","GPU minyak urut",
"Herocyn","INSTO tetes mata","Inzana","Kalpanak","KAPAK Minyak angin no. 6","Komik cair","Komix kids","Konidin tablet","Koyo Cabe","Balsem LANG 10 gr",
"Balsem LANG 20 gr","LANG KayuPutih no.3","LANG KayuPutih no.4","Laserin 30 ml","Laserin madu","Mixagrip","Neo NAPACIN","Neo Ultasiline","Neozep","OBH combi Batuk Flu","OBH Combi Batuk Flu anak",
"Oskadon","Paracetamol","Panadol biru","Panadol cold flu","Panadol Merah","Paramek","PROMAG","Remacyl","Salep 88","Salicyl","Salonpas","Sanaflu",
"Sangobion","Tolak angin cair","Tolak angin anak","Ultraflu","Vegeta","Vegeta Herbal"]

nama_obat = ["Hufagrip pilek","Adem sari","Antangin JRG cair","Antimo anak","Antimo tablet","Hansaplast","Betadine 5 ml","Bodrek flu batuk","Bodrex Extra",
"Bodrex Migra","Bodrexyn tablet","Decolgen","Diapet","ENTROSTOP","ENTROSTOP Anak","Fatigon","GELIGA balsem","GPU minyak urut",
"Herocyn","INSTO tetes mata","Inzana","Kalpanak","KAPAK Minyak angin no. 6","Komik cair","Komix kids","Konidin tablet","Koyo Cabe","Balsem LANG 10 gr",
"Balsem LANG 20 gr","LANG KayuPutih no.3","LANG KayuPutih no.4","Laserin 30 ml","Laserin madu","Mixagrip","Neo NAPACIN","Neo Ultasiline","Neozep","OBH combi Batuk Flu","OBH Combi Batuk Flu anak",
"Oskadon","Paracetamol","Panadol biru","Panadol cold flu","Panadol Merah","Paramek","PROMAG","Remacyl","Salep 88","Salicyl","Salonpas","Sanaflu",
"Sangobion","Tolak angin cair","Tolak angin anak","Ultraflu","Vegeta","Vegeta Herbal"]

harga_obat = [20000,3000,7000,5000,2000,20000,8000,8000,8000,9000,9000,5000,5000,6000,9000,20000,25000,25000,35000,12000,7000,30000,25000,3000,4000,3000,5000,8000,15000,30000,
50000,17000,20000,10000,13000,8000,5000,7000,9000,15000,20000,8000,10000,12000,12000,12000,7000,7000,12000,10000,3500,15000,8000,2500,4000,6000,8000]
subtotal = []

def Layar_Bersih():
    os.system('cls' if os.name == 'nt' else 'clear')

def awal():
    print("="*40)
    print("\t === Selamat Datang ===")
    print("\t   ==== APOTEK ====")
    print("\t   === KITA SEHAT ===")
    print("="*40)
    login()

def login():
    print ("---Silahkan Login Sebagai :---")
    dict_akses = {'a': "[1] Kostumer", 'b' : "[2] Admin Apotek", 'c': "[0] Keluar"}
    print (dict_akses ['a'])
    print (dict_akses ['b'])
    print (dict_akses ['c'])
    pilih_login = int (input("Masukkan Pilihan Akses Anda :"))
    if pilih_login == 1 :
        menukostumer()
    elif pilih_login == 2 :
        akses()
    elif pilih_login == 0:
        keluarapp()
        time.sleep(5)
        exit()
    else : 
        print ("--- Pilihan Yang Di Masukkan Salah ---")
        login()

def keluarapp():
    print("\tAnda Keluar Dari Aplikasi")
    print("-"* 40)

def akses(user='adminapotek',password=120902):
    Login = str (input("Masukkan Username yang tepat :"))
    kode = int (input("Masukkan Password yang tepat :"))

    if Login == user and kode == password:
        print("\tLogin Berhasil")
        print("\tSelamat Datang")
        input("Tekan ENTER untuk melanjutkan.....")
        menuadmin()
    elif Login == user and kode != password:
        kesalahan1()
    elif Login != user and kode == password:
        kesalahan2()
    else:
        print ("--- Maaf Inputan Yang Anda Masukkan SALAH ---")
        login()
    return (akses)

def kesalahan1():
    Layar_Bersih()
    print("--- Maaf Password yang anda masukkan SALAH ---")
    login()
def kesalahan2():
    Layar_Bersih()
    print("--- Maaf Username yang anda masukkan SALAH ---")
    login()



def menuadmin():
    print("\t---pilih menu---")
    print("-"* 44)
    tuple_menu = "[1] Daftar Obat Di Gudang ","[2] Input Daftar Baru","[3] Edit Daftar Obat","[4] Hapus Daftar Obat","[0] Keluar"
    d,e,f,g,h = tuple_menu
    print (d)
    print (e)
    print (f)
    print (g)
    print (h)
    Pilihan = int(input("Masukkan Pilihan Akses :"))

    if(Pilihan == 1):
        daftar_gudang()
        Kembali_menu()
    elif(Pilihan == 2):
        tambah_daftar()
        Kembali_menu()
    elif(Pilihan == 3):
        edit_daftar()
        Kembali_menu()
    elif(Pilihan == 4):
        hapus_daftar()
        Kembali_menu()
    elif (Pilihan == 0):
        keluar()
    else:
        print("--- Pilihan Salah ---")
        Kembali_menu()

def daftar_gudang():
    print("=====================================")
    print ("Pilihan Akses Daftar Obat di Gudang :\n [1] Lihat Daftar Terurut\n [2] Tambah Daftar Obat\n [3] Hapus Daftar Obat\n [4] Edit Daftar Obat\n [5] Cari Obat \n [0] Keluar")
    akse_gudang = int (input("Masukkan Pilihan Akses :"))
    if akse_gudang == 1:
        metodepengurutan()
        kembali_menu_g()
    elif akse_gudang == 2:
        tambah_daftar_gudang()
        kembali_menu_g()
    elif akse_gudang == 3:
        hapus_daftar_gudang()
        kembali_menu_g()
    elif akse_gudang == 4:
        edit_daftar_gudang()
        kembali_menu_g()
    elif akse_gudang == 5:
        cari_gudang()
        kembali_menu_g()
    elif akse_gudang == 0:
        menuadmin()
    else:
        print("---Pilihan Yang Anda Masukkan Salah---")
        daftar_gudang()


def lihat_daftar_gudang():
    Layar_Bersih()
    print ("--- Daftar Obat Yang Tersedia ---")
    if len(Daftarstock_obat)<=0:
         print("--- Belum Ada Data ---")
    else:
        for indeks in range(len(Daftarstock_obat)):
            print([indeks+1],Daftarstock_obat[indeks])

def tambah_daftar_gudang():
    Layar_Bersih()
    lihat_daftar_gudang()
    print("=====================================")
    obat_baru_gudang = str(input("Masukkan Nama Obat :"))
    Daftarstock_obat.append(obat_baru_gudang)
    print ("--- Daftar Berhasil Disimpan---")

def hapus_daftar_gudang():
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    lihat_daftar_gudang()
    print("====================================")
    indeks = int (input("Masukkan Nomor Obat :"))
    if(indeks > len(Daftarstock_obat)):
        print ("---- Nomor Salah ---")
    else:
       Daftarstock_obat.remove(Daftarstock_obat[indeks-1])
    print ("--- Daftar Berhasil Dihapus ---")

def edit_daftar_gudang():
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    lihat_daftar_gudang()
    print("====================================")
    indeks = int (input("Masukkan Nomor Obat :"))
    if(indeks > len(Daftarstock_obat)):
        print ("--- Nomor Salah ---")
    else:
        nama_Baru_gudang = str(input("Masukkan Nama Obat Baru :"))
        Daftarstock_obat[indeks-1] = nama_Baru_gudang
        print ("--- Daftar Berhasil Diperbaharui ---")

def metodepengurutan():
    print ("=============================================")
    print("Pilih Metode Pengurutan Nama Obat :\n [1] Ascending \n [2] Descending")
    urut = int(input("Masukkan Pilihan Metode :"))
    if urut == 1:
        insertionSortascen(Daftarstock_obat)
    elif urut == 2:
        insertion_sortdescen(Daftarstock_obat)
    else:
        print("---Pilihan Yang Anda Masukkan Salah---")
        metodepengurutan()


def insertionSortascen(array):
    for langkah in range(1, len(array)):
        kunci = array[langkah]
        j = langkah -1


        while j>= 0 and kunci < array[j]:
            array[j+1]= array[j]
            j = j-1


        array[j+1] = kunci
    print("=====================================")
    print('Daftar Obat Terurut secara Ascending:')
    for indeks in range(len(Daftarstock_obat)):
        print([indeks+1],Daftarstock_obat[indeks])

def insertion_sortdescen(array):
    for langkah in range(1,len(array)):
        kunci = array[langkah]
        j = langkah - 1
              
        while j >= 0 and kunci > array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = kunci

    print("=====================================")
    print('Daftar Obat Terurut secara Descending:')
    for indeks in range(len(Daftarstock_obat)):
        print([indeks+1],Daftarstock_obat[indeks])


def cari_gudang():
    lihat_daftar_gudang()
    print("===============================================")
    cari1 = str (input("Masukkan Data yang ingin dicari :"))
    result1 = linearSearch_obat(Daftarstock_obat, cari1)

    if (result1 == -1):
        print ("Obat Belum Tersedia Di Gudang")
    else:
        print ("Obat Yang di Cari Ditemukan, Berada Pada Nomor", result1)

def lihat_daftar():
    Layar_Bersih()
    print ("--- Daftar Obat Yang Tersedia ---")
    if len(nama_obat)<=0:
         print("--- Belum Ada Data ---")
    else:
        for indeks in range(len(nama_obat)):
            print([indeks+1],nama_obat[indeks],"\tRp.",harga_obat[indeks])
    

def tambah_daftar():
    Layar_Bersih()
    lihat_daftar()
    print("=====================================")
    obat_baru = str(input("Masukkan Nama Obat :"))
    Harga_baru = int(input("Masukkan Harga Obat :"))
    nama_obat.append(obat_baru)
    harga_obat.append(Harga_baru)
    print ("--- Daftar Berhasil Disimpan---")
    
def edit_daftar():
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    lihat_daftar()
    print("====================================")
    indeks = int (input("Masukkan Nomor Obat :"))
    if(indeks > len(nama_obat)):
        print ("--- Nomor Salah ---")
    else:
        nama_Baru = str(input("Masukkan Nama Obat Baru :"))
        harga_baru = int(input("Masukkan Harga Obat Baru :"))
        nama_obat[indeks-1] = nama_Baru
        harga_obat[indeks-1] = harga_baru
        print ("--- Daftar Berhasil Diperbaharui ---")

def hapus_daftar():
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    Layar_Bersih()
    lihat_daftar()
    print("====================================")
    indeks = int (input("Masukkan Nomor Obat :"))
    if(indeks > len(nama_obat)):
        print ("---- Nomor Salah ---")
    else:
       nama_obat.remove(nama_obat[indeks-1])
       harga_obat.remove(harga_obat[indeks-1])
    print ("--- Daftar Berhasil Dihapus ---")


def keluar():
    Layar_Bersih()
    print("\tAnda Keluar Dari Aplikasi")
    print("-"* 40)
    login()

def Kembali_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menuadmin()

def kembali_menu_g():
    print("\n")
    input("Tekan Enter Untuk kembali...")
    daftar_gudang()

def Kembali_kasir():
    print("\n")
    masukkan()

def Terimakasih():
    print("="* 46)
    print("\tTerima kasih telah Berbelanja")
    print("\t             Di")
    print("\t   ---APOTEK KITA SEHAT---")
    print("="* 46)

def menukostumer():
    print("\t---pilih menu---")
    print("+"* 44)
    tuple_menu2 = "[1] Lihat Daftar Obat", "[2] Berbelanja", "[3] Cari Obat"
    k,l,m = tuple_menu2
    print(k)
    print (l)
    print(m)
    p_kostumer = int (input("Masukkan Pilihan Anda :"))
    if p_kostumer == 1:
        lihat_daftar()
        Kembali_menuk()
    elif p_kostumer == 2:
        masukkan()
    elif p_kostumer == 3:
        cari()
        Kembali_menuk()
    else :
        print ("--- Maaf Pilihan Yang Anda Masukkan Salah---")
        menukostumer()

def Kembali_menuk():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menukostumer()


def kasir(harga,jumlah):  
    return harga*jumlah

def linearSearch_obat(array, x):
    for i in range(len(array)):
        if (array[i] == x):
            return i + 1
    return -1

def cari():
    lihat_daftar()
    print("===============================================")
    cari = str (input("Masukkan Data yang ingin dicari :"))
    result = linearSearch_obat(nama_obat, cari)

    if (result == -1):
        print ("Maaf Obat Belum Tersedia")
    else:
        print ("Obat Yang di Cari Ditemukan, Berada Pada Nomor", result)

def masukkan():
    lihat_daftar()
    totalharga = 0
    global harga,jumlah 
    print ("----------------------------------------")
    codeobat= int(input("Masukkan Nomor Obat yang ingin dibeli :"))
    jumlah = int (input("Masukkan Jumlah Obat yang ingin dibeli :"))
    harga = harga_obat[codeobat-1]

    if(codeobat > len(nama_obat)or jumlah<=0):
        print ("--- Maaf Inputan Yang Anda Masukkan SALAH ---")
        tetap()

    else:
        subtot = kasir(harga,jumlah)
        print ("Obat yang dibeli :",nama_obat[codeobat-1],"Rp.",harga_obat[codeobat-1])
        print ("Subtotal Harga :",subtot)
        subtotal.append(subtot)
        for i in range(len(subtotal)):
            totalharga = subtotal[i]+totalharga
        print("Total Harga :",totalharga)
        ulang()
        
        x = 1
        while (x==1):
            try:
                print("Total Harga :",totalharga)
                bayar = float(input("Pembayaran : "))
            except ValueError:
                Kembali_kasir()

            if(bayar >= totalharga):
                kembalian = bayar-totalharga
                print("Kembalian: Rp.",kembalian)
                x = 0
                Terimakasih()
                subtotal.clear()
                login()
            else:
                print("--- Maaf Uang Yang Dimasukkan Tidak Mencukupi ---")
                x = 1

def tetap():
        lagi = str(input("Tetap Melakukan Pembelian (ya/tidak) : "))
        if lagi == 'ya':
            Kembali_kasir()
        elif lagi == 'tidak':
            ulang()
        else:
            print("--- Pilihan hanya ya/tidak ---")
            tetap()

def ulang():
    jawab=str (input("Ingin Melakukan Pembelian Lagi ? (ya/tidak)"))
    if jawab == 'ya':
        masukkan()
    elif jawab == 'tidak':
        print("-"* 40)
    else:
       print("--- Pilihan hanya ya/tidak ---")
       ulang()

awal()

