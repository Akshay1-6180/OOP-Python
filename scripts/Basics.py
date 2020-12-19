#-------------GETTERS AND SETTERS-------------#
class Patient:

    def __init__(self, name, age, alergies=None, num_children = 0):
        self.name = name
        self.age = age
        self.alergies = alergies
        self.num_children = num_children
    
    def printObject(self):
        print(self.name,self.age,self.alergies,self.num_children)
person1 = Patient("ram",12)
person2 = Patient("ram",12,["peanuts"])
person3 = Patient("ram",12,["peanuts"],5)
person4 = Patient("ram",12,num_children=5) #to omit an argument we have to specify which paramter

person1.printObject();
person2.printObject();
person3.printObject();
person4.printObject();

class Bacteria:

    def __init__(self, x, y, species, half_life=100 , mutation_rate=None):
        
        self.x = x
        self.y = y
        self.species = species
        self.mutation_rate = mutation_rate
        self.half_life = half_life #in days

newBacteria1 = Bacteria(15.0,25.0,"E. coli")
newBacteria2 = Bacteria(75.0,15.0,"Lentisphaerae",150)
newBacteria3 = Bacteria(45.0,29.0,"Nitrospirae",178,"frequent")

class Donut:
        def _init__(self, flavor, toppings, filling, size):
                self.flavor = flavor
                self.toppings = toppings
                self.filling = filling
                self.size = size

class Customer:
    	def _init_(self, name, age, address, favorite_dessert):
		    self.name = name
		    self.age = age
		    self.address = address
		    self.favorite_dessert= favorite_dessert

class Cake:


	def __init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality



class Car:

    seats = 4

    def __init__(self, model):
        self.model = model

    def printModel(self):
        print("the class atribute inside is " + str(Car.seats))
        print("the instance atribute inside is " + str(self.seats))

car1 = Car("tesla")

print(car1.seats)
print(Car.seats)
#modifing the class atribute
Car.seats = 10
car1.seats = 15

print("acccesing class attribute outisde the class " + str(Car.seats))
car1.printModel()

class A:

    attr = 5

    def __init__(self):
        A.attr +=1

a1 = A()
a2 = A()
print(A.attr)
A.attr = 26
a3 = A()
print(A.attr)

#an example of a payroll system
class Programmer:
    
     # Add the class attributes

    salary = 1000000
    monthly_bonus = 10000
    
    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
 
class Assistant:
    
    # Add the class attributes
    salary = 500000
    monthly_bonus = 100000

    def __init__(self, name, age, address, phone, bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.bilingual = bilingual
 
# Program ==================================================================
 
# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month
def calculate_payroll(employees):
 
    total = 0
 
    print("\n========= Welcome to our Payroll System =========\n")
 
    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
 
    # Display the total 
    print("\nThe total payroll this month will be: $", total)
 
# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)
 
# List of instances
employees = [jack, isabel, nora]
 
# Function call - Passing the list of instances as argument
calculate_payroll(employees)

class Cars:
    
    seats = 4

    def __init__(self, model, year, id_num, serial_num):
        self.model = model
        self.year = year
        self._id_num = id_num
        self.__serial_num__ = serial_num

car1 = Cars("teska", 2006, 2010, "546876136476")
print(car1._id_num)
print(car1.__serial_num__)
class Book:
     
	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self.author = author
		self.num_pages = num_pages
		self.ISBN = ISBN
		self.publisher = publisher

