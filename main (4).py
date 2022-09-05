#Word input

import replit
import random

words = ["zombie","funny","apple","pirate","planet","school","ocean","computer","science","defragmentation","helicopter","rocket"]

number = round(random.randint(0,len(words)-1))

word = words[number]
arr = []
usedletters = []
replit.clear()
man = """
"""
#Game

tries = 10

#creates an array to hide letters
for x in range(0,len(word)):
  arr.append("_")
#while player is not out of tries game plays
while tries > 0:
  found = False        
  if tries == 10:
    print("""
     
      
      
      
      


    """)
  if tries == 9:
    print("""
     
      
      
      
      
      
=========
    """)
  if tries == 8:
    print("""

      |
      |
      |
      |
      |      
=========
    """)
  if tries == 7:
    print("""
 +----+
      |
      |
      |
      |
      |      
=========
    """)
  if tries == 6:
    print("""
 +----+
 |    |
      |
      |
      |
      |      
=========
    """)
  if tries == 5:
    print("""
 +----+
 |    |
 o    |
      |
      |
      |      
=========
    """)
  if tries == 4:
    print("""
 +----+
 |    |
 o    |
 |    |
      |
      |      
=========
    """)
  if tries == 3:
    print("""
 +----+
 |    |
 o    |
 |\   |
      |
      |      
=========
    """)
  if tries == 2:
    print("""
 +----+
 |    |
 o    |
/|\   |
      |
      |      
=========
    """)
  if tries == 1:
    print("""
 +----+
 |    |
 o    |
/|\   |
  \   |
      |      
=========
    """)
  print(arr)  
  letter = str(input("Enter a letter "))
  print("Used letters",usedletters)
  if len(letter) > 1:
    if letter.lower() == word.lower():
      print("Correct")
      found = True
      exit()
    else:
      tries -= 1
  else:
    ings = False
    if len(usedletters) != 0:
      for z in range(0,len(usedletters)):
        if usedletters[z].lower() == letter.lower():
          ings = True
          print(usedletters[z])
    if ings == False:
      usedletters.append(letter)    
      for x in range(0,len(word)):
        if letter.lower() == word[x].lower():
          arr[x] = letter
          found = True
      if found == False:
        tries -= 1
else:
  print("""
 +----+
 |    |
 o    |
/|\   |
/ \   |
      |      
=========
    """)
  print("Word was",word)