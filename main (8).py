class Player:
  def __init__(self,name,side):
    self.__name = name
    self.___side = side
  
  def getside(self):
    return self.___side
  
  def getname(self):
    return self.__name

class Grid:
  def __init__(self):
    self.__grid = {
      'A1' : 'E',
      'A2' : 'E',
      'A3' : 'E',
      'B1' : 'E',
      'B2' : 'E',
      'B3' : 'E',
      'C1' : 'E',
      'C2' : 'E',
      'C3' : 'E',
    }

  def mark(self,spot,player):
    if self.__grid[spot] == "E":
      self.__grid[spot] = player.getside()
    elif self.__grid[spot] == player.getside():
      print("You have already claimed this")
    else:
      print("Other player has already claimed this")
      respot = str(input("Enter a different spot"))
      self.remark(respot,player)
  
  def remark(self,spot,player):
    if self.__grid[spot] == "E":
      self.__grid[spot] = player.getside()
    elif self.__grid[spot] == player.getside():
      print("You have already claimed this")
    else:
      print("Other player has already claimed this")
      respot = str(input("Enter a different spot "))
      self.remark(respot,player)

  def showGrid(self):
    print(' ',1,2,3)
    print('A',self.__grid["A1"],self.__grid["A2"],self.__grid["A3"])
    print('B',self.__grid["B1"],self.__grid["B2"],self.__grid["B3"])
    print('C',self.__grid["C1"],self.__grid["C2"],self.__grid["C3"])

  def haswon(self,player):
    if self.__grid["A1"] == player.getside() and self.__grid["A2"] == player.getside() and self.__grid["A3"] == player.getside():
      return True
    if self.__grid["B1"] == player.getside() and self.__grid["B2"] == player.getside() and self.__grid["B3"] == player.getside():
      return True  
    if self.__grid["C1"] == player.getside() and self.__grid["C2"] == player.getside() and self.__grid["C3"] == player.getside():
      return True  
    if self.__grid["A1"] == player.getside() and self.__grid["B1"] == player.getside() and self.__grid["C1"] == player.getside():
      return True  
    if self.__grid["A2"] == player.getside() and self.__grid["B2"] == player.getside() and self.__grid["C2"] == player.getside():
      return True  
    if self.__grid["A3"] == player.getside() and self.__grid["B3"] == player.getside() and self.__grid["C3"] == player.getside():
      return True  
    if self.__grid["A1"] == player.getside() and self.__grid["B2"] == player.getside() and self.__grid["C3"] == player.getside():
      return True     
    if self.__grid["A3"] == player.getside() and self.__grid["B2"] == player.getside() and self.__grid["C1"] == player.getside():
      return True   
    else:
      return False

def play(p1, p2, grid):
  win = False
  for x in range(0,9):
    if (x % 2) == 0:
      spot1 = str(input("Enter a spot player1 "))
      grid.mark(spot1,p1)
      grid.showGrid()
      if grid.haswon(p1) == True:
        print(p1.getname(),"wins")
        win = True
        break
    else:
      spot2 = str(input("Enter a spot player2 "))
      grid.mark(spot2,p2)    
      grid.showGrid()
      if grid.haswon(p2) == True:
        print(p2.getname(),"wins")
        win = True
        break
  if win == False:
    print("Tie")

grid = Grid()

player1 = Player("Ege","X")
player2 = Player("Oguz","O")

grid.showGrid()
play(player1,player2,grid)