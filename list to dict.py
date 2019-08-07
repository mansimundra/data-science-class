l1=["name","age","phone","city"]
l2=["abc", 25, "9876543210","indore"]
l3=[27, "9039932377", "gwalior", "bcd"]
l4=["def",29, "9039932377", "gwalior"]
l5=[30, "9039932323", "gwalior", "ghi"]


#l2.pop(0)
#print(l2)
#l3.insert(0,l3[3])
#l3.pop(4)
#print(l3)

dict1={}

#for i in range(0,4):
    #dict[l1[i]]=[l2[i],l3[i]]
    #print(l1[i],dict[l1[i]])
#print(dict)

dict1 = dict1.fromkeys(l1,[])
print("1",dict1)
fnal_list=[l2,l3,l4,l5]
# print(fnal_list)
print()
names = []
ages=[]
phones=[]
cities=[]

for i in fnal_list:
    print(i)
    # dict1[l1[i]] = [l2[i],l3[i]]

    if type(i[0])==int:
        print("int : ",i[0])
        # print(i[3])
        names.append(i[3])
        ages.append(i[0])
        phones.append(i[1])
        cities.append(i[2])
    #     l3[i]=l3[i-1]
    #     dict1[l1[i]]=[l2[i], l3[i]]
    else:
        print("str : ",i[0])
        # print(i[3])
        names.append(i[0])
        ages.append(i[1])
        phones.append(i[2])
        cities.append(i[3])
    #     dict1[l1[i]]=[l2[i],l3[i]]
    # print(dict1)
    # print(dict1)
    print("**********************************")
dict1["name"]=names
dict1["age"]=ages
dict1["phone"]=phones
dict1["city"]=cities
from pprint import pprint
pprint(dict1)

