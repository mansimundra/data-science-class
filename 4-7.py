#4
# l=input("enter list=")
# list=l.split(",")
# print(list)
# a=tuple(list)
# print(a)

#6
# import math
# # d=int(input("enter d="))
#
# def problem_6(d):
#     """Write a program that calculates and prints the value according t	o the given formula:
#     Q = Square root of [(2 * C * D)/H]
#     Following are the fixed values of C and H:
#     C is 50. H is 30.
#     """
#
#     c=50
#     h=30
#     Q=(2*c*d)/h
#     a=math.sqrt(Q)
#     a =round(a)
#     print(a)
#     return a
#
# user_input = input("Provide D values : ")
# print("user_input 1: ",user_input)
# user_input = user_input.split(",")
# print("user_input 2: ",user_input)
#
# for d in user_input:
#     print("d : ",d)
#     problem_6(int(d))

#7

# a=input("enter row and column values=")
# a=a.split(",")
# # y=int(input("enter y"))
# matrix=[]
# b=a[0]
# c=a[1]
# for i in range(0,int(b)):
#     element=[]
#     for j in range(0,int(c)):
#         print(i*j)
#         element.append(i*j)
#     print("element : ",element)
#     matrix.append(element)
# from pprint import pprint
# pprint(matrix)

#3-D matrix

a=input("enter x,y,z for 3-D matrix=")
a=a.split(",")
# y=int(input("enter y"))
matrix=[]
b=a[0]
c=a[1]
d=a[2]
for i in range(0,int(b)):
    element=[]
    for j in range(0,int(c)):
        dimension=[]
        for k in range(0,int(d)):
            print(i*j*k)
            dimension.append(i*j*k)
        print("di : ",dimension)
        element.append(dimension)
    matrix.append(element)
from pprint import pprint
pprint(matrix)