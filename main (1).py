import time
import replit

graph = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def fillgraph(graph,numrows):
  for x in range(0,len(graph)):
    for y in range(0,numrows):
      graph[x].append(" ")

def fillrow(graph,row,numrows):
  for x in range(0,numrows):
    graph[row].append(" ")

def displaygraph(graph):
  for x in range(0,len(graph)):
    print(graph[x])

def shape1():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-1] = "X"
  graph[3][(len(graph[0]) // 2)-1] = "X"

def shape2():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-2] = "X"

def shape3():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)] = "X"

def shape4():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[0][(len(graph[0]) // 2)] = "X"
  graph[1][(len(graph[0]) // 2)] = "X"

def shape5():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-2] = "X"
  graph[1][(len(graph[0]) // 2)] = "X"

def shape6():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[0][(len(graph[0]) // 2)-2] = "X"
  graph[1][(len(graph[0]) // 2)] = "X"

def shape7():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[0][(len(graph[0]) // 2)] = "X"
  graph[1][(len(graph[0]) // 2)-2] = "X"

def shape8():
  graph[0][(len(graph[0]) // 2)-1] = "X"
  graph[1][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-1] = "X"
  graph[2][(len(graph[0]) // 2)-2] = "X"

def check():
  for x in range(0,len(graph[len(graph)-1])):
    if graph[len(graph)-1][x] == "X":
      return True
    else:
      return False

def move():
  num = 0
  while check() != True:
    time.sleep(2)
    replit.clear()
    temp = 0
    print(num)
    temp = graph[num+2]
    graph[num+2] = graph[num+1]
    graph[num+3] = temp
    graph[num+1] = graph[num]
    graph[num] = []
    fillrow(graph,num,10)
    num += 1
    displaygraph(graph)

fillgraph(graph,10)
shape4()
move()