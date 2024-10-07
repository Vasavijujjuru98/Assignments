print("---------first program----------")
#single inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print(self.name,"bark")
d=Dog("puppy")
d.speak()
print("---------second program----------")
#multiple inheritance
class Teacher:
    def __init__(self,subject):
        self.subject=subject
class Reasearcher:
    def __init__(self,field):
        self.field=field
class TeachingReasercher(Teacher,Reasearcher):
    def __init__(self,subject,field):
        Teacher.__init__(self,subject)
        Reasearcher.__init__(self,field)
    def display(self):
        print(self.subject,self.field)
T=TeachingReasercher("maths","algebra")
T.display()

print("---------second program-2----------")
#problem -2
class bird:
   def __init__(self,species):
       bird.species=species
class flyable:
   def fly(self):
      return "flying"
class Eagle(bird,flyable):
   def __init__(self,species):
      bird.__init__(self,species)
   def display(self):
      print(self.species,"is",self.fly())
e=Eagle("wild turkey")
e.display()
print("---------third program----------")
# Multilevel Inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def d(self):
        print(self.name)
        print(self.age)

class Employee(person):
    def __init__(self,name,age,salary):
        person.__init__(self,name,age)
        self.salary=salary
class manager(Employee):
    def __init__(self,name,age,salary,depart):
        Employee.__init__(self,name,age,salary)
        self.depart=depart
    def display(self):
        print(self.name,self.age,self.salary,self.depart)
m=manager("vasu",25,23000,"python")
m.display()
m.d()
print("---------fourth program-----------")
# Hierarchical Inheritance
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def d(self):
        print(self.salary)
        
class Developer(Employee):
    def __init__(self,name,salary,planguage):
        Employee.__init__(self,name,salary)
        self.planguage=planguage
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        Employee.__init__(self,name,salary) 
        self.team_size=team_size
        print(self.name,self.salary,self.team_size)
class intern(Developer):
    def __init__(self,name,salary,planguage,duration):
        Developer.__init__(self,name,salary,planguage)
        self.duration=duration
    def display(self):
        print(self.name,self.salary,self.planguage,self.duration)
i=intern("vasu","23000","python","6months")  
i.display() 
m=Manager("bharu","40000",10)
m1=Manager("lucky",25000,5)
print("---------fourth program -2-----------")
#problem --2
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class car(vehicle):
    def __init__(self,brand,model,no_doors):
        vehicle.__init__(self,brand,model)
        self.no_doors=no_doors
    def d1(self):
        print(self.brand,self.model,self.no_doors)
class Bike(vehicle):
    def __init__(self,brand,model,price):
        vehicle.__init__(self,brand,model)
        self.price=price
    def d2(self):
        print(self.brand,self.model,self.price)
c=car("benz","GlE",5)
c.d1()
b=Bike("pulsur","N125",90000)
b.d2()
print("---------fifth program----------")
#hybrid  inheritance
class Device:
    def __init__(self,name):
        self.name=name
class phone(Device):
    def __init__(self,name,pno):
        Device.__init__(self,name)
        self.pno=pno
class Tablet(Device):
    def __init__(self,name,screen_size):
        Device.__init__(self,name)
        self.screen_size=screen_size
    def d1(self):
        print(self.name,self.screen_size)

class smartphone(phone,Tablet):
    def __init__(self,name,pno,screen_size,os):
        phone.__init__(self,name,pno)
        Tablet.__init__(self,name,screen_size)
        self.os=os
    def display(self):
        print(self.name,self.pno,self.screen_size,self.os)

s=smartphone("samasung",9963658260,"6inches","tizen")          
s.display()
s.d1()
print("---------sixth program----------")
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def d1(self):
        print(self.name,self.age)
class student(person):
    def __init__(self,name,age,grade):
        person.__init__(self,name,age)
        self.grade=grade
    def d2(self):
        print(self.name,self.age,self.grade)
d=student("vasu",25,"firstclass") 
d.d2() 
d.d1()    
p=person("bharu",26)
p.d1()


      
      
    
   
       
