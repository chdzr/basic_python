# list sama seperti array. bisa menampung deret dari sebuah nilai. dan deret tersebut bisa di isi dengan berbagai macam nilai dengan beragam tipedata

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(type(mylist))
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

# mencetak semua nilai dri list bisa menggunakan for

for x in mylist:
    # x adalah variable pencacah : variable yang akan nilai sesuai dengan perulangan
    print(x)