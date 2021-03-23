print('Selamat datang!')

def menu():
    print('--- Menu ---')
    print('1. Daftar kontak')
    print('2. Tambah kontak')
    print('3. Keluar')

menu()
pilih = int(input('Pilih menu: '))

kontak = {'Farhan': '08123456789', 'Joko': '08987654321'}

def tambah_nama():
    nama_kontak = str(input('Masukkan nama kontak: '))
    telepon_kontak = int(input('Masukkan telepon kontak: ')) 
    kontak.update({nama_kontak:telepon_kontak})
    print('Kontak berhasil ditambahkan!')

while pilih != 3:
    if pilih == 1:
        for key, value in kontak.items():
            print('Nama: ', key,'\nTelepon :' , value)

    elif pilih == 2:
        tambah_nama()
             
    else:
        print('Menu tidak tersedia')

    print()
    menu()
    pilih = int(input('Pilih menu: '))

print('Program selesai, sampai jumpa!')
