name="vasavi"
print(name)
str="python world"
print(str[1])
print(str[-1])
print(str[1:6])
print(str[ :6])
print(str[0:12:3])
print(str[ : :2])
s1="hello"
s2="python"
print(s1+" "+s2)#concatenation
#print((s1+" ")*10)
print(("vasavi"+" ")*10)#repetation
s1=" welcome to python "
print(s1.strip())# removing the  spaces from the begining and ending of the string
print(s1.lstrip())
print(len(s1))
print(len(s1.strip()))
print(len(s1.lstrip()))#removing the spaces from left side of the string
print(len(s1.rstrip()))#removing the spaces from right side of the string
print(s1.split())
print(s1.split("o"))# split the string according to given value and it return a values in list format
print(s1.count("e")) #it return how many no of time the given value is occur in the string
print(s1.find("o")) #it return index of the given value from left to right by default
print(s1.rfind("o"))#it return index of the given value from right to left
print(s1.index("m"))
print(s1.find("m"))
# print(s1.index("b")) 
print(s1.find("b"))
s2="hello python"
for ch in s2:
    if ch=="p":
        print(ch)
        print(s2.index(ch))
      