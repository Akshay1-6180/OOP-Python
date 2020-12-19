#-------------GETTERS AND SETTERS-------------#
class Dog:
    
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else :
            print("enter a valid name")
        


dog1 = Dog("snoopy")
print(dog1.get_name())
dog1.set_name("bruno")
print(dog1.get_name())
dog1.set_name(1234)

#--- example of getter and setter---#

class Patient:

    def __init__(self, name, age, id_num, num_children=0):
        self.name = name
        self.age = age
        self._id_num = id_num #protected hence should not be acceses from outside
        self._num_children = num_children #protected hence should not be acceses from outside

    @property
    def id_num(self):
        print("getter")
        return self._id_num;

    @id_num.setter
    def id_num(self, id):
        print("setter")
        if isinstance(id,str):
            self._id_num = id

        else:
            print("not a valid id")
        
    @id_num.deleter
    def id_num(self):
        print("deletor")
        del self._id_num

    @property
    def num_children(self):
        print("getter")
        return self._num_children

    @num_children.setter
    def num_children(self, numchild):
        
        if isinstance(numchild, int) and (0 < numchild < 70):
            self._num_children = numchild

        else:
            print("not a valid number of children")
    

# patient2 = Patient("ram",24,"45672",2)
# print(patient2.get_id_num())
# print(patient2.get_num_children())
# patient2.set_id_num(456)
# patient2.set_num_children(-2)

patient1 = Patient("ram",24,"45672",2)
print(patient1.id_num) # we are actually calling the getter method
patient1.id_num = "8456" # we are actually calling the setter method

#del patient1.id_num
#print(patient1.id_num)

#Calculator Class 

class Calculator:
    
    def __init__(self, model, year, serial_num):

        self.model = model
        self.year = year
        self._serial_num = serial_num #protected variable

    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        if a >= b:
            return a - b
        else:
            raise ValueError("a is smaller than b")

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if(b != 0):
            return a/b
        else:
            raise ValueError("Denominator b is 0")

my_calculator = Calculator("casio", 2005, "4513584")
print(my_calculator.add(5,4))
#print(my_calculator.subtract(6,7)) #will raise value error
print(my_calculator.subtract(8,7))
print(my_calculator.multiply(4,5))
print(my_calculator.divide(8,7))

#--------Alternate syntax to call a method---------#
class Bus:
     
    def __init__(self, color):
        self._color = color
	
    def welcome_student(self, student_name):
        print(f"Hello {student_name}, how are you today? ,the bus has a great {self._color} color ")

bus = Bus("blue")
Bus.welcome_student(bus, "Johnathan") 
bus.welcome_student("Johnathan")

#----calling methods from another methods---#
class CashRegister:
    
    tax = 0.05

    def __init__(self, cashier, serial):
        self.cashier = cashier
        self._serial = serial

    @property
    def serial(self):
        return self._serial

    def display_total(self, subtotal):
        print("=== Welcome to our store ===")
        print("The subtotal is:", subtotal)
        print("The tax is:", self._calculate_tax(subtotal))
        print("-----------------------")
        print("The total is:", self._calculate_total(subtotal))

    def _calculate_total(self, subtotal):
        return subtotal + self._calculate_tax(subtotal)

    def _calculate_tax(self, amount):
        return amount * CashRegister.tax
        
register = CashRegister("Melanie", "3453513")
register.display_total(5022.5) # we cant call _calculate_total and _calculate_tax as they are non public methods

#-------Method Chaining----------#

class Pizza:

    def __init__(self):
        self.toppings = []

    def add_topping(self, toppping):
        self.toppings.append(toppping)
        return self #returns the object instance

    def display_topping(self):
        print("the toppings this pizza has are")
        for topping in self.toppings:
            print(topping)

pizza = Pizza()
pizza.add_topping("olives").add_topping("cheese").add_topping("tomato").display_topping()

print("\n using \\ \n ")
#or another way
pizza.add_topping("chicken")\
    .add_topping("rabbit")\
    .add_topping("capsicum") \
    .display_topping()