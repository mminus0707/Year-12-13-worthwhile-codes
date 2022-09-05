values = ["A","B","C","D","E","F","G",]
graph0 = [
  [0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]

]

graph1 = [
  [0, 1, 0, 1, 1, 0, 0],
  [1, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0],
  [1, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0]

]

stack = []
visit = []

stack.append(values[0])

def dfs(graph,beg,dest):
  global stack
  global visit
  for x in range(0,len(graph[beg])-1):
    if graph[beg][x] == 1:
      visit.append(x)
      
  for z in range(0,len(visit)-1):
    u = visit[z]
    if (values[u] not in stack) == True:  
      stack.append(values[u])
    visit.remove(visit[z])
    return visitdfs(graph,u,dest)

def visitdfs(graph,u,dest):
  for x in range(u,len(graph[u])):
    if values[u] == dest:
      print(stack)
      exit()
    has1 = False
    if graph[u][x] == 1:
      has1 = True
      if (values[x] not in stack) == True:
        stack.append(values[x])
      return visitdfs(graph,x,dest)
  if has1 == False:
    return dfs(graph,visit[0],dest)

dfs(graph1,0,"A")
