# continue digunakan untuk melanjutkan suatu perulangan dan tidak execute perinta setelah continue
for i in range(5):
    if i == 3:
        continue
    print(i)

print("------------------------------------")

# break digunakan untuk menghentikan proses perulangan
for i in range(5):
    if i == 3:
        break
    print(i)