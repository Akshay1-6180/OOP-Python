import random

#we need to create two classes Playerclass and board class
#player class - 
#---marker( X(user, default) , 0(compter))
#---is_human (true(user), false(computer))
class Player:

    def __init__(self, is_human=True):
        self._is_human = is_human

        if(self._is_human):
            self._marker = "X"
        else:
            self._marker = "0"

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    #methods
    def get_player_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        move = input("Player move (X) : ")
        return move


    def get_computer_move(self):
        row = random.choice([1, 2, 3])
        col = random.choice(["A", "B", "C"])

        move = str(row) + col
        print("Computer move (0) : ", move)

        return move
