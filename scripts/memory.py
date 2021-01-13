#objects in memory and the is operator
a = [5,1,3,7,3]
b = [5,1,3,7,3]
print(id(a))
print(id(b))
print(a is b) #the is operator is used to see if they refer to the same object in memory
print(a==b)

class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

circle1 = Circle(54,"red")
circle2 = Circle(23,"yellow")
circle3 = circle2
print(circle1 is circle2)
print(circle3 is circle2)
circle3.color = "blue"
print(circle2.color)
print(id(circle1))
print(circle1) # is the hexadecimal version of the id which shows the memory address of the object
print(hex(id(circle1)))
print("\n ----------------- \n")
#unexpected results of the is operator
a = "Holberton_School98!"
b = "Holberton_School98!"
print(a is b)
c = "abcd"
d = "".join(["a","b","c","d"])
print(c is d)

print("\n ---------Aliasing-------- \n")

a = {"b":5,"a":24,"c":56}
print(id(a))
z = a
print(id(z)) #same id

class Circle:
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

circle1 = Circle(54,"red")
circle2 = circle1

print("\n ---------Mutabilty-------- \n")

a = [1,2,3,4,5]
a[2] = -5
print(a)
# b = (1,2,3,4,5)
# b[2] = -5
# print(b)

#e = {[1,2,3]:"a",[4,5,6]:"b"}
f = {(1,2,3):"a",(4,5,6):"b"}

print("\n ---------Cloning-------- \n")

a = [1,2,3,4,5]
b = a[:]
print(id(a))
print(id(b))

print("\n ---------Assignment-------- \n")

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
    data1 = data[:]
    for item in data:
        if item == target:
            data1.remove(target)
    return data1
 
def get_product(data):
    data1 = data[:]
    total = 1
    for i in range(len(data1)):
        total *= data1.pop()
    return total
 
print(remove_elem(c, 3))
print(get_product(b))
print(a)