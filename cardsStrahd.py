# Import required modules
from random import shuffle
  
  
# Common (numbered) cards
class CommonCards:
    global common_suites, common_values
    common_suites = ['Glyphs', 'Coins', 'Stars', 'Swords']
    common_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']
  
    def __init__(self):
        pass

# High (face/joker) cards
class HighCards:
    global high_cards
    high_cards = ['Ghost', 'Innocent', 'Marionette', 'Darklord', 'Mists', 'Executioner', 'Broken One', 'Tempter', 'Beast', 'Donjon', 'Raven', 'Seer', 'Artifact', 'Horseman']
  
    def __init__(self):
        pass

# Define a class to categorize each card
class CommonDeck(CommonCards):
    def __init__(self):
        CommonCards.__init__(self)
        self.mycardset = []

        for n in common_suites:
            for c in common_values:
                self.mycardset.append((c) + " of " + n)
  
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "DECK EMPTY"
        else:
            cardpopped = self.mycardset.pop()
            print("Card removed is", cardpopped)

# Define a class to categorize each card
class HighDeck(HighCards):
    def __init__(self):
        HighCards.__init__(self)
        self.mycardset = []

        for c in high_cards:
            self.mycardset.append(c)

    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            print("Card removed is", cardpopped)
    
    def __str__(self):
        return str(self.mycardset)

# Shuffle common cards
class ShuffleCommonCards(CommonDeck):
    # Constructor
    def __init__(self):
        CommonDeck.__init__(self)
  
    # Method to shuffle cards
    def shuffle(self):
        shuffle(self.mycardset)
        return self.mycardset
  
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            return (cardpopped)

# Shuffle high cards
class ShuffleHighCards(HighDeck):
    # Constructor
    def __init__(self):
        HighDeck.__init__(self)
  
    # Method to shuffle cards
    def shuffle(self):
        shuffle(self.mycardset)
        return self.mycardset
  
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            return (cardpopped)

### MAIN ###
scc = ShuffleCommonCards()
scc.shuffle()
print('Card 1:', scc.popCard())
scc.shuffle()
print('Card 2:', scc.popCard())
scc.shuffle()
print('Card 3:', scc.popCard())

shc = ShuffleHighCards()
shc.shuffle()
print('Card 4:', shc.popCard())
shc.shuffle()
print('Card 5:', shc.popCard())
