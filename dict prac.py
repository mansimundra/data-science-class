a={}
print(type(a))
b={"name":"Mansi"}
print(b["name"])
c={"name":"Mansi", "age":22, "phone":9039932377, 0:"null"}
print(c[0])
c['city']='indore'
c[0]= "zero"
print(c)
print(c.keys())
print(list(c.keys())[1])