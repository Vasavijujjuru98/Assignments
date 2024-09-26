"""1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information."""

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
p=person("vasavi",25,"female")
p.display()
k=person("bhargavi",26,"female")
k.display()
k.age=24
k.display()
"""Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others."""
class company:
    total_emp=0
    def __init__(self):
        pass
    def add_employee(self,name,dept):
        self.name=name
        self.dept=dept
        company.total_emp+=1
    def display(self):
        print(company.total_emp)

p1=company()
p1.add_employee("vasu","it")
p1.display()
p2=company()
p1.add_employee("bharu","python")
p2.display()
"""Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle."""
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        calculate=self.length*self.width
        print(calculate)
r=rectangle(20,4)
r.area()
k=rectangle(10,3)
k.area()
"""Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe"""

class Employee:
    bonus=10000
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    def t_salary(self):
        total_salary=self.salary+Employee.bonus
        print(total_salary)
e=Employee("vasu",20000)
e1=Employee("Bharu",30000)
e1.t_salary()
e.t_salary()
Employee.bonus=5000
e.t_salary()
e1.t_salary()




