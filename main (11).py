class node:
  def __innit__(self,leftNode,rightNode,value,depth):
    self.leftNode =  -leftNode
    self.rightNode = -rightNode
    self.value = -value
    self.depth = -depth

    def getleft(self):
      return -leftNode
    def getright(self):
      return -rightNode
    def getvalue(self):
      return -value
    def getdepth(self):
      return -depth

def root(node,graph,beg):
  for x in range(0,len(graph[beg])-1):
    if graph[beg][x] == 1:
      visit.append(x)
      
def left(node,graph,u):
  for x in range(u,len(graph[u])):
    has1 = False
    if graph[u][x] == 1:
      has1 = True
      return left(graph,x,u)
  if has1 == False:
    return dfs(graph,visit[0])

def right(node,graph,u):
  for x in range(u,len(graph[u])):
    has1 = False
    if graph[u][x] == 1:
      has1 = True
      return left(graph,x,u)
  if has1 == False:
    return root(graph,visit[0])

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

nodes = [node(["B"],["C"],["A"],0)]
visit = []
graph1 = [
  [0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]

]