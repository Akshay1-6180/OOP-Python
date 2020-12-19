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


