arr = [3,9,5,6,7,1,51,29,18]
arr2 = [3,9,5,6,7,1,51,29,18]
cyc = 0
for x in range(1,len(arr)):
  y = x
  while y != 0 and arr[y] < arr[y-1]:
    temp = arr[y-1]
    arr[y-1] = arr[y]
    arr[y] = temp
    y -= 1
    cyc += 1
    print(arr)

print(cyc)

cyc2 = 0
swap = True

while swap == True:
  cyc2 = cyc2 + 1
  swap = False
  for x1 in range(0,(len(arr2)-1)): 
    if arr2[x1] > arr2[x1+1]: 
      swap = True
      temp2 = arr2[x1]
      arr2[x1] = arr2[x1+1]
      arr2[x1+1] = temp2
      print(arr2)

print(cyc2)

if cyc2 < cyc:
  print("Bubble sort is more efficient it took",cyc2,"cycles while insertion sort took ",cyc,"cycles")
else:
  print("Insertion sort is more efficient it took",cyc,"cycles while bubble sort took ",cyc2,"cycles")