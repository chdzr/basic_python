list_contact = []
welcome_text = "Selamat Datang!"
menu_not_found = "Menu Tidak ditemukan"

show_menu = True
itteration_menu = 0

while show_menu:
    if itteration_menu == 0 :
        print(welcome_text)
    print("Silahkan Masukkan Menu")
    print("1. Daftar Kontak")
    print("2. Input Kontak")
    print("3. Keluar")
    print("pilih Menu :")
    
    option = int(input())

    itteration_menu += 1

    if option == 3:
        print("Program Telah Selesai, terimakasih")
        show_menu = False
    elif option == 2:
        contact = []
        name= input("Masukkan Nama :")
        phone= input("Masukkan No Telp :")
        contact.append(name)
        contact.append(phone)
        list_contact.append(contact)
    elif option == 1:
        print("List of Contact :")
        for i in range(len(list_contact)):
            contact = list_contact[i]
            print("Nama : {}".format(contact[0]))
            print("No Telp : {}".format(contact[1]))
    else:
        print("input tidak diketahui")
