player1 = input(" PLAYER 1 = ")
player2 = input(" PLAYER 2 = ")

import replit
replit.clear()

import random
selected1 = random.randint(1, 6)
selected2 = random.randint(1, 6)
selected3 = random.randint(1, 6)
selected4 = random.randint(1, 6)

player1total = selected1 + selected3


if selected1 == selected3:  
  roll1 = random.randint(1, 6)
  player1total = selected1 + selected3 + roll1
  print(player1,"rolled",roll1,)

if player1total % 2 == 0:
  player1total = player1total + 10
else: 
  player1total = player1total - 5

print(player1,"rolled",selected1,"and",selected3)

if selected1 == selected3:
  print(player1,"rolled too") 

print(player1,"'s score is",player1total)

print("")
#player2 total

player2total = selected2 + selected4

if selected2 == selected4:  
  roll2 = random.randint(1, 6)
  player2total = selected2 + selected4 + roll2

if player2total % 2 == 0:
  player1total = player2total + 10
else: 
  player2total = player2total - 5

print(player2,"rolled",selected2,"and",selected4)

if selected2 == selected4:
  print(player2,roll2,"rolled too") 

print(player2,"'s score is",player2total)


#########################################################################
#                      ROUND         TWO                                #
#########################################################################

round2 = input("Continue to second round? y/n ")
if round2 == "n":
    print("Say no until you reach the fourth round.")
    if player1total > player2total:
        print(player1, "is the winner with", player1total, "points")
    if player2total > player1total:
        print(player2, "is the winner with", player2total, "points")

else:
    print("Invalid key")
if round2 == "y":
    replit.clear()

    player1total = selected1 + selected3


   if selected1 == selected3:
     roll1 = random.randint(1, 6)
     player1total = selected1 + selected3 + roll1
     print(player1,"rolled",roll1,)

 if player1total % 2 == 0:
   player1total = player1total + 10
 else: 
   player1total = player1total - 5

print(player1,"rolled",selected1,"and",selected3)

if selected1 == selected3:
  print(player1,"rolled too") 

print(player1,"'s score is",player1total)

print(" ")
#player2 total

player2total = selected2 + selected4

if selected2 == selected4:  
  roll2 = random.randint(1, 6)
  player2total = selected2 + selected4 + roll2

if player2total % 2 == 0:
  player1total = player2total + 10
else: 
  player2total = player2total - 5

print(player2,"rolled",selected2,"and",selected4)

if selected2 == selected4:
  print(player2,roll2,"rolled too") 

print(player2,"'s score is",player2total)

print(" ")
#########################################################################
#                      ROUND         THREE                              #
#########################################################################

round3 = input("Continue to third round? y/n ")
if round3 == "n":
    if player1total > player2total:
        print(player1, "is the winner with", player1total, "points")
    if player2total > player1total:
        print(player2, "is the winner with", player2total, "points")
    elif player1total == player2total:
        print("Its a draw")
if round3 == "y":
    replit.clear()
    selectedr25 = random.randint(1, 6)
    selectedr26 = random.randint(1, 6)

    if selectedr25 == selectedr26:
        roll5 = random.randint(1, 6)
        print(player1, "Rolled", roll5, "too")
        player1total = (selected1 + selected2 + selectedr21 + selectedr22 +
                        selectedr25 + selectedr26 + roll5)
    else:
        player1total = (selected1 + selected2 + selectedr21 + selectedr22 +
                        selectedr25 + selectedr26)

    print(player1, "rolled", selectedr25, "and", selectedr26)
    selectedr27 = random.randint(1, 6)
    selectedr28 = random.randint(1, 6)

    if selectedr27 == selectedr28:
        roll6 = random.randint(1, 6)
        print(player2, "Rolled", roll6, "too")
        player2total = (selected3 + selected4 + selectedr23 + selectedr24 +
                        selectedr27 + selectedr28 + roll6)
    else:
        player2total = (selected3 + selected4 + selectedr23 + selectedr24 +
                        selectedr27 + selectedr28)

    print(player2, "rolled", selectedr27, "and", selectedr28)

else:
    print("Invalid key")

#########################################################################
#                      ROUND         FOUR                               #
#########################################################################

round4 = input("Continue to fourth round? y/n ")
if round4 == "y":

    replit.clear()

selectedr29 = random.randint(1, 6)

selectedr30 = random.randint(1, 6)
if selectedr29 == selectedr30:
    roll7 = random.randint(1, 6)
    print(player1, "Rolled", roll7, "too")
    player1total = (
        selected1 + selected2 + selectedr21 + selectedr22 + selectedr25 +
        selectedr26 + roll7 + selectedr29 + selectedr30)
else:
    player1total = (selected1 + selected2 + selectedr21 + selectedr22 +
                    selectedr25 + selectedr26 + selectedr29 + selectedr30)

print(player1, "rolled", selectedr29, "and", selectedr30)

print(" ")
selectedr31 = random.randint(1, 6)
selectedr32 = random.randint(1, 6)

if selectedr31 == selectedr32:
    roll8 = random.randint(1, 6)
    print(player2, "Rolled", roll8, "too")
    player2total = (
        selected3 + selected4 + selectedr23 + selectedr24 + selectedr27 +
        selectedr28 + selectedr31 + selectedr32 + roll8)
else:
    player2total = (selectedr31 + selectedr32 + selected3 + selected4 +
                    selectedr23 + selectedr24 + selectedr27 + selectedr28)

print(player2, "rolled", selectedr31, "and", selectedr32)
print(" ")
player2total = (selected3 + selected4 + selectedr23 + selectedr24 + selectedr27
                + selectedr28 + selectedr31 + selectedr32)

