a = "Hello World"
print(a[1]) #print index ke-1 dari sequence char a
print(a[9:10]) #print 
print(len(a)) #print length dari sequence of char a

text1 = "Hello"
text2 = "World"
number  = 123
c = text1 + text2
d = text1 + " " + str(number)
print(c)
print(d)
print(text1,text2)

age = 36
txt = "My Name is John, and I am {} , {}".format(age, text1)
print(txt)