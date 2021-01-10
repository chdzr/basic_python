# casting adalah merubah tipe data satu ke tipe data lain
# casting dari float ke int akan selalu menjadi round down 
# pembulatan ke atas menggunakan ceil() implementasi library math. notes : untuk menggunakan ceil harus diubah menjadi numeric dahulu
# pembulatan mendekati bilangan bulat menggunakan round() implementasi library math. notes : untuk menggunakan ceil harus diubah menjadi numeric dahulu
# pembulatan ke bawan menggunakan floor() implementasi library math. notes : untuk menggunakan ceil harus diubah menjadi numeric dahulu
from math import floor, ceil
x = int(2.8)
y = float("3.0")
z = str(2.7)
castCeil = ceil(3.2)
castFloor = floor(3.8)
castRound = round(3.5)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(castCeil)
print(type(castCeil))
print(castFloor)
print(type(castFloor))
print(castRound)
print(type(castRound))