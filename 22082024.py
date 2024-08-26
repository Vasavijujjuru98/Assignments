#arthamatic operations
a=int(input("enter a value "))
b=int(input("enter b value ")) 
print(a+b)
print(b-a)
print(a*b)
print(b/a)
print(b//a)
print(b%a)
print(a**2)
x=(input("enter a value ")) # by default input  function take string literals
print(type(x))
#if you want take integer value by using int() function similarly  if we want float value we can use float() function
y=int(input(" enter y value"))
print(y)
print(type(y))
"""type casting means converting one type to another type
   if you want to integer to anytype. we cant convert string character to anytyp but we convert numerical string 
    value to anytype"""  
num=float(y)#converting integer to floating value
print(num)
print(type(num)) 
z=str(num)#converting float to string
print(z)
print(type(z))

m=input(" enter your value")
print(m)
n=int(m)
print( type(n))# conerting numerical string literal to ineger type  
#logical operation means if the logic is true it return true otherwise it returns false
n1=int(input(" enter n1 value"))
n2=int(input("enter n2 value"))
p=(n1<10) or (n2>20)
print(p) 
n3=(n2!=25) 
print(n3)
#relational operator: it is a comparative operator. it check the relation between the two operand. if condition is true it return true otherwise it return false
if(n1<=10):
    print("n1 equal to 10")
else:
    print("n1 is greater than 10")
print("a " >"b")

#identity operators
l1=[1,2.34,"vasavi",67]
l2=72
x=l2 not in l1
print(x)

p1=10
p2=20
q=p1 | p2 #bitwise operator
print(q)
print(type(q))

    

