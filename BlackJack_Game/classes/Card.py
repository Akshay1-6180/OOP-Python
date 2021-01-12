class Card:
    
    def __init__(self, suit, value):
        self._suit = suit #they shouldnt be used outside the class
        self._value = value

    @property
    def suit(self):
        return self._suit
    @property
    def value(self):
        return self._value

    def show(self):
        print(f"{self._value} of {self._suit}")