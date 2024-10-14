from abc import ABC, abstractmethod
class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def get_info(self):
        return self.brand,self.year
class car(vehicle):
    def __init__(self,brand,year,no_of_doors):
        vehicle.__init__(self,brand,year)
        self.no_of_doors=no_of_doors
    def get_info(self):
        return self.brand+str(self.year)+str(self.no_of_doors)
class motorcycle(vehicle):
    def __init__(self,brand,year,has_sidecar):
        vehicle.__init__(self,brand,year)
        self.has_sidecar=has_sidecar
    def get_info(self):
        return self.brand+str(self.year)+self.has_sidecar
                
c=car("benz",2020,4)
print(c.get_info())
m=motorcycle("royal&field",2021,"yes") 
print(m.get_info()) 


#---------------------2 problem------------------
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(Animal):
    def make_sound(self):
        return " dog can sound woof"
class cat(Animal):
    def make_sound(self):
        return " cat can sound meow"
class cow(Animal):
    def make_sound(self):
        return " cow can sound moo"
def play_sound(animal):
    if isinstance(animal,Animal):
        return animal.make_sound()
dog=dog()
cat=cat()
cow=cow()
print(play_sound(dog))
print(play_sound(cat))
print(play_sound(cow))

#--------------3.problem--------------------

class BankAccount:
    def __init__(self,damount,wamount,balance):
        self.balance=balance
        self.damount=damount
        self.wamount=wamount

    def deposit(self):
        pass
    def withdraw(self):
        pass
    def __get_balance(self):
        pass
class savingAccount(BankAccount):
    def deposit(self):
        self.balance=self.balance+self.damount
        return self.balance
    def withdraw(self):
        if(self.wamount>0):
            if(self.balance>500):
               self.balance=self.balance-self.wamount
               return self.balance
            else:
               return " connot withdraw the amount is insufficient"
        else:
            return " the amount must be positive"
    def __get_balance(self):
            return self.balance
class currentAccount(BankAccount):
    def deposit(self):
        self.balance=(self.balance)+(self.damount)
        return self.balance
    def withdraw(self):
        if(self.wamount>0):
            if(self.balance-self.wamount>=-1000):
               self.balance=self.balance-self.wamount
               return self.balance
            else:
               return "cannot withdrawal, the amount is overdraft"
        else:
            return " the amount must be positive"
           
    def __get_balance(self):
            return self.balance
s=savingAccount(500,100,500)
print(s.deposit())
print(s.withdraw())
c=currentAccount(5000,3000,1000)
print(c.withdraw())

#---------------4 problem----------------
class Employee:
    def  __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return self.name+" "+str(self.salary)
    def get_salary(self):
        return self.salary
    def increase_salary(self,percentage):
        self.percentage=percentage
        self.salary+=self.salary*(self.percentage)/100
        

class manager(Employee):
    def __init__(self,name,salary,depart):
        super().__init__(name,salary)
        self.depart=depart
    def get_details(self):
        return (super().get_details()+"  "+self.depart)
   
    
class developer(Employee):
    def __init__(self,name,salary,planguage):
        super().__init__(name,salary)
        self.planguage=planguage
    def get_details(self):
        return (super().get_details()+"  "+self.planguage)

m=manager("bharu",50000,"hrdepart")
print(m.get_details())

d=developer("vasu",23000,"python")
print(d.get_details())
m.increase_salary(3)
d.increase_salary(2)
print("----------after increment--------")
print(m.get_details())
print(d.get_details())
#-------------------5 problem-------------------
from abc import abstractmethod


class Media:
    @abstractmethod
    def play(self):
        pass
class audio(Media):
    def play(self):
        return " play .mp3 file"
class video(Media):
    def play(self):
        return "play .mp4 file"  
class liveStream(Media):
    def play(self):
        return "play a live stream"
def start_media(media):
    if isinstance(media,Media):
        return media.play()
a=audio()
v=video()
l=liveStream()
print(start_media(a))
print(start_media(v))
print(start_media(l))
#-------------6.problem----------"""
from abc import ABC,abstractmethod
class libraryItem:
    def borrow(self):
        pass
    def return_item(self):
        pass
class book(libraryItem):
    def __init__(self,title,author,num_copies):
        self.title=title
        self.author=author
        self.num_copies=num_copies
    def borrow(self):
        self.num_copies-=1
        return self.num_copies
    def return_item(self):
        return self.title,self.author,self.num_copies 
         
class DVD(libraryItem):
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
    def borrow(self):
        return "dvd is borrowed"
    def return_item(self):
        return self.title,self.director,self.duration
def borrow_item(item):
    if(isinstance(item,libraryItem)):
        return item.borrow()

b=book("apptitude","rs agrawal",10)
print(b.return_item())
print(borrow_item(b))
d=DVD("rrr","rs rajamouli","2hours")
print(borrow_item(d))
print(d.return_item())
        





