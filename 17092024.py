#write a program to print sqrt of each and every element in a list
l=["1","4","3","7","5","2",'9',"8"]
l1=[]
for ele in l:
    l1.append(int(ele))
print(l1)
def sqrt(l):
    l2=[]
    for i in l:
        l2.append(i*i)
    return l2
print(sqrt(l1))  
#write a program to print reverse a string
word="learning python is very easy" 
print(word[::-1])  
#write a program to print reverse of string by words
l2=word.split()[::-1]
s1=" ".join(l2)
print(s1)
#write a python program to find the minimum and maximum lements in a tuple of integers
t1=eval(input("enter the tuple "))
def max_tuple(t):
    return max(t)
def min_tuple(t):
    return min(t)
print("max",max_tuple(t1))
print("min",min_tuple(t1))
#given a tuple containing nested tuples.write a python program to flatten it into a single tuple
t1=eval(input("enter the tuple"))
l=[]
for i in t1:
    if isinstance(i,tuple):
        l.extend(i)
    else:
        l.append(i)
print(tuple(l))
#write a python program to sort a tuple of tuples based on the second element of each tuple
def second(t):
    t1=sorted(t,key=lambda x:x[1])
    return t1
tuple1=eval(input("enter the tuple "))
print(tuple(second(tuple1)))
"""Create a dictionary where the keys are tuples representing coordinates (x, y)
  and the values are city names. Write a Python program to print the city name for a given coordinate. 
 Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} 
Input: (40.7128, -74.0060) # Expected Output: New York"""
d=eval(input("enter the dict "))
key=eval(input("enter the key "))
print(d[key])




