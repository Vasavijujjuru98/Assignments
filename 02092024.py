#To create a empty tuple
t=()
print(type(t))
print(t)
#To add an item to the tuple
t1=list(t)
print(t1)
n=int(input("enter the list size"))
for i in range(n):
    ele=(input())
    t1.append(ele)
print(t1)
print(tuple(t1))
# write a python program to convert tuple into string
#tup1=(29,35,"a","ram")
s=""
for ele in t1:
    s+=str(ele)
print(s)
#write a python program to find most frequent element in a tuple
t3=(20,20,10,30,5,20,56,30,"a")
c1=0
res=t3[0]
for ele in t3:
    current_freq=t3.count(ele)
    if(current_freq>c1):
        c1=current_freq
        res=ele
print(str(res))

#write a python program to unpack a tuple into several variables"""
names=("ram","krishna","latha")
print(names)
(siva,venkat,srinu)=names
print(siva)
print(venkat)
print(srinu)
bike=("honda","bullet","pulasar")
(black,blue,red)=bike
print(black)
print(blue)
print(red)
t4=(20,30,40)
(n1,n2,n4)=t4
print(n1)
print(n2)
print(n4)
print(n1+n2+n4)
