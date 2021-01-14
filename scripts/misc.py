def add(a,b):
    """add two integers and return the resulting integer"""
    return a + b
#using docstring
#help(add) gives info
print(add.__doc__)

def frequency_dict(data):
    """Return a dictionary with the numner of occurances of each value in the list

    Create a dictionary that maps each element of the list (key) 
    to the number of times it appears in the list

    Args:
        data: A list of values of an immutable data type
            These values can be integers, booleans, tuples or strings
    Return:
        A dictionary mapping each value (key) with its frequency.
        For example, this function call:

        a = [1, 6, 2, 6, 2]

        returns this dictionary

        {1:1, 6:2, 2:2} 
    
    Raise:
        ValueError: if the list is empty
    """

    if not data:
        raise ValueError("The list cannot be empty")
    
    freq = {}

    for elem in data:
        if elem not in freq:
            freq[elem] = 1

        else:
            freq[elem] +=1

    return freq

#print(frequency_dict.__doc__)

#-----docsrings assignment---

class Flight:

    """Class that represents the details about the flight. 
    Attributes: 
        number (int): the unique number assicated with the flight.
        origin (str): the origin of the flight.
        destination (str): the destination of the flight.
        num_passengers (int): the total number of passsengers in the flight.
        total_weight (float) : the total weight of the flight.
        pilot(str):the name of the pilot.
        crew(list): the list of names of the crew members.
    Methods: 
        display_flight_data(): displays the four essenttial details about the flight data.
    """
    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """Initalize the values of the instance attributes of an instance of Flight. 
        Args: 
            number (int): the unique number assicated with the flight.
            origin (str): the origin of the flight.
            destination (str): the destination of the flight.
            num_passengers (int): the total number of passsengers in the flight.
            total_weight (float) : the total weight of the flight.
            pilot(str):the name of the pilot.
            crew(list): the list of names of the crew members.
        """ 
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot 
        self._crew = crew
    
    @property
    def total_weight(self):
        """total weight of the flight.""" 
        return self._total_weight
    
    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight	
    
    @property
    def pilot(self):
        """The name of the pilot.""" 
        return self._pilot
    
    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot
        
    @property
    def crew(self):
        """The list of names of the crews"""
        return self._crew
    
    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew
    
    def display_flight_data(self):
        """Display flight_data in a human-readable format.""" 
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self.total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)

#help(Flight)

#----------Special methods-----

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cordinates = {"x": self.x, "y": self.y}

    def __str__(self):
        return f"Cordinates : {self.x} , {self.y}"
    
    def __len__(self):
        """Distance from the origin"""
        return round((self.x**2 + self.y**2)**(1/2))

    def __getitem__(self, cord):
        return self.cordinates[cord]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y  + other.y
        return Point(x,y)

    def __bool__(self):
        return self.x > self.y

    def __lt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other):
        return (self.x != other.x) or (self.y != other.y)

    def __gt__(self, other):
        return self.x > other.x

    def __ge__(self, other):
        return self.x >= other.x

p1 = Point(2,4)

#print(p1)
#print(len(p1))
#print(p1["x"])
p2 = Point(6,3)
p3 = p1 + p2
#print(p3)
# print(bool(p2))
# print(bool(p1))
print(p1<p2)
print(p1>p2)
print(p1<=p2)
print(p1>=p2)
print(p1==p2)
print(p1!=p2)