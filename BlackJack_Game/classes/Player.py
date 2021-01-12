class Player:
    def __init__(self, name, is_dealer=False):
        self._name = name #we dont want to give public access to any of these attributes
        self._hand = []
        self._is_dealer = is_dealer

    @property
    def name(self):
        return self._name
    
    @property
    def hand(self):
        return self._hand

    @property
    def is_dealer(self):
        return self._is_dealer

    def draw(self, deck):
        self._hand.append(deck.draw())
        return self #return the reference to the object
    
    def show_hand(self, reveal_card = False):
        if not self.is_dealer:
            for card in self._hand:
                card.show()
        else:
            for i in range(len(self._hand)-1):
                self._hand[i].show()

            if reveal_card:
                self.hand[-1].show()
            else:
                print("X")

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value

        return value
