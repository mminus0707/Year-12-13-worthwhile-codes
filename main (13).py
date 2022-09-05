import random
graph = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 1, 0]
]

pos = 8
dest = 0

def nav(current):
  global dest
  if current != dest:
    arr = []
    for x in range(0,len(graph)):
      if (graph[current][x] == 1) and (x < current):
        arr.append(x)
    print(arr)
    nextdest = int(input("Next available nodes, choose one "))
    found = False
    for y in range(0,len(arr)):
      if arr[y] == nextdest:
        found = True
    while found != True:
      print(arr)
      nextdest = int(input("Next available nodes, choose one "))
      found = False
      for y in range(0,len(arr)):
        if arr[y] == nextdest:
          found = True
    xyz = random.randint(0,100)
    if xyz > 65:
      if nextdest == arr[random.randint(0,len(arr)-1)]:
        print("You stepped on a mine and died")
        exit()
    if found == True:
      current = nextdest
      nav(nextdest)
  else:
    print("You have reached your destination")

nav(pos)