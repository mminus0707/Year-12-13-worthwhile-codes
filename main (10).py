values = ["A","B","C","D","E","F","G"]
graph1 = [
  [0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]

]

#   A
#  B C
#  E D
#  F G

visited = ['A']

def shortestpath(graph,dest,visited):

  for x in range(0, len(graph1)):
    for y in range(0, len(graph1[x])):
      if graph1[x][y] == 1:
        visited.append(values[y])
        if values[y] == dest:
          print(visited)



shortestpath(graph1,"F",visited)