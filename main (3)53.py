def bsort(arr):
  low = 0
  great = 1
  swap = 0
  pass1 = 0
  while swap != 0 and pass1 > 0:

    if arr[low] > arr[great]:
      replace = arr[great]
      arr[great] = arr[low]
      arr[low] = replace
      swap += 1
    low += 1
    great += 1