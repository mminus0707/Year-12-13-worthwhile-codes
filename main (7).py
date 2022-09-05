def spellnum(num):
  GRAPH = {
            '4' : ['one', 'two', 'three','four','five','six','seven','eight','nine'], 
            '3' : ['#', 'twenty', 'thrity','forty','fifty','sixty','seventy','eighty','ninty'],
            '2' : ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred'], 
            '1' : ['one thousand', 'two thousand', 'three thousand', 'four thousand', 'five thousand', 'six thousand', 'seven thousand', 'eight thousand', 'nine thousand']
            }
  TEEN = ['ten','eleven', 'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  numspell = ""
  if num == 0:
    numspell = 'zero'
  while len(str(num)) < 4:
    num = str(num)
    num = '0' + num
  num = str(num)
  teen = False
  for x in range(0,len(num)):
    if num[x] != '0' and teen == False:
      numspell = numspell + GRAPH[str(x+1)][int(num[x])-1] + " "
    if teen == False and num[len(num)-2] == '1' and x == len(num)-3:
      teen = True
      numspell = numspell + TEEN[int(num[len(num)-1])] + " "
  print(numspell)

spellnum(578)