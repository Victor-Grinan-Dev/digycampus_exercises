# kortin maa (esim. hertta)
class Suit:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# kortti
class PlayingCard:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

        if 1 < value < 11:  # numerokortti
            self.__name = str(value)
        elif 0 < value < 14:    # kuvakortti
            names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
            self.__name = names[value]

    def get_value(self):
        return self.__value

    # tätä metodia kutsutaan, kun kutsutaan str(kortti), kortin ollessa PlayingCard-olio
    def __str__(self):
        return self.__name + " of " + self.__suit.get_name() + "s"

    # toteutetaan luokan vertailu merkkijonon perusteella (EI LIITY TEHTÄVÄÄN)
    def __eq__(self, other):
        if str(other) == str(self):
            return True
        else:
            return False

    # samoin kuin luokan hashaaminen (EI LIITY TEHTÄVÄÄN)
    def __hash__(self):
        return hash(str(self))