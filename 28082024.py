# count of occurance of a given character in a string
str="hello world"
str1=str.count("l")
print(str1)
# to check the given string is palindram or not
s=input(" enter  the string:")
s1=s[::-1]
if s==s1:
    print(" the given string is palindram")
else:
    print(" the given string is not palindram")
#replace the space with given string using replace
p="hello world"
s1=p.replace(" ","@")
print(s1)
#To print lowercase to uppercase letters of  a given string
str=input("enter the given string")
s2=str.upper()
print(s2)
#convert the lowercase vowel to uppercase
s="hello world"
str2=""
n=len(s)
for i in range(n):
    if(p[i]=="a"or p[i]=="e" or p[i]=="i" or p[i]=="o" or p[i]=="u"):
        c=(s[i].upper())
        str2=str2+c
    else:
        str2+=p[i]
print(str2)
#the given character is vowels or consonents
c='b'
if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
    print("vowels")
else:
    print("consonents")
m="123456"
print(m.isdigit())
n="abc123"
print(n.isdigit()) 
# remove the vowels from the given string
str1="hello world"
vowels=['a','e','i','o','u']
n=len(str1)
result=""
for i in range(n):
    if str1[i] not in vowels:
        result=result+str1[i]
print(result)
#to print the count of occurance of vowels and consonents
string1="hello world"
vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
vowels_count=0
consonents_count=0
for ch in string1:
    if ch in vowels:
        vowels_count+=1
    else:
        consonents_count+=1
print(vowels_count)
print(consonents_count)
#write a program to print highest frequency of character in a given string 
string1="ababcccccdancc"
print(string1)
all_freq={}
for i in string1:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
result=max(all_freq,key=all_freq.get)
print("heighest frequency character "+result)
#write a program to replace first character of vowels to - 
string="hello world"
vowels="aeiouAEIOU"
for i in range(len(string)):
    if string[i] in vowels:
        string=string[:i]+"-"+string[i+1:]
        break
print(string)
# write a program to print how many occurance of alphabets,digits,and symbols
string="hello world123@_#"
alphabet_count=0
digit_count=0
symbols_count=0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabet_count+=1
    elif(string[i].isdigit()):
        digit_count+=1
    else:
        symbols_count+=1
print(alphabet_count)
print(digit_count)
print(symbols_count)
#write a python program the given character is digit or not without using isdigit()
ch=input(" enter the given character")
if(ch>='0' or ch<='9'):
    print(" The given character is digit")
else:
    print("the  given character is not digit") 
# to print sum of the integers of given string
x="abc1234hello"
sum1=0
for i in x:
    if ord(i)>=48 and ord(i)<=57:
        sum1=sum1+int(i)
print(str(sum1))
#to print given character is vowels or consonents
c1=input(" enter the character")
vowels="aeiou"
if c1 in vowels:
    print(" the given  character is vowel")
else:
    print("the given character is consonents")
# To print copy of one string into another string
s1="hello world"
s2=str(s1)
print(s1)
# To print non repeated character in  a given string
s1="hello world"
for i in s1:
    count=0
    for j in s1:
        if i==j:
            count+=1
        if count>1:
            break
    if(count==1):
        print(i)    
#to print the given character is digit or not
c=input("enter the character")
if c.isdigit():
    print("the given character is digit")
else:
    print("the given character is not  a digit")
#To print the given two strings are anagram or not
str1=input("the first string;")
str2=input("the second string:")
if (sorted(str1)==sorted(str2)):
    print("the given string is anagram")
else:
    print(" the given string is not anagram")
#to saparate characters in given string
str="hello world"
for i in range(0, len(str)):
    print(str[i],end=" ")
# to remove the blank spaces from string
str="hello world"
str2=str.replace(" ","")
print(str2)
#to print cancating of two strings using join method
str="hello"
str1="world"
s="".join([str,str1])
print(s)
# to print concating of two strings without using join method
str="hello"
str1="world"
print(str+str1)
#to remove the repeated characters from the given string
str1="hello world"
p=""
for char in str1:
    if char not in p:
        p=p+char
print(p)

























