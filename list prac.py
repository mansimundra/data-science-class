a=[1,2,3]
print(a,a[0])
b=[["hello"],"$","world"]
print(b[0][0])
a=[1,2,3,4,5,6,7]
#print(a[1:5])
a.append(8)
print(a)
a.insert(3,11)
print(a)
a.insert(a.index(4),21)
print(a)
b=[22,33,44,55,11]
print(22 in b)
#a.append(b)
a.extend(a)
print(a)
a.pop(a.index(21))
print(a)
a.remove(1)
print(a)
print(a.count(5))
del a

print([1]*10)