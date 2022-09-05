import random
import replit
def fruitmachine(bal):

  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  roll3 = random.randint(1,6)

  bell = 2
  skull = 6

  arr = ['🍒','🔔','🍋','🍊','⭐','💀']

  print("""
  
                              .-------.
                              |Jackpot|
                  ____________|_______|____________
                 |  __    __    ___  _____   __    |  
                 | / _\  / /   /___\/__   \ / _\   | 
                 | \ \  / /   //  //  / /\ \\ \   []|  
                 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
                 | \__/\____/\___/   \/     \__/ []| __
                 |===_______===_______===_______===|(  )
                 |===_______===_______===_______===| ||
                 ||*|       |*|       |*|       |*|| ||
                 ||*|       |*|       |*|       |*|| ||
                 ||*| """"", arr[roll1-1], """  |*| """, arr[roll2-1], """  |*| """"", arr[roll3-1], """  |*|| ||
                 ||*|       |*|       |*|       |*|| ||
                 ||*|_______|*|_______|*|_______|*||_//
                 |===_______===_______===_______===|_/
                 |===___________________________===|
                 |  /___________________________\  |
                 |   |                         |   |
                _|    \_______________________/    |_
               (_____________________________________)
  """)

  prize = False

  if prize == False:

    if (roll1 == skull and roll2 == skull and roll3 == skull) and prize == False:
      bal -= bal
      prize = True
    if (roll1 == bell and roll2 == bell and roll3 == bell) and prize == False:
      bal += 5
      prize = True
    if (roll1 == roll2 and roll2 == roll3) and prize == False:
      bal += 1
      prize = True

    if ((roll1 == skull and roll2 == skull) or (roll1 == skull and roll3 == skull) or (roll3 == skull and roll2 == skull)) and prize == False:
      bal -= 1
      prize = True
    if ((roll1 == roll2) or (roll1 == roll3) or (roll3 == roll2)) and prize == False:
      bal += 0.5
      prize = True

    if (roll1 != roll2 and roll1 != roll3 and roll2 != roll3):
      bal -= 0.5
      prize = True
  return bal

def play(bal):
  opt = 0
  while opt != 'Leave' and bal > 0:
    bal = fruitmachine(bal)

    print('Balance £',round(bal,2))
    opt = str(input("Take or Leave "))
    replit.clear()
  if opt == 'Leave':
    win(bal)
balance = 1

def win(bal):
  print("You started with £ 1.0 and left with £",round(bal,2))

play(balance)