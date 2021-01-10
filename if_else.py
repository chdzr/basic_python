a = 220
b = 33

# and -> untuk menggabungkan kondisi
# or -> untuk opsional kondisi
# not -> untuk define negasi dari sebuah nilai

if (not b > a) and (a == 220):
    print("b is greater than a")
elif a == b or b == 33:
    print("b is equal a")
else:
    print("a is greater than b")