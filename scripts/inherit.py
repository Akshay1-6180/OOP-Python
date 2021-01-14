class Dog:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Poodle(Dog):

    def poodle_introduction(self):
        print(f"Hi my name is {self.name} and my age is {self.age}")

poodle1 = Poodle("Snoopy",24,"blue")
poodle1.poodle_introduction()

class Vehicle:

    def __init__(self, speed, miles, price):
        self.speed = speed
        self.miles = miles
        self.price = price


    def hello(self):
        print(f"hello at {self.speed}")
        print(f"hello at {self.speed} and {self.miles}")

class Truck(Vehicle):

    def __init__(self, speed):
        #Vehicle.__init__(self, speed, miles, price)

        self.speed = speed

t1 = Truck(24)
print(t1.speed)
#t1.hello()

#---assignemnt---

class Electronic_Device:
    
    def __init__(self, chargable, cost, portable, company):
        self.chargable = chargable
        self.cost = cost
        self.portable = portable
        self.company = company

class Computer(Electronic_Device):

    def __init__(self, chargable, cost, portable, company, memory):
        super().__init__(chargable, cost, portable, company)
        self.memory = memory

class TV(Electronic_Device):

    def __init__(self, chargable, cost, portable, company, screen_type):
        super().__init__(chargable, cost, portable, company)
        self.screen_type = screen_type

class Desktop(Computer):

    def __init__(self, chargable, cost, portable, company, memory, frame_rate):
        super().__init__(chargable, cost, portable, company, memory)
        self.frame_rate = frame_rate

class Laptop(Computer):
    
    def __init__(self, chargable, cost, portable, company, memory, operating_system):
        super().__init__(chargable, cost, portable, company, memory)
        self.operating_system = operating_system


#-----------inheritence method-----

class Teacher:
    
    def __init__(self, name, age, class_code):
        self.name = name
        self.age = age
        self.class_code = class_code

    def welcome_students(self):
        print("Welcome, dear students...")

class PhysicsTeacher(Teacher):

    def welcome_students(self):
        super().welcome_students()
        print("Let's start our physics class")

class BiologyTeacher(Teacher):

    def welcome_students(self):
        super().welcome_students()
        print("Let's start our biology class")

b1 = BiologyTeacher("aksh", 12, 404)
b1.welcome_students()
