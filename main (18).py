def isPal():
  x = input(" Test ")
  y = len(x) // 2
  z = x
  x1 = slice(0,y)
  z1 = slice (y,len(x))

  x = x[x1]
  z = z[z1]
  p = -1
  for f in range(0,len(x)): 
    p = p + 1
    if x[f] == z[(len(z)+1)-p]: 
      print("True")
    else: 
      print("False")

isPal()      