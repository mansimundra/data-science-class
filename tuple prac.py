
#in tuple we cannot update or delete any item or tuple because tuple is immutable data type in which cannot be changed once created.
a=[]
b=()
print(type(a), type(b))
c=(1)
print(type(c))
c=2.0034
print(type(c))
b=(1, "a")
print(type(b))
c=(1,2,"a",4)
print(c[2], c[1:5])
del c
#del c[2]
#print(c)
#in tuple del works only to del whole tuple . Doesn't works when we need to del only one item in the tuple
