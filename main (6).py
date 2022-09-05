height = int(input("Height: "))
width = int(input("Width: "))
width1 = ""
height1 = "*"
for x in range(0,width):
  width1+="*"
for y in range(0,width-2):
  height1 += " "
height1 += "*"
print(width1)
for z in range(0,height-2):
  print(height1)
print(width1)