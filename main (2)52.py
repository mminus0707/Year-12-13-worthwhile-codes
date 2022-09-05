complexity = 0
linear = 0

def findSplit(list_,first,last):
  global complexity
  global linear
  complexity += 1
  pivot = list_[first]
  leftMark = first+1 
  rightMark = last
  listSorted = False
  while listSorted == False:
    while leftMark <= rightMark and list_[leftMark] <= pivot:
      leftMark += 1
      linear += 1
    while list_[rightMark] >= pivot and rightMark >= leftMark:
      rightMark -= 1
      linear +=1

    print(rightMark)
    print(leftMark)

    if rightMark < leftMark:
      listSorted = True
    else:
      temp = list_[leftMark]
      list_[leftMark] = list_[rightMark]
      list_[rightMark] = temp
    temp=list_[first]
    list_[first] = list_[rightMark]
    list_[rightMark] = temp
    return(rightMark)

def quickSort(list_,first,last):
  if first < last:
    split = findSplit(list_,first,last)
    quickSort(list_,first,split-1)
    quickSort(list_,split+1,last)
  print(list_)

arr=[4,4,6,8,5,3,97,108,3,2,56]
arr_=[3,2,1,6,5,4,9,8,7]
quickSort(arr,0,len(arr)-1)
print("n x log(n):",linear * complexity)