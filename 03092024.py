#write a program which will find all such numbers which are divisible by 7 but are not multiple of 5,between 2000 and 3200 the numbers obtained should be printed in a comma separated sequance  on a single line
for i in range(2000,3201):
    if((i%7)==0):
        if((i%5)!=0):
            print(i,end=",")
#write agiven integral number n,write a program to generate a dictionart that contain 1 and n and then the program should print the dictionary 
n=int(input(" enter the number"))
dict={}
for i in range(1,n+1):
   dict[i]=i*i
print(dict)
#write a program which accepts a seq of comma-saparated number of console and generate a list and tuple which contains every number 
value=(input("enter the element.."))
t1=value.split(",")
t2=tuple(t1)
print(t1)
print(t2)
#write a program that accepts a comma saparated sequance of words in a comma separated sequance after sorting them alphabatically
word=input('enter the word')
word_list=word.split(",")
t=word_list.sort()
print((",").join(word_list))
#write a program that accepts a sentence and calculate the number of letters and digits 
p=input("enter the word")
count_letter=0
count_digit=0
for ele in p:
    if ele.isalpha():
        count_letter=count_letter+1
    elif ele.isdigit():
        count_digit=count_digit+1
print(count_letter)
print(count_digit)
#write a program that accept a sentence and calculate the number of uppercase letters andlowercase letters
word=input("enter a word  ")
uppercase=0
lowercase=0
for ele in word:
   if ele.isupper():
      uppercase=uppercase+1
   elif ele.islower():
      lowercase=lowercase+1
print(uppercase)
print(lowercase)
#write a program that compute the net amount of a bank account  based on transaction log from console input
a=input()
b=a.split()
balance=0
for i in range(len(b)):
   if b[i]=="D":
      balance+=int(b[i+1])
   elif b[i]=="W":
      balance-=int(b[i+1])
print(balance)
       
   


        


       





