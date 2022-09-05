import random

def test(score):
  num1 = random.randint(1,20)
  num2 = random.randint(1,20)
  op = random.randint(0,3)
  operation=['add','sub','div','mul']
  if operation[op] == 'add':
    ans = num1 + num2
    print("What is the sum of",num1,'and',num2)
    inp = input('Answer: ')
  if operation[op] == 'sub':
    ans = num1 - num2
    print("What is the result of",num1,'-',num2)
    inp = input('Answer: ')
  if operation[op] == 'div':
    ans = round((num1 / num2),2)
    print("What is the answer of",num1,'divided by',num2,'in 2 decimal places')
    inp = input('Answer: ')
  if operation[op] == 'mul':
    ans = num1 * num2
    print("What is the multiplication of",num1,'and',num2)
    inp = input('Answer: ')

  if inp != '':
    if float(inp) == ans:
      score += 1
      print("Correct")
      return 1
    else:
      print('Correct answer was',ans)
      return 0
  else:
    return 0

score = 0
for x in range(0,10):
  score = score + test(score)

print("Your score is:",score)