import random

# CARD OBJECT
# COLOUR (4 COLOURS / YELLOW RED GREEN BLUE)
# NUMBER (1-9)
# GETNUM()
# GETCOL()
# GETDISPLAY()

class Card:
  def __init__(self,myColour,myNum):
    self.color = myColour
    self.number = myNum
  
  def getCol(self):
    return self.color  

  def getNum(self):
    return self.number

  def display(self):
    dis = ""
    dis += str(self.number)
    dis += str(self.color)
    return dis

# PLAYER OBJECT
# CARDS (CARDS IN PLAYER'S HAND / USE ARRAY)
# GETLENARR()
# INSERTCARD()
# CHOOSE CARD (CHOOSE CARD FROM THE ARRAY / VALIDATE THAT THE CARD IS IN THE ARRAY)
# REMOVE CARD (CHOOSE CARD IS VALID REMOVE THE CARD FROM PLAYER'S DECK)
# GETNUMCARD (CHECKS HOW MANY CARDS THE PLAYER HAS GOT LEFT / RETURN TRUE IF 0)
# IF PLAYER HAS NO SAME COLOUR CARD OR SAME NUMBER(GETTOPCOL() AND GETTOPNUM()) PULL ONE CARD FROM PULL_DECK VIA GETTOP() THEN INSERT THE PULLED CARD VIA INSERTCARD() THEN DELETE FROM PULL DECK VIA REMOVETOP()
class Player:
  def __init__(self,myDeck,myName):
    self.deck = myDeck
    self.name = myName
  
  def getName(self):
    return self.name
  
  def displayDeck(self):
    arr = []
    for x in range(0,len(self.deck)):
      arr.append((self.deck)[x].display())
    return arr

  def getDeck(self):
    return self.deck

  def getDeckLen(self):
    return len(self.deck)
  
  def insertCard(self,Card):
    (self.deck).append(Card)

  def removeCard(self,Card):
    (self.deck).remove(Card)
  
  def chooseCard(self,Card,gameDeck):
    if ((gameDeck.getTopCol() == Card.getCol()) or (gameDeck.getTopNum() == Card.getNum())):    
      
# GAME OBJECT
# IF BOTH PLAYERS HAVE GETLENARR() OF 0 DISTRIBUTE 7 CARDS FROM PULL_DECK VIA GETTOP() AND PLAYER INSERTCARD()
# PUT ON A LOOP UNTIL ONE OF THE PLAYER.GETNUMCARD() RETURNS TRUE
# PRINT PLAYED_DECK.DISPLAY()
# CHECK IF CHOSEN CARD CAN BE PUT ON TOP OF THE PLAYED_DECK (USE PLAYED_DECK.GETTOP())
# IF VALID USE PLAYED_DECK.INSERT()
class game:
  def __init__(self,cards):
    self.player1 = input("Enter Player1 ")
    self.player2 = input("Enter Player2 ")
    self.gameDeck = GameDeck([])

    self.pulldeck = pullDeck(cards)
    self.deck1 = []
    self.player1 = Player(self.deck1,self.player1)

    self.deck2 = []
    self.player2 = Player(self.deck2,self.player2)

    self.pulldeck.shuffle()
    self.pulldeck.begin(self.player1,self.player2,self.gameDeck)

    print(self.player1.getName())
    print(self.player1.displayDeck())

    print(self.player2.getName())
    print(self.player2.displayDeck())

    (self.gameDeck).insert("TEST")
    print(self.gameDeck.displayDeck())

    while(((self.player1).getDeckLen() > 0) and ((self.player2).getDeckLen() > 0)):
      
      (self.player1).chooseCard()
# PLAYED DECK
# USE QUEUE DISPLAY LAST 5 CARDS
# DISPLAY()
# GETTOP()
# INSERT()
# GETTOPCOL()
# GETTOPNUM()
# USE QUEUE
class GameDeck:
  def __init__(self,myDeck):
    self.deck = myDeck
  
  def insert(self,Card):
    (self.deck).append(Card)

  def getTop(self):
    return(self.deck[len(self.deck)-1])

  def getTopCol(self):
    return (self.deck[len(self.deck)-1]).getCol()
  
  def getTopNum(self):
    return (self.deck[len(self.deck)-1]).getNum()
  
  def displayTop(self):
    return (self.deck[len(self.deck)-1]).display()

  def displayDeck(self):
    arr = []
    if len(self.deck) < 5:
      for x in range(0,len(self.deck)-1):
        arr.append((self.deck[x]).display())
    else:
      for x in range(len(self.deck)-5,len(self.deck)-1):
        arr.append((self.deck[x]).display())
    return arr
# PULL DECK
# USE QUEUE HAVE 36 CARDS
# CARDS WILL BE DISTRIBUTED IN A RANDOM ORDER TO EACH PLAYER
# EACH PLAYER WILL HAVE 7 CARDS TO BEGIN WITH
# REMOVETOP()
# GETTOP()
# USE QUEUE

class pullDeck:
  def __init__(self,myDeck):
    self.deck = myDeck
  
  def begin(self,Player1,Player2,GameDeck):
    for y in range(0,6):
      Player1.insertCard((self.deck)[y])
      self.remove((self.deck)[y])
    for x in range(0,6):
      Player2.insertCard((self.deck)[x])
      self.remove((self.deck)[x])
      
    num = random.randint(0,len(self.deck))

    GameDeck.insert(self.deck[num])
    self.remove(self.deck[num])

  def remove(self,Card):
      (self.deck).remove(Card)

  def getTop(self):
    return (self.deck)[0]

  def getTot(self):
    return len(self.deck)

  def shuffle(self):
    random.shuffle(self.deck)
    

cards = [Card("Y",1),Card("Y",2),Card("Y",3),Card("Y",4),Card("Y",5),Card("Y",6),Card("Y",7),Card("Y",8),Card("Y",9),Card("R",1),Card("R",2),Card("R",3),Card("R",4),Card("R",5),Card("R",6),Card("R",7),Card("R",8),Card("R",9),Card("G",1),Card("G",2),Card("G",3),Card("G",4),Card("G",5),Card("G",6),Card("G",7),Card("G",8),Card("G",9),Card("B",1),Card("B",2),Card("B",3),Card("B",4),Card("B",5),Card("B",6),Card("B",7),Card("B",8),Card("B",9),Card("Y",1),Card("Y",2),Card("Y",3),Card("Y",4),Card("Y",5),Card("Y",6),Card("Y",7),Card("Y",8),Card("Y",9),Card("R",1),Card("R",2),Card("R",3),Card("R",4),Card("R",5),Card("R",6),Card("R",7),Card("R",8),Card("R",9),Card("G",1),Card("G",2),Card("G",3),Card("G",4),Card("G",5),Card("G",6),Card("G",7),Card("G",8),Card("G",9),Card("B",1),Card("B",2),Card("B",3),Card("B",4),Card("B",5),Card("B",6),Card("B",7),Card("B",8),Card("B",9)]

game(cards)