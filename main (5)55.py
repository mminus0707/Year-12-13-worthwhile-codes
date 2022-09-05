# My hashtable array with 6 buckets.
hashTable = [None, None, None, None, None, None]

###################################################
# TASK ONE
# Comment the code below so that:
#
# For methods hashFunction, CHAdd, increment, LPAdd:
#   1. What are the inputs.
#   2. What is the output (if there is one).
#   3. Do the values of any global variables change (in this case, hashTable).
#   4. What is the method doing?
#
# For each If statement:
#   1. What is the condition being checked?
#   2. What happens if the condition is True.
#   3. What happens if the condition is False.
#
# For each While Loop
#   1. What is the condition of the while loop.
#   2. When does the condition become false/when do we stop looping.
#
#
# TASK TWO:
# Read the comments and write code for the methods: CHSearch, CHDelete, LPSearch, LPDelete.
###################################################

def hashFunction(n):
  return len(n) % len(hashTable)

def CHAdd(element):
  x = hashFunction(element)
  if hashTable[x] == None:	#if there is None in the index position of the result of modulo
    hashTable[x] = [element] # hash table's modulo index is equal to the element
  else:# if not creates a chain for the index value
    hashTable[x].append(element)
  return True

def increment(n):
  n = n + 1
  if n >= len(hashTable): # if the length of the hashtable is les or equal to the n
    return 0 # it returns 0
  else: 
    return n #if not returns the n

def LPAdd(element):
  x = hashFunction(element)
  if hashTable[x] == None or "REMOVED": #if the result of the modulo index position of the hash table is None
    hashTable[x] = element #hash table's result of modulo calculation's index is equal to the element
  else:
    y = increment(x) # y is equal to the incrementation of the value of modulo function
    while y != x: # while the incrementing value is not equal to the result of modulo
      if hashTable[y] == None or "REMOVED": # if there is nothing in the location of the incremented value
        hashTable[y] = element # that index value is equal to the element
        return True
      else: # if the value isnt None
        y = increment(y) # Y is called again with incremented value
    return False

# Takes in an input 'element', and returns True if that element is in the hashtable and false if not. It does not change the state of the array hashtable. The method uses the hash function to search through the list in the hash table for the element.
def CHSearch(element):
  for y1 in range(0,len(hashTable)):
    if hashTable[y1] != None:
      if element in hashTable[y1]:
        return True
  return False

# Takes in an input 'element', and returns True if that element is removed from the hashtable and false if the element is not in the hash table and therefore cannot be removed. It changes the hashtable so that the input element is no longer contained but all other elements remain. The method uses the hash function and searches through the appropriate list and removes the element from the list if it finds it.
def CHDelete(element):
  for y1 in range(0,len(hashTable)):
    if hashTable[y1] != None:
      for x1 in range(0,len(hashTable[y1])):
        if element == hashTable[y1][x1]:
          hashTable[y1].remove(element)
          return True
  return False

# Takes in an input 'element', and returns True if that element is in the hashtable and false if not. It does not change the state of the array hashtable. The method uses the hash function to search through the hash table for either the element or the first instance of None.
def LPSearch(element):
  for y2 in range(0,len(hashTable)):
    if hashTable[y2] != None and "REMOVED":
      if hashTable[y2] == element:
        return True
  return False

# Takes in an input 'element', and returns True if that element is removed from the hashtable and false if the element is not in the hash table and therefore cannot be removed. It changes the hashtable so that the input element is no longer contained but all other elements remain. The method uses the hash function to search through the hash table for either the element or the first instance of None. If it finds the element, it replaces it with a string "REMOVED" to indicate it has been removed.
def LPDelete(element):
  for y3 in range(0,len(hashTable)):
    if hashTable[y3] != None and "REMOVED":
      if hashTable[y3] == element:
        hashTable[y3] = "REMOVED"
        return True
  return False

CHAdd("Pizza")
CHAdd("Burger")
CHAdd("Shake")
CHAdd("Cola")
print(CHSearch("Pizza"))
print(CHDelete("Pizza"))
#CHSearch("Burger") Should return True
#CHSearch("Chips") Should return False

#CHDelete("Cola")

print(hashTable)

hashTable = [None, None, None, None, None, None]

LPAdd("TEST")
LPAdd("TEST1")
LPAdd("TEST2")
print(LPSearch("TEST"))
LPDelete("TEST")
print(hashTable)