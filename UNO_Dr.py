class Card:

  def __init__(self, pNumber, pColour):
    self.number = pNumber
    self.colour = pColour
    #constructor

  def getNumber(self):
    return self.number
    #gets the number of the card

  def getColour(self):
    return self.colour
    #gets the coolour of the card

import random

class Deck:
  
  def __init__(self):
    self.size = 0
    self.deck = []
  #constructor

  def addCard(self, card):
    self.deck.append(card)
    self.size = self.size + 1
  #adds card to the deck increments the deck size

  def removeLastCard(self):
    if self.size == 0:
      return False
    else:
      self.size = self.size - 1
      card = self.deck.pop()
      return card
    #checks if the size is 0 if not pops the top element decrements the deck size

  def removeCard(self, card):
    if card in self.deck:
      self.deck.remove(card)
      self.size = self.size - 1
      return True
    else:
      return False
  #checks whether if the selected card is in the deck if it is in the deck then removes it and decrements the size by one if successful returns True else False

  def removeCardStr(self, cardstr):
    if len(cardstr) != 2:
      return False
    else:
      for c in self.deck:
        if c.getColour() == cardstr[0] and c.getNumber() == cardstr[1]:
          self.removeCard(c)
          return c
      return False
  #if the length is not equal to 2 returns false else for every card in deck gets their colour and if its equal to the colour of cardstr removes it and returns the index
    
    if card in self.deck:
      self.deck.remove(card)
      self.size = self.size - 1
      return True
    else:
      return False

  def getDeck(self):
    return self.deck
  #returns the deck

  def setDeck(self, pDeck):
    self.deck = pDeck
  #setter for the deck

  def getSize(self):
    return self.size
  #gets the size of the deck

  def showDeck(self):
    hand = []
    for card in self.deck:
      c = card.getColour() + card.getNumber()
      hand.append(c)
    return hand
  #displays the deck

  def shuffle(self):
    random.shuffle(self.deck)
  #shuffles the deck

  def buildDeck(self):
    colours = ["B", "G", "R", "Y"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    self.deck = []
    for c in colours:
      for n in numbers:
        newCard = Card(n, c)
        self.deck.append(newCard)
    self.size = 40
    self.shuffle()
  #goes through each available colour and number and builds a deck


class Player(Deck):

  def __init__(self, pName):
    self.__name = pName
    super().__init__()
    #player constructor with name that is set afterwards

  def getName(self):
    return self.__name
    #returns the name of the player

class Discard(Deck):
  
  def __init__(self):
    super().__init__()

  def peek(self):
    lCard = super().removeLastCard()
    if lCard == False:
      return False
    else:
      super().addCard(lCard)
      lCardStr = lCard.getColour() + lCard.getNumber()
      return lCardStr
  #if there is a card in the deck it displays its color and number

  def peekCard(self):
    lCard = super().removeLastCard()
    super().addCard(lCard)
    if lCard == False:
      return False
    else:
      return lCard
  #returns the card class if there is a card in the deck

  def addCard(self, card):
    lCard = super().removeLastCard()
    if lCard == False:
      super().addCard(card)
      return True
    else:
      if lCard.getColour() == card.getColour() or lCard.getNumber() == card.getNumber():
        super().addCard(lCard)
        super().addCard(card)
        return True
      else:
        super().addCard(lCard)
        return False
    #removes the last card in the dispaly global variable if there isnt anything and the card matches with the colour or number then add the current to the displayed game deck if correct add the lastcard and card into the global variable if not return false and add lastcard back to super


class Game:

  def __init__(self, pplayers):
    self.__players = pplayers
    self.__deck = Deck()
    self.__deck.buildDeck()
    self.__discard = Discard()
  #constructr with pplayers deck and discard builds the deck itself

  def dealout(self):
    #Initializing
    self.__deck.buildDeck()
    self.__discard.setDeck([])
    for p in self.__players:
      p.setDeck([])

    #Dealing out giving out cards 
    for i in range(0,6):
      for p in self.__players:
        movedCard = self.__deck.removeLastCard()
        p.addCard(movedCard)
    
    movedCard = self.__deck.removeLastCard()
    self.__discard.addCard(movedCard)
    #discards the pulled card from the deck

  def canPlay(self, p):
    lCard = self.__discard.peekCard()
    for c in p.getDeck():
      if c.getColour() == lCard.getColour() or c.getNumber() == lCard.getNumber():
        return True
    return False
  #validation of the players deck

  def takeCard(self, p):
    size = self.__deck.getSize()
    if size == 0:
      self.__deck.buildDeck()
  #takes card from the deck and adds it to the player deck

    card = self.__deck.removeLastCard()
    p.addCard(card)

#parameter being which round it is
  def playRound(self, i):
    print(" ")
    print("Round", str(i))
    #for each player in the players array it will get their turn
    for p in self.__players:
      name = p.getName()
      print(" ")
      print("It is now", name, "'s turn")
      print("Discard:", self.__discard.peek())
      print(name, "'s hand:", p.showDeck())
      #if the player has a card that can be played it plays
      if self.canPlay(p):
        needToChoose = True
        while needToChoose:
          print("Which card would you like to play?")
          choice = input("You choose: ")
          success = p.removeCardStr(choice)
          if success == False:
            print("Invalid. Please try again.")
          else:
            validPlay = self.__discard.addCard(success)
            if validPlay:
              needToChoose = False
              if p.getSize() == 0:
                print("Game Over!")
                return p
            else:
              print("Invalid Play. Please choose a different card.")
              p.addCard(success)
      else:
        print("You could not play.")
        self.takeCard(p)
        print("Your new hand:", p.showDeck())
        self.rebound(i,p)

    return False

  def rebound(self,i,p):
      if self.canPlay(p):
        needToChoose = True
        while needToChoose:
          print("Which card would you like to play?")
          choice = input("You choose: ")
          success = p.removeCardStr(choice)
          if success == False:
            print("Invalid. Please try again.")
          else:
            validPlay = self.__discard.addCard(success)
            if validPlay:
              needToChoose = False
              if p.getSize() == 0:
                print("Game Over!")
                return p
            else:
              print("Invalid Play. Please choose a different card.")
              p.addCard(success)
      else:
        print("You could not play.")
        self.takeCard(p)
        print("Your new hand:", p.showDeck())
        self.rebound(i,p)

  def playGame(self):
    canContinue = True
    round = 1
    while canContinue:
      check = self.playRound(round)
      if check == False:
        round = round + 1
      else:
        canContinue = False
        print("Congratulations", check.getName())