if round4 == "n":
    if player1total > player2total:
        print(player1, "is the winner with", player1total, "points")
    if player2total > player1total:
        print(player2, "is the winner with", player2total, "points")
    elif player1total == player2total:
        print("Its a draw")

#########################################################################
#                      ROUND         FIVE                               #
#########################################################################

round5 = input("Continue to fifth round ? y/n ")
if round5 == "y":

    replit.clear()
selectedr33 = random.randint(1, 6)
selectedr34 = random.randint(1, 6)

if selectedr33 == selectedr34:
    roll9 = random.randint(1, 6)
    print(player1, "Rolled", roll9, "too")
    player1total = (selected1 + selected2 + selectedr21 + selectedr22 +
                    selectedr25 + selectedr26 + roll9 + selectedr29 +
                    selectedr30 + selectedr33 + selectedr34)
else:
    player1total = (
        selected1 + selected2 + selectedr21 + selectedr22 + selectedr25 +
        selectedr26 + selectedr29 + selectedr30 + selectedr33 + selectedr34)

print(player1, "rolled", selectedr33, "and", selectedr34)
selectedr35 = random.randint(1, 6)
selectedr36 = random.randint(1, 6)

if selectedr35 == selectedr36:
    roll10 = random.randint(1, 6)
    print(player2, "Rolled", roll10, "too")

    player2total = (selected3 + selected4 + selectedr23 + selectedr24 +
                    selectedr27 + selectedr28 + selectedr31 + selectedr32 +
                    roll10 + selectedr35 + selectedr36)
else:
    player2total = (
        selectedr31 + selectedr32 + selected3 + selected4 + selectedr23 +
        selectedr24 + selectedr27 + selectedr28 + selectedr35 + selectedr36)

print(player2, "rolled", selectedr35, "and", selectedr36)

if round5 == "n":
    if player1total > player2total:
        print(player1, "is the winner with", player1total, "points")
    if player2total > player1total:
        print(player2, "is the winner with", player2total, "points")
    elif player1total == player2total:
        print("Its a draw")
else:
    print("Invalid key")
    replit.clear()

#########################################################################
#                      FINAL         ROLLS                              #
#########################################################################

if player1total == player2total:
    selectedrd1 = random.randint(1, 6)
    selectedrd2 = random.randint(1, 6)

    print(player1, "has rolled", selectedrd1)
    print(player2, "has rolled", selectedrd2)
    print(" ")
    if selectedrd1 > selectedrd2:
        print(player1, "Has won the last roll")
    elif selectedrd2 > selectedrd1:
        print(player2, "Has won the last roll")
    while selectedrd1 == selectedrd2:
        import random
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(player1, "has rolled", d1)
        print(" ")
        print(player2, "has rolled", d2)
        print(" ")
        if d1 > d2:
            print(
                player1,
                "Has won the game with the final roll of",
                d1,
            )
        elif d2 > d1:
            print(player2, "Has won the game with final roll of", d2)
        else:
            print(
                "Wow didn't expected you guys to be at the same score for this roll you both are the winners",
                player1, "and", player2)

print(" ")

x = 5
for x in range(0,1500,1): 
   print("/")
   print(" ")
   print(" ")   
   replit.clear()
   print("-")
   print(" ")
   print(" ")   
   replit.clear()
   print("\ ")
   print(" ")
   print(" ")   
   replit.clear()
   print("-")
   print(" ")
   print(" ")
   replit.clear()

if player1total > player2total and player1total % 2 != 0:
    print(player1, "is the winner with", player1total - 5, "points")

    pt1 = player1total

    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player1)
    hs.write(" ")
    hs.write(str(pt1 - 5))
    hs.write(" \n")
    hs.close

if player1total > player2total and player1total % 2 == 0:
    print(player1, "is the winner with", player1total + 10, "points")

    pt1 = player1total

    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player1)
    hs.write(" ")
    hs.write(str(pt1 + 10))
    hs.write(" \n")
    hs.close

if player2total > player1total and player2total % 2 != 0:
    print(player2, "is the winner with", player2total - 5, "points")
    
    pt2 = player2total

    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player2)
    hs.write(" ")
    hs.write(str(pt2 - 5))
    hs.write(" \n")
    hs.close

if player2total > player1total and player2total % 2 == 0:

    pt2 = player2total

    print(player2, "is the winner with", player2total + 10, "points")
    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player2)
    hs.write(" ")
    hs.write(str(pt2 + 10))
    hs.write(" \n")
    hs.close

elif player1total == player2total:
    print("Its a draw")
    import random
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(player1, "has rolled", d1)
    print(" ")
    print(player2, "has rolled", d2)
    print(" ")
    if d1 > d2:
        print(
            player1,
            "Has won the game with the final roll of",
            d1,
        )
    elif d2 > d1:
        print(player2, "Has won the game with final roll of", d2)
    else:
        print(
            "Wow didn't expected you guys to be at the same score for this roll you both are the winners",
            player1, "and", player2)
print(" ")

#########################################################################
#                          HIGH       SCORES                            #
#########################################################################

pt1 = player1total
pt2 = player2total


if player2total > player1total
    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player2)
    hs.write(" ")
    hs.write(str(pt2))
    hs.write(" \n")
    hs.close

if player1total > player2total
    hs = open("highscores.txt", "a")
    hs.write(" \n")
    hs.write(player1)
    hs.write(" ")
    hs.write(str(pt1))
    hs.write(" \n")
    hs.close