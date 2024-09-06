# write a program to add a key to a dictionary
dict={}
dict["name"]="vasavi"
dict["age"]=24
dict["id"]=101
print(dict)
dict.update({"height":"5feet"})
print(dict)
#write a program the given value is present in the dictionary or not
value=dict.values()
n=eval(input("enter a value"))
if n in value:
    print("the value present in the dictionary")
else:
    print("the value is not present in the dictionary")
#write a python program to print a dict where the keys are numbers between 1 and 15
n=int(input("enter the dictionary size"))
dict={}
for i in range(1,n+1):
    dict[i]=i*i
print(dict)
#write a program to create a dictionary from string
str=input("enter the string   ")
dict={}
for letter in str:
    if letter in dict:
        dict[letter]+=1
    else:
        dict[letter]=1
print(dict)
#write a python program to combine two dictionaries by adding values of common keys
d1=eval(input("enter dictionary1  "))
d2=eval(input("enter dictionary2  "))
for key in d2:
    if key in d1:
        d2[key]=d2[key]+d1[key]
print(d2)
#write a python program to merge two dictionaries
d1={'name':'vasavi',"age":25}
d2={'id':101,"salary":30000}
d3=d1|d2
print(d3)
#write a python program to sort  dictionary by keys
dict1=eval(input("enter the dictionary  "))
l=sorted(dict1.keys())
s=list()
for ele in l:
    s.append(dict1[ele])
d1=dict(zip(l,s))
print(d1)


   
