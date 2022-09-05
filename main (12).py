def dictionarycompression(sentence,compressed):
  sentence += " "
  save = 0 
  newthis = []
  dictionary = []
  #creating the dictionary
  for x in range(0,len(sentence)):
    if sentence[x] == " " or x == len(sentence):
      slic = slice(save,x)
      newthis.append(sentence[slic])
      save = x + 1
  for y in range(0,len(newthis)):
    count = 0
    for z in range(0,len(newthis)):
      if newthis[y] == newthis[z]:
        count += 1
    if count > 1:
      if newthis[y] not in dictionary:
        dictionary.append(newthis[y])
  #compressing the sentence
  for y in range(0,len(newthis)):
    for z in range(0,len(dictionary)):
      if newthis[y] == dictionary[z]:
        compressed += str(z)
      if newthis[y] not in dictionary and newthis[y] not in compressed:
        compressed += newthis[y]
    if len(dictionary) == 0:
      for h in range(0,len(newthis)):
        compressed += newthis[h]
  extraction = input("Do you want to extract your dictionary? y/n ")
  if extraction.lower() == "y":
    o = open("Dictionary_for_Compression.txt", "a")
    for u in range(0,len(dictionary)):
      o.write(dictionary[u])
      o.write("\n")
    o.close()
  return(compressed)

def dictionarydecompression(text,dictionary):
  num = ["0","1","2","3","4","5","6","7","8","9"]
  decompressed = ""
  for x in range(0,len(text)):
    if text[x] not in dictionary and text[x] not in num:
      decompressed += text[x]
    for y in range(0,len(dictionary)):
      if text[x] == num[y]:
        decompressed += " " + dictionary[y]       
  print(decompressed)
  extraction = input("Do you want to extract your decompressed file? y/# ")
  if extraction.lower() == "y":
    o = open("Decompressed.txt", "a")
    o.write(decompressed)
    o.close()
  
def rlecompression(text):
  text += " "
  compressed = ""
  count = 0
  this = text[0]
  for x in range(0,len(text)):
    if text[x] == this:
      count += 1
    else:
      compressed += str(count)
      compressed += text[x-1]   
      this = text[x]
      count = 1
  return(compressed)   

def rledecompression(text):
	num = ["1","2","3","4","5","6","7","8","9","0"]
	decompressed = ""
	for x in range(0,len(text)):
		if text[x] in num:
			if text[x+1] in num:
				this = ""
				this += text[x]
				this += text[x+1]
				for y in range(0,int(this)):
					decompressed += text[x+2]
			else:
				for y in range(0,int(text[x])):
					decompressed += text[x+1]
	print(decompressed)

def cdict(sentence):
  newthis = []
  dictionary = []
  save = 0
  for x in range(0,len(sentence)):
    if sentence[x] == " " or x == len(sentence)-1:
      slic = slice(save,x)
      newthis.append(sentence[slic])
      save = x + 1
  for y in range(0,len(newthis)):
    count = 0
    for z in range(0,len(newthis)):
      if newthis[y] == newthis[z]:
        count += 1
    if count > 1:
      if newthis[y] not in dictionary:
        dictionary.append(newthis[y])
  total = 0
  for i in range(0,len(dictionary)):
    for o in range(0,len(dictionary[i])):
      total += 1
  return total

def menu():
	global run
	option = input("""
	What would you like to do ?

	1. Dictionary Compression
	2. Dictionary Decompression
	3. Run Length Encoding Compression
	4. Run Length Encoding Decompression
	5. Find the most optimal compression type
	To exit press 0

	""")

	if option == "1":
		text = input("Enter your text: ")
		file = ""
		print(dictionarycompression(text,file))
	if option == "2":
		dictionar = []
		print("Dictionary decompression can only support up to 10 words")
		text = input("Enter your compressed text: ")
		words = 1
		print("Creating Dictionary, enter 0 to stop")
		while words != "0":
			words = input("Enter your words: ")
			dictionar.append(words)
		else:
			dictionarydecompression(text,dictionar)
	if option == "3":
		text = input("Enter your text: ")
		print(rlecompression(text))
	if option == "4":
		print("RLE Decompression can only support up to 99 characters")
		text = input("Enter your compressed text: ")
		rledecompression(text)
	if option == "5":
		file = ""
		text = input("Enter your text: ")
		diction2 = len(dictionarycompression(text,file)) + cdict(text)
		rle2 = len(rlecompression(text))
		if len(dictionarycompression(text,file)) + cdict(text) < len(rlecompression(text)):
			print("Dictionary compression is the most optimal compression", diction2, "is the number of bytes required with dictionary compression where run length requires",rle2)
			print(dictionarycompression(text,file))
		else:
			print("Run Length Encoding Compression is the most optimal compression", rle2, "is the number of bytes required with run length compression where dictionary compression requires",diction2)
			print(rlecompression(text))
	if option == 0:
		run = False
	else:
		print("Please choose one of the options")

run = True

while run == True:
	menu()
else:
	exit()