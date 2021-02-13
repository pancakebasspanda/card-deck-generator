import collections
from random import choice

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# sorting spades, hearts, diamonds, clubs and then numbers with ace being the highest
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print('rank_value: ', rank_value) # rank value based on 0-10, JKQA
    print('suit_values: ', len(suit_values)) # no of suites
    print('suit_values[card.suit]: ', suit_values[card.suit])  # rank based on suit

    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # list of tuples
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':

    Card = collections.namedtuple('Card', ['rank', 'suit'])

    ace_of_spades = Card('A', 'spades')
    print(ace_of_spades)

    print(len(ace_of_spades))

    deck = FrenchDeck()

    print(len(deck))

    # get an item from the deck
    print(deck[0]) # Card(rank='2', suit='spades')
    print(deck[-1]) # Card(rank='A', suit='hearts')

    print(choice(deck)) # random card

    print(deck[:3])  # supports slicing

    value = spades_high(ace_of_spades)  # highest value 51
    print(value)

    value = spades_high(Card('2', 'clubs'))  # lowest value 0
    print(value)

    value = spades_high(Card('2', 'Diamonds'))  # 1
    print(value)






