import re
name = []
argument = {}

def Create(words):
	if not(words[1] in name):
		if(re.search(r'[a-zA-Z]',words[1])):
			name.append(words[1])
			argument.update({words[1]: []})
			print("Set", words[1], "has been created")
			print(argument)
		else: print("incorrect name")
	else: print("this name has been created")


def Insert(words):
	if(words[1] in name):
		argument.get(words[1]).append(str.split('[', 1)[1].split(']')[0].replace(',', ' ').split())
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		print("Range [" + arg[0]+ ',', arg[1] + "] has been added to set_name.")
		print(argument)

def Contains(words):
	if(words[1] in argument):
		k = argument.get(words[1])
		for i in k:
			if(i == str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()):
				print("True")
			else: print("False")

def Search(words):
	limit = []
	answ = []
	# limit.append(str.split('[', 1)[1].split(']')[0].replace(',', ' ').split())
	k = argument.get(words[1])
	for i in k:
		print(k[i])
	if(words[1] in argument):
		if(len(words) > 2):
			if(re.search(r'(?i)where', words[2])):
				if(re.search(r'(?i)contains_by',words[3])):
					print("cont")
				elif(re.search(r'(?i)intersects', words[3])):
					print("inter")
				elif(re.search(r'(?i)right_of', words[3])):
					print('right')
				else: print("WHERE is error")
		else: print(argument.get(words[1])[0][0])
		print(answ)
def Print(words):
	if(words[1] in argument):
		print(argument.get(words[1]))
	else: print("Haven't this tree")


def filter(str):
	"""Create"""
	words = re.findall(r'\S+', str)
	if(re.search(r'(?i)create',words[0])):
		Create(words)
	elif(re.search(r'(?i)insert',words[0])):
		Insert(words)
	elif(re.search(r'(?i)contains',words[0])):
		Contains(words)
	elif(re.search(r'(?i)search',words[0])):
		Search(words)
	elif(re.search(r'(?i)print',words[0])):
		Print(words)
	else:
		print("incorrect command")

while True:
    str = input('--> ')
    for command in str.split(';'):
    	if command:
            filter(command)
