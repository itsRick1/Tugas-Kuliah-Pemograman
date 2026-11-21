

def hapus_antrean():
    with open('TugasBesar-python/database/bookingsalon.txt','r') as file:
        data = file.readlines()
    if len(data) == 0:
        print('Belum ada orderan')
        return
    try:
        indeks = int(input('masukkan order yang akan di hapus: ')) - 1
        bayaran = 25000
        if 0 <= indeks < len(data):
            data.pop(indeks)
            with open('TugasBesar-python/database/bookingsalon.txt','w') as file:
                file.writelines(data)
            print('antrian di hapus')
            with open('TugasBesar-python/database/kas.txt','r') as file:
                kas = int(file.read().strip())
            hasil = kas + bayaran
            with open ('TugasBesar-python/database/kas.txt','w') as file:
                file.write(str(hasil))
    
        else:
            print('antrian tidak ditemukan')
    except ValueError:
        print('Input harus berupa angka')

    
def lihat_antrean():
    with open('TugasBesar-python/database/bookingsalon.txt','r') as file:
        for line in file :
            data = line.strip().split('|')
            if len(data) == 4:
                print(data)
def lihat_kas():
    with open('TugasBesar-python/database/kas.txt','r') as file:
        data=file.read()
    print(data)

def edit_menu():
    potongan_baru = input('masukkan potongan baru: ').upper()
    with open('TugasBesar-python/database/modelpotongan.txt','a') as file:
        file.write(potongan_baru + '\n')

def admin_login():
    print(50*"=")
    print('selamat datang admin'.center(50))
    print('1.Edit Model Potongan\n2.Lihat Kas\n3.Lihat Antrean\n4.Hapus Antrean\n5.Keluar')
    print(50*"=")
    while True:
        pilihan = int(input('masukkan pilihan anda: '))
        if pilihan == 1:
            edit_menu()
        elif pilihan == 2:
            lihat_kas()
        elif pilihan == 3:
            lihat_antrean()
        elif pilihan == 4:
            hapus_antrean()
        elif pilihan == 5:
            break
        else:
            print('masukkan pilihan yang benar')
        

