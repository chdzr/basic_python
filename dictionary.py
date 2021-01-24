# Dictionary di python seperti hal nya dengan object pada javascript menggunakan key value untuk pendefinisan nya

model ={
    "region": "EU",
    "regionName": "Europe"
}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "type": ["Automatic", "Manual"], #list
    "year": 1964,
    "model": model
}
print(thisdict["model"]["region"])
print(thisdict["type"])
thisdict["year"] = 2016
x = thisdict["year"]
print(x)

print("--------------------------------------------")

list = []


for i in range(3):
    contact = {
        "name":"",
        "no_telp": ""
    }
    contact["name"] = "Test {}".format(i)
    contact["no_telp"] = "Telp {}".format(i)
    list.append(contact)

print(list)

