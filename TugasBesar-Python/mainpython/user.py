import pprint

def order(user):
    print('silahkan order')
    print('JAM OPERASI\n 07.30|09.00|10.00|11.00|13.00|14.00|15.00|16.00')
    print('HARGA = 25.000')
    nama = user 
    model_rambut = input('masukkan model potongan yang ada inginkan: ').upper()
    tanggal_bulan = input('masukkan tanggal dan bulan: ').upper() #2026
    jam = input('masukkan jam yang ingin kamu pilih: ')
    jumlah_booking = 0
    while True:
        data_jam =['07.30','09.00','10.00','11.00','13.00','14.00','15.00','16.00']
        if jam not in data_jam:
            print('jam tidak tersedia')
            return
        try:
            with open('database/bookingsalon.txt','r') as file:
                for line in file:
                    data = line.strip().split('|')
                    if len(data) == 4 and data[2] == tanggal_bulan and data[3] == jam:
                        jumlah_booking = jumlah_booking + 1 
                            
        except FileNotFoundError:
            pass

        if jumlah_booking >= 3:
                print('antrian penuh')
        else:
            with open('database/bookingsalon.txt','a') as file:
                file.write(f'{nama}|{model_rambut}|{tanggal_bulan}|{jam}\n')
                print('Orderan berhasil masuk')
                return

def menu_user(user):
    print(f'selamat datang di menu {user}'.upper())
    while True:
        pilihan = int(input('1.Lihat Model Potongan\n2.Order\n3.Keluar '))
        if pilihan == 1:
            with open('database/modelpotongan.txt','r') as file:
                data = file.read().splitlines()
                pprint.pprint(data[:15], width=50, compact=True)
                print('Bisa Request Selain di Menu')
        elif pilihan == 2:
            order(user)
        elif pilihan == 3:
            break
            
        

def register():
    print('silahkan daftar')
    username_baru = input('masukkan username anda: ')
    password_baru = input('masukkan password baru: ')
   

    if not username_baru or not password_baru:
        print("Username dan password tidak boleh kosong!")
        return

    try:
        '''mengecek username ada yang sama atau tidak'''
        with open('database/userlogin.txt','r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 2 and data[0] == username_baru:
                    print("Username sudah terdaftar! Gunakan username lain.")
                    return
    except FileNotFoundError:
        pass
                
    with open('database/userlogin.txt', 'a') as file:
        file.write(f"{username_baru}|{password_baru}\n")

def login():
    
    print('MENU LOGIN')
    username = input('masukkan username: ')
    password = input('masukkan password: ')
    try:
        with open('database/userlogin.txt','r') as file:
            for line in file:
                data = line.strip().split('|')
                if len(data) == 2:
                    db_user,db_pass = data[0], data[1]
                    if db_user == username and db_pass == password:
                        print(f"\nLogin berhasil! Selamat datang, {username}.")
                        menu_user(username)
                        return
                    
        print('password salah')
    except:
        print('anda belum buat akun')



def user():
    status= int(input('\n 1.Login\n 2.Registrasi'))
    if status == 1:
        login()
    elif status == 2:
        register()






