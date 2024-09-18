#write a python program to guess a random number
import random
n=random.randint(1,100)
choice=0
while choice<10:
    guess=eval(input("enter your guess  "))
    if(guess>n):
       print("your guess is greather than random")
    elif(guess<n):
       print('your guess is less than random')
    else:
       print("congratulation your guess is correct")
       break
#write a python program to calculate dmart billing system 
product={"santhor":45,"oil":120,"milk":20,"sugar":40,"dal":50}
l=[]
t=[]
print("welcome to dmart")
num=int(input("enter no of items"))
for i in range(num):
    item_s=input("enter the item ")
    l.append(item_s)
for i in range(len(l)):
    if(l[i]=="santhor"):
        x=product.get("santhor")
        t.append(x)
    elif(l[i]=="oil"):
        x=product.get("oil")
        t.append(x)
    elif(l[i]=="milk"):
        x=product.get("milk")
        t.append(x)
    elif(l[i]=="sugar"):
        x=product.get("sugar")
        t.append(x)
    elif(l[i]=="dal"):
        x=product.get("dal")
        t.append(x)
    else:
        print("item is not available")
        break
sum=0
for i in range(len(t)):
    sum=sum+t[i]
print(sum)


   


    

    

   