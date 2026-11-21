import admin
import user


def Mulai():
    print('Winchester Barbershop'.center(50))
    print(50*"=")
    print("SELAMAT DATANG DI WINCHESTER BARBERSHOP".center(50))
    print("BUKA = 07.30 - 17.00".center(50))
    print("BUKA SETIAP HARI".center(50))
    print(50*"=")

    while True:
        role = int(input('status anda?\n 1.Admin\n 2.User\n 3.Berhenti\n '))
        if role == 1:
            admin.admin_login()
        elif role == 2:
            user.user()
        elif role == 3:
            break
        else:
            print('pilihan tidak valid')
Mulai()
