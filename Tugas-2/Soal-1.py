import os

#clear terminal console
def clear_console():
    os.system('cls')

def show_welcome_board():
    print("Selamat datang!")

def show_main_menu():
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()
    print("pilih Menu :")

def show_exit_message():
    print("Program selesai, sampai jumpa!")

def show_unexpected_input():
    print("Menu Tidak Tersedia")
    prompt_back_to_menu()

def show_contact_added_message():
    print("Kontak berhasil ditambahkan")

def entry_contact_list(list_contact):
    contact = {"name":"","phone":""}
    contact["name"]= input("Masukkan Nama :")
    contact["phone"]= input("Masukkan No Telp :")
    list_contact.append(contact)
    show_contact_added_message()
    print()
    prompt_back_to_menu()

def show_contact_list(list_contact):
    print("Daftar kontak :")
    for i in range(len(list_contact)):
        contact = list_contact[i]
        print("Nama: {}".format(contact["name"]))
        print("No Telepon: {}".format(contact["phone"]))
        print()
    prompt_back_to_menu()

def prompt_back_to_menu():
    input("Tekan Enter untuk kembali ke menu")
    clear_console()

def main():
    list_contact = []
    show_menu = True
    itteration_menu = 0
    while show_menu:
        if itteration_menu == 0 :
            show_welcome_board()
        show_main_menu()
        #try-except for prevent breaking code while input alphabetical character
        try:
            option = int(input())
        except:
            option = 4
        
        clear_console()
        
        if option == 3:
            show_exit_message()
            show_menu = False
        elif option == 2:
            entry_contact_list(list_contact)
        elif option == 1:
            show_contact_list(list_contact)
        else:
            show_unexpected_input()
            


if __name__ == "__main__":
    main()