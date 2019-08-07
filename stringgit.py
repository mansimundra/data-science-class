str1="\n hi my name is Mansi Mundra and I am from Indore \n"
print(str1)
str1=str1.strip()
print(str1)
str1=str1.replace("I am from Indore", "contact me on +919039932377 or mansimundra.38@gmail.com")
print(str1)
list1=str1.split("and")
print(list1)
name=list1[0].split('is')[-1].split()[0]
print(name)
surname=list1[0].split('is')[1].split()[-1]
print(surname)
phone=list1[1].split('or')[0].split()[-1]
print(phone)
email=list1[1].split('or')[1].strip()
print(email)
print("Name: {}\nSurname: {}\nPhone: {}\nEmail: {}".format(name,surname,phone,email))