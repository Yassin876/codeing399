# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16RkXtDEXUcYoEyKNsXe6Qpxi1VaU004r
"""

#this is task the user input three numbers and print maxmam number between
num1=float(input("enter frist number\n"))
num2=float(input("enter secand number\n"))
num3=float(input("enter therd number\n"))
if num1>=num2 and num1>=num3:
  print(num1)
elif num1<=num3 and num2 <= num3:
  print(num3)
else:
  print(num2)

#this is task user input word and program read by backwards
def Palindrome(word):

  no_spas=word.strip()
  backwards=no_spas[::-1]
  if no_spas == backwards:
    print(f"this is word {word} read by backwards")
  else:
    print(f"this is word {word} can not read by backwards")
word=str(input("enter your word\n"))
Palindrome(word)

for i in range(1,100+1):
  if i%3==0 and i%5==0:
    print("fizz buzz")
  elif i%3==0:
    print("fizz")
  elif i%5==0:
    print("buzz")
  else:
    print(i)

n=int(input("enter number\n"))
def factorial (n):
  if n==0 or n==1:
    return (1)
  else:
    return n*factorial (n-1)
while n<0:
  print("pless enter number morthan zero")
  n=int(input("enter number\n"))
else:
  print(f"factorial {n} is {factorial (n)}")

word=input("enter your word\n")
titel="aeiouAEUIO"
r=''
for i in word:
  if i in titel:
    r+=i
total=len(r)
print(total)

