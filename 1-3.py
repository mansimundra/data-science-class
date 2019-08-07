#1
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i)
#2
a=int(input("enter number"))
fact=1
for i in range(1, a+1):
    fact=fact*i
print(fact)
#3
dict1={}
a=int(input("enter range="))
for i in range(1, a+1):
    dict1[i]=(i*i)
print(dict1)

