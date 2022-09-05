option = False
lc = 0
while option == False:

  import string
  import random
  lis = string.ascii_letters
  print(lis)
  score = 0

  #arrays for loops
  arrnum = []
  arrletter = []
  arrletter_C = arrletter

  #random numbers
  for numb in range(0,6):
    numb = random.randint(0,len(lis))
    arrnum.append(numb)

  #translating numbers to integers
  for y in range(0,len(arrnum)):  
    y_ = lis[arrnum[y]-1]
    if arrnum[y] < 25: 
      score = score + 1
    if arrnum[y] > 25:  
      score = score + 2
    if arrnum[y] == 25: 
      score = score + 3
    if arrnum[y] == 51: 
      score = score + 4
    arrletter.append(y_)
  
  print(score)
  print(arrletter)
  #bonus points
  bonus =  True
  numc = -1
  numc2 = 0
  while bonus == True:  
    numc = numc + 1
    while numc2 < len(arrletter): 
      numc2 = numc2 + 1
      if arrletter[numc] == arrletter[numc2]: 
        arrletter.remove(arrletter[numc2])
        score = score + 1
    if numc > len(arrletter):  
      bonus = False    

  print(arrnum)
  print(arrletter)
  print(score)

  #Used for counting how many turns it takes until the user reaches a score of 11. When found the count resets and the user can continue
  lc = lc + 1
  if score  == 11:
    print("it took",lc,"turns to find 11")
    cont = input("Do you want to continue? press enter or enter n: ")
    lc = 0
    if cont == "n":
      print("Goodbye!")
      option = True 
   
  
  nturn=input("Press enter to continue to your next turn.")