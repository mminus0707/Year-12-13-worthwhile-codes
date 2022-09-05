num = input("Enter your number (numbers must be between 1 and 4) ")
arr = []
fine = False
while fine == False:  
  if len(num) > 6 or len(num) < 6:  
    num = input("Make sure that its 6 digits ")
  else: 
    for o in range(0,len(num)): 
      if int(num[o]) > 4:  
        num = input("Make sure that numbers are between 1 and 4 ")
      else:
        fine = True
if fine == True:
  for x in range(0,len(num)): 
    for y in range(0,int(num[x])):
      arr.append("▮")
    arr.append(" ")
  for z in range(0,4):  
    print(*arr, sep='')