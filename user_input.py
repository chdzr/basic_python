#input digunakan untuk memasukan nilai kedalam variable. nilai dari variable yang di define dengan fungsi input() akan menghasilkan value dengan dataType string. bisa di casting pada saat input atau casting saat penggunaan variable
#print() dengan value nya numeric menggunakan comma. kalo sama2 string bisa menggunakan +
name = input()
age = int(input())
print("Your name is : " +  name)
print("Your Age is : ",  age)
print(type(name))
print(type(age))