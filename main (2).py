class graphNode:
  def __innit__(self):
    self.value = 0
    self.pointers = []

  def getVal(self):
    return self.value

  def setVal(self,value):
    self.value = value

  def getPointers(self):
    return self.pointers

  def setPointers(self,pointer):
    (self.pointers).append(pointer)
    
class graph:
  def __innit__(self):
    self.nodes = []

  def getNodes(self):
    return self.nodes

  def addNode(self,node):
    (self.nodes).append(node)

  def addEdge(self,node1,node2):
    node1.setPointers(node2.getVal())

  def removeEdge(self,node1,node2):
    (node1.getPointers()).remove(node2)