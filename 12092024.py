#given a tuple containing nested tuples write a python program to flatten it into a single tuple
tuple1=eval(input("enter the tuple"))
l=[]
for i in tuple1:
    if isinstance(i,tuple):
        l.extend(i)
    else:
        l.append(i)
print(tuple(l))
#write a python program to sort a tuple of tuples based on the second element
def last(n):
    return n[-1]
def sort(tuples):
    return sorted(tuples,key=last)
a=eval(input("enter the tuple"))
t=sort(a)
print(tuple(t))


