def fungsi():
    print("Hello, World!")

def print_name(name):
    print("Hello, world "+ name)

def default_parameter(name="Wicak Doang"):
    print("Hello, world "+ name)

def fungsi_with_return(x):
    return 5 * x

fungsi()
print_name("Wicak")
default_parameter()

y = fungsi_with_return(4)
print(y)