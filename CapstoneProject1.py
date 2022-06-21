'''
Muhammad Rafi Amiruddin
Capstone Project Module 1
JC Data Science and Machine Learning
'''

def showData(barang): # Function untuk menampilkan Data
    print('''
                ***** Daftar Barang Toko Interstellar *****
''')
    print('| Nomor Data\t| Kode Barang \t| Barang  \t| Stock\t| Harga(Rp) \t| Warna  \t|')
    for i in range(len(barang)) :
        print(f"| {i+1}     \t| {barang[i]['Kode Barang']}\t\t| {barang[i]['Barang']}   \t| {barang[i]['Stock']}\t| {barang[i]['Harga']}  \t| {barang[i]['Warna']}  \t|")

def checkExitRead(): # Function untuk konfirmasi Exit pada Menu Read
    while True:
        checkExit = input("\nApakah anda yakin ingin keluar dari Menu Read? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak':
            return menuRead()
        else:
            print('''
            ====================================
            Masukkan PILIHAN ENTRY dengan benar!
            ====================================''')

def checkExitCreate(): # Function untuk konfirmasi Exit pada Menu Create
    while True:
        checkExit = input("\nApakah anda yakin ingin keluar dari Menu Create? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak':
            return menuCreate()
        else:
            print('''
            ====================================
            Masukkan PILIHAN ENTRY dengan benar!
            ====================================''')

def checkExitUpdate(): # Function untuk konfirmasi Exit pada Menu Update
    while True:
        checkExit = input("\nApakah anda yakin ingin keluar dari Menu Update? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak':
            return menuUpdate()
        else:
            print('''
            ====================================
            Masukkan PILIHAN ENTRY dengan benar!
            ====================================''')

def checkExitDelete(): # Function untuk konfirmasi Exit pada Menu Delete
    while True:
        checkExit = input("\nApakah anda yakin ingin keluar dari Menu Delete? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak':
            return menuDelete()
        else:
            print('''
            ====================================
            Masukkan PILIHAN ENTRY dengan benar!
            ====================================''')

def checkExitTransaksi(): # Function untuk konfirmasi Exit pada Menu Transaksi
    while True:
        checkExit = input("\nApakah anda yakin ingin keluar dari Menu Transaksi? (ya/tidak) : ").lower()
        if checkExit == 'ya':
            break
        elif checkExit == 'tidak':
            return menuTransaksi()
        else:
            print('''
            ====================================
            Masukkan PILIHAN ENTRY dengan benar!
            ====================================''')

def errorEntry(): # Function template notifikasi Error
    print('''
        =================================
                   ERROR ENTRY!
        Masukkan ANGKA menu dengan benar!
        =================================''')

def inputKodeBarang(): # Function untuk check tipe data input Value kolom Kode Barang
    while True:
        kodeBarang = input('\nMasukkan nomor Kode Barang : ')
        x = kodeBarang.isnumeric()
        if x == True:
            x = kodeBarang
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN ANGKA!
            =====================''')

def inputNamaBarang(): # Function untuk check tipe data input kolom Value Barang
    while True:
        namaBarang = input('Masukkan Nama Barang : ').capitalize()
        x = namaBarang.isnumeric()
        if x == False:
            x = namaBarang
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN HURUF!
            =====================''')

def inputStockBarang(): # Function untuk check tipe data input Value kolom Stock
    while True:
        stockBarang = input('Masukkan Stock Barang : ')
        x = stockBarang.isnumeric()
        if x == True:
            x = int(stockBarang)
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN ANGKA!
            =====================''')

def inputHargaBarang(): # Function untuk check tipe data input Value kolom Harga
    while True:
        hargaBarang = input('Masukkan Harga Barang : ')
        x = hargaBarang.isnumeric()
        if x == True:
            x = int(hargaBarang)
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN ANGKA!
            =====================''')

def inputWarnaBarang(): # Function untuk check tipe data input Value kolom Warna
    while True:
        warnaBarang = input('Masukkan Warna Barang : ').capitalize()
        x = warnaBarang.isnumeric()
        if x == False:
            x = warnaBarang
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN HURUF!
            =====================''')

def updateBarangBaru(data): # Function untuk update Value kolom Barang
    barangBaru = inputNamaBarang()
    print('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock \t| Harga(Rp) \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}       \t| {barangBaru}      \t| {data[i]['Stock']}      \t| {data[i]['Harga']}      \t| {data[i]['Warna']}")
    while True:
        checkUpdate = input("\nApakah anda sudah yakin untuk mengupdate data tersebut? (ya/tidak) : ").lower()
        if checkUpdate == 'ya':
            data[0]['Barang'] = barangBaru
            showData(listBarang)
            print('''
                            ==============
                            DATA TERUPDATE
                            ==============''')
            return menuUpdate()
        elif checkUpdate == 'tidak':
            return menuUpdate()
        else:
            print('''
                    ====================================
                    Masukkan PILIHAN ENTRY dengan benar!
                    ====================================''')

def updateStockBaru(data): # Function untuk update Value kolom Stock
    stockBaru = inputStockBarang()
    print('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock \t| Harga \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}       \t| {data[i]['Barang']}      \t| {stockBaru}      \t| {data[i]['Harga']}      \t| {data[i]['Warna']}")
    while True:
        checkUpdate = input("\nApakah anda sudah yakin untuk mengupdate data tersebut? (ya/tidak) : ").lower()
        if checkUpdate == 'ya':
            data[0]['Stock'] = stockBaru
            showData(listBarang)
            print('''
                            ==============
                            DATA TERUPDATE
                            ==============''')
            return menuUpdate()
        elif checkUpdate == 'tidak':
            return menuUpdate()
        else:
            print('''
                    ====================================
                    Masukkan PILIHAN ENTRY dengan benar!
                    ====================================''')

def updateHargaBaru(data): # Function untuk update Value kolom Harga
    hargaBaru = inputHargaBarang()
    print('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock \t| Harga \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}       \t| {data[i]['Barang']}      \t| {data[i]['Stock']}      \t| {hargaBaru}      \t| {data[i]['Warna']}")
    while True:
        checkUpdate = input("\nApakah anda sudah yakin untuk mengupdate data tersebut? (ya/tidak) : ").lower()
        if checkUpdate == 'ya':
            data[0]['Harga'] = hargaBaru
            showData(listBarang)
            print('''
                            ==============
                            DATA TERUPDATE
                            ==============''')
            return menuUpdate()
        elif checkUpdate == 'tidak':
            return menuUpdate()
        else:
            print('''
                    ====================================
                    Masukkan PILIHAN ENTRY dengan benar!
                    ====================================''')

def updateWarnaBaru(data): # Function untuk update Value kolom Warna
    warnaBaru = inputWarnaBarang()
    print('\nNomor Data \t| Kode Barang \t| Barang  \t| Stock \t| Harga \t| Warna')
    for i in range(len(data)) :
        print(f"{i+1}       \t| {data[i]['Kode Barang']}       \t| {data[i]['Barang']}      \t| {data[i]['Stock']}      \t| {data[i]['Harga']}      \t| {warnaBaru}")
    while True:
        checkUpdate = input("\nApakah anda sudah yakin untuk mengupdate Kolom Data tersebut? (ya/tidak) : ").lower()
        if checkUpdate == 'ya':
            data[0]['Warna'] = warnaBaru
            showData(listBarang)
            print('''
                            ==============
                            DATA TERUPDATE
                            ==============''')
            return menuUpdate()
        elif checkUpdate == 'tidak':
            return menuUpdate()
        else:
            print('''
                ====================================
                Masukkan PILIHAN ENTRY dengan benar!
                ====================================''')

def deleteData(data, kode): # Function untuk delete data spesifik
    for i in range(len(data)):
        if data[i]['Kode Barang'] == kode:
            del data[i]
            break
    showData(data)
    print('''
                            ============
                            DATA DELETED
                            ============''')
    return menuDelete()

# Function untuk Menu Read
def menuRead(): 
    menuPencarian = input('''
Menu Pencarian Daftar Penjualan Barang

1. Daftar Penjualan Barang
2. Mencari Daftar Barang
3. Exit Menu Pencarian

Masukkan angka Menu yang ingin dijalankan : ''')

    if menuPencarian == '1':
        if len(listBarang) == 0:
            print('''\n
            ==============
            TIDAK ADA DATA
            ==============
            ''')
            return menuRead()
        else:
            showData(listBarang) # line 7
            return menuRead()
    elif menuPencarian == '2':
        if len(listBarang) == 0:
            print('''
            ==============
            TIDAK ADA DATA
            ==============''')
            menuRead()
        else:
            kodeBarang = inputKodeBarang() # line 87
            pencarianData = (list(filter(lambda data: data['Kode Barang'] == kodeBarang, listBarang)))
            if len(pencarianData):
                showData(pencarianData)
                return menuRead()
            else:
                print('''
            ==============
            TIDAK ADA DATA
            ==============''')
            return menuRead()
    elif menuPencarian == '3':
        return checkExitRead() # line 15
    else:
        errorEntry() # line 80
        return menuRead()

# Function untuk Menu Create
def menuCreate() :
    menuTambahBarang = input('''
Menu Tambah Daftar Barang:
    
1. Tambah Daftar Barang
2. Exit Menu Tambah Barang

Masukkan angka Menu yang ingin dijalankan: ''')

    if menuTambahBarang == '1':
        kodeBarang = inputKodeBarang() # line 87
        pencarianData = list(filter(lambda data: data['Kode Barang'] == kodeBarang, listBarang))
        if len(pencarianData):
            showData(pencarianData)
            print('''
                            ==============
                            DATA SUDAH ADA
                            ==============''')
            return menuCreate()
        else:
            namaBarang = inputNamaBarang() # line 100
            stockBarang = inputStockBarang() # line 113
            hargaBarang = inputHargaBarang() # line 126
            warnaBarang = inputWarnaBarang() # line 139
            listBarangBaru = [{
            'Kode Barang': kodeBarang,
            'Barang': namaBarang,
            'Stock': stockBarang,
            'Harga': hargaBarang,
            'Warna': warnaBarang
            }]
            showData(listBarangBaru) # line 7
            while True:
                tambahData = input("\nApakah anda yakin ingin menambahkan Data Barang tersebut? (ya/tidak) : ").lower()
                if tambahData == 'ya':
                    listBarang.extend(listBarangBaru)
                    showData(listBarang)
                    print('''
                                ==============
                                DATA TERSIMPAN
                                ==============''')
                    return menuCreate()
                elif tambahData == 'tidak':
                    return menuCreate()
                else:
                    print('''
                ====================================
                Masukkan PILIHAN ENTRY dengan benar!
                ====================================''')
    elif menuTambahBarang == '2':
        return checkExitCreate() # line 28
    else:
        errorEntry() # line 80
        return menuCreate()

# Function untuk Menu Update
def menuUpdate() :
    while True:
        menuUpdateBarang = input('''
Menu Update Daftar Barang:

1. Update Data Barang
2. Exit Menu Update

Masukkan angka Menu yang ingin dijalankan: ''')

        if menuUpdateBarang == '1':
            if len(listBarang) == 0:
                print('''
                    ==================================
                                DATA KOSONG! 
                    MOHON INPUT DATA TERLEBIH DAHULU
                    ==================================''')
                break
            else: 
                showData(listBarang) # line 7
                kodeBarang = inputKodeBarang() # line 87
                pencarianData = list(filter(lambda data: data['Kode Barang'] == kodeBarang, listBarang))
                if len(pencarianData):
                    showData(pencarianData)
                    while True:
                        updateData = input("\nApakah anda yakin ingin mengubah Data Barang tersebut? (ya/tidak) : ").lower()
                        if updateData == 'ya':
                            while True:
                                updateBarang = input("\nMasukkan nama kolom data yang ingin diubah (barang/stock/harga/warna) : ").lower()
                                if updateBarang == 'barang':
                                    updateBarangBaru(pencarianData) # line 152
                                    break
                                elif updateBarang == 'stock':
                                    updateStockBaru(pencarianData) # line 175
                                    break
                                elif updateBarang == 'harga':
                                    updateHargaBaru(pencarianData) # line 198
                                    break
                                elif updateBarang == 'warna':
                                    updateWarnaBaru(pencarianData) # line 221
                                    break
                                else:
                                    print('''
                                =======================================
                                MOHON MASUKKAN NAMA KOLOM DENGAN BENAR!
                                =======================================''')
                        elif updateData == 'tidak':
                            return menuUpdate()
                        else:
                            print('''
                        ====================================
                        Masukkan PILIHAN ENTRY dengan benar!
                        ====================================''')
                        break
                else:
                    print('''
                    =============================
                    DATA YANG ANDA CARI TIDAK ADA
                    =============================''')
                    return menuUpdate()
                break
        elif menuUpdateBarang == '2':
            return checkExitUpdate() # line 41
        else:
            errorEntry() # line 80
            return menuUpdate()

# Function untuk Menu Delete
def menuDelete() :
    while True:
        menuHapusBarang = input('''
Menu Delete Daftar Barang:

1. Hapus Data Barang
2. Exit Menu Hapus Data

Masukkan angka Menu yang ingin dijalankan: ''')

        if menuHapusBarang == '1':
            if len(listBarang) == 0:
                print('''
                    ==================================
                                DATA KOSONG! 
                    MOHON INPUT DATA TERLEBIH DAHULU
                    ==================================''')
                break
            else:
                showData(listBarang) # line 7
                kodeBarang = inputKodeBarang()
                pencarianData = (list(filter(lambda data: data['Kode Barang'] == kodeBarang, listBarang)))
                if len(pencarianData):
                    showData(pencarianData)
                    while True:
                        hapusData = input("\nApakah anda yakin ingin menghapus Data Barang tersebut? (ya/tidak) : ").lower()
                        if hapusData == 'ya':
                            deleteData(listBarang, kodeBarang) # line 244
                            break
                        elif hapusData == 'tidak':
                            return menuDelete()
                        else:
                            print('''
                        ====================================
                        Masukkan PILIHAN ENTRY dengan benar!
                        ====================================''')
                else:
                    print('''
                    ==============
                    DATA TIDAK ADA
                    ==============''')
                    return menuDelete()
                break
        elif menuHapusBarang == '2':
            return checkExitDelete() # line 54
        else:
            errorEntry() # line 80
            return menuDelete()

def inputNomorData(): # Function untuk cek input value Nomor Data
    while True:
        nomorData = input('\nMasukkan Nomor Data barang yang ingin dibeli : ')
        x = nomorData.isnumeric()
        if x == True:
            x = int(nomorData)
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN ANGKA!
            =====================''')

def inputQtyBarang(): # Function untuk cek input value Qty Barang
    while True:
        qtyBarang = input('\nMasukkan jumlah yang ingin dibeli : ')
        x = qtyBarang.isnumeric()
        if x == True:
            x = int(qtyBarang)
            return x
        else:
            print('''
            =====================
            HANYA MASUKKAN ANGKA!
            =====================''')

# Function untuk Menu Transaksi
def menuTransaksi() :
    menuJualBeli = input('''
Menu pembelian barang:

1. Membeli barang
2. Exit Menu Pembelian

Masukkan angka Menu yang ingin dijalankan : ''')

    if menuJualBeli == '1':
        if len(listBarang) == 0:
            print('''
            ==============================
            MOHON MAAF, STOCK BARANG HABIS
            ==============================''')
            return menuTransaksi()
        else:
            showData(listBarang) # line 7
        while True :
            nomorData = inputNomorData() # line 477
            if 1 <= nomorData <= len(listBarang):
                if listBarang[nomorData-1]['Stock'] == 0:
                    print(f'''
                    ===================================
                    Mohon maaf stock {listBarang[nomorData-1]['Barang']} telah habis
                    ===================================''')
                    return menuTransaksi()
                qtyBarang = inputQtyBarang() # line 490
                if(qtyBarang > listBarang[nomorData-1]['Stock']) :
                    print(f"""
                    ================================================
                    Stock barang tidak cukup, stock {listBarang[nomorData-1]['Barang']} sisa: {listBarang[nomorData-1]['Stock']}
                    ================================================""")
                    return menuTransaksi()
                else :
                    keranjang.append({
                        'Barang': listBarang[nomorData-1]['Barang'],
                        'Warna': listBarang[nomorData-1]['Warna'],
                        'Qty': qtyBarang, 
                        'Harga': listBarang[nomorData-1]['Harga'], 
                        'Nomor Data': nomorData-1
                    })
            else:
                print('''
                ======================================
                MOHON MASUKKAN NOMOR DATA DENGAN BENAR
                ======================================''')
                continue

            print('\nIsi Keranjang :')
            print('\nBarang\t| Warna    \t| Qty\t| Harga(Rp)')
            for item in keranjang :
                print(f"{item['Barang']}\t| {item['Warna']}     \t| {item['Qty']}\t| {item['Harga']}")
            check_keranjang = input('\nApakah anda ingin membeli barang yang lain? (ya/tidak) : ').lower()
            if check_keranjang == 'tidak':
                break

    elif menuJualBeli == '2':
        return checkExitTransaksi() # line 67
    else:
        errorEntry()
        return menuTransaksi()

    print('\nDaftar Belanja :')
    print('\nBarang\t| Warna        \t| Qty\t| Harga(Rp)   \t| Total Harga')
    totalHarga = 0
    for item in keranjang :
        print(f"{item['Barang']}\t| {item['Warna']}     \t| {item['Qty']}\t| {item['Harga']}\t| {item['Qty'] * item['Harga']}")
        totalHarga += item['Qty'] * item['Harga']    
    while True :
        print(f"\nTotal belanja yang harus dibayarkan = {totalHarga}")
        jumlahUang = int(input('Masukkan jumlah uang : '))
        if(jumlahUang > totalHarga) :
            kembali = jumlahUang - totalHarga
            print(f"""
                *** Payment Accepted ***

              ============================
              Terima kasih!
              Uang kembali anda : {kembali}
              ============================""")
            for item in keranjang :
                listBarang[item['Nomor Data']]['Stock'] -= item['Qty']
            keranjang.clear()
            break
        elif (jumlahUang == totalHarga) :
            print('''
                *** Payment Accepted ***

                    ================
                    Thank You!
                    Have a good day!
                    ================''')
            for item in keranjang :
                listBarang[item['Nomor Data']]['Stock'] -= item['Qty']
            keranjang.clear()
            break
        else:
            kekurangan = totalHarga - jumlahUang
            print(f"""
                   ### Payment Denied ###

            ===================================
            Uang anda kurang sebesar : {kekurangan}
            ===================================""")

listBarang = [
    {
        'Kode Barang': '1001',
        'Barang': 'Sepatu',
        'Stock': 100,
        'Harga': 250000,
        'Warna': 'Merah'
    },
    {
        'Kode Barang': '1002',
        'Barang': 'Baju',
        'Stock': 200,
        'Harga': 150000,
        'Warna': 'Hitam'
    },
    {
        'Kode Barang': '1003',
        'Barang': 'Jaket',
        'Stock': 300,
        'Harga': 300000,
        'Warna': 'Cokelat'
    },
    {
        'Kode Barang': '1004',
        'Barang': 'Topi',
        'Stock': 250,
        'Harga': 100000,
        'Warna': 'Putih'
    },
    {
        'Kode Barang': '1005',
        'Barang': 'Tas',
        'Stock': 150,
        'Harga': 350000,
        'Warna': 'Biru'
    }
]

keranjang = []

def menuUtama():
    while True :
        pilihanMenu = input('''
                 ***** Selamat datang di Toko Interstellar! *****

Ada yang bisa kami bantu?

1. Melihat Data Penjualan Barang
2. Menambah Data Penjualan Barang
3. Update Data Penjualan Barang
4. Hapus Data Penjualan Barang
5. Pembelian Barang
6. Exit Program

Masukkan angka Menu yang ingin dijalankan : ''')

        if(pilihanMenu == '1') :
            menuRead()
        elif(pilihanMenu == '2') :
            menuCreate()
        elif(pilihanMenu == '3') :
            menuUpdate()
        elif(pilihanMenu == '4') :
            menuDelete()
        elif(pilihanMenu == '5') :
            menuTransaksi()
        elif(pilihanMenu == '6') :
            break
        else:
            errorEntry()

menuUtama()