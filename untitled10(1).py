# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Ns5Uvpmd--phRf-mdFvH6Jwjs4pEOKd
"""

number=input("enter number")
c=' '.split()
c+=number
list1=list(map(int,c))
print(sum(list1))

list1=[1,2,3,4,5,6,7,8,9]
maxmam_number=max(list1)
print(maxmam_number)

list1=[1,2,3,4,2,5,6,72,2,2,3]
target=2
list2=[]
for i in list1:
  if i == target:
    list2.append(i)
print(len(list2))

num1=float(input("enter frist number: "))
num2=float(input("enter sacand number:"))
output=0
for i in range(1,12+1):
  if num1 and num2 % i==0:
    output+=i
print (i)

def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def milt(x,y):
  return x*y
def div(x,y):
  return x/y

while True:
  print("1.add")
  print("2.sub")
  print("3.milt")
  print("4.div")
  print("5.exit")
  choice=int(input("choice oprashen"))

  while int(choice<1 or choice>5):
    print("pless enter from oprashan")
    choice=int(input("choice oprashen"))

  if choice==5:
    print("goodbyyyyy")
    break
  x=float(input("enter frist number: "))
  y=float(input("enter sacand number:"))
  if choice==1:
    print( add(x,y))
  elif choice==2:
    print(sub(x,y))
  elif choice==3:
    print( milt(x,y))
  elif choice==4:
    while y==0:
      y=float(input("enter sacand number:"))
    else:
      print(div(x,y))
  else:
    print("you are donkeeeeeeee")

list1=[0,1]
num=int(input("  "))
for i in range(2,num):
  x=list1[-1]+list1[-2]
  list1.append(x)
print(list1[:num])

list1=[1,2,4,5,3,7,6,9]
n=max(list1)
number=0
for i in range(1,n+1):
  list1.append(i)

for num in list1:
  number^=num

print(number)

