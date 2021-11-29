from func import *
import re
name_tree = []
argument = {}

def Create(words):
	if not(words[1] in name_tree):
		if(re.search(r'[a-zA-Z]',words[1])):
			argument[words[1]] = []
			name_tree.append(words[1])
			print("Set", words[1], "has been created")
		else: print("Incorrect name")
	else: print("This name has been created")

def Insert(words):
	if(words[1] in name_tree):
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		if (int(arg[0]) <= int(arg[1])):
			if (argument[words[1]] == []):
				argument[words[1]] = Node(arg + [0])
			else:
				argument[words[1]].insert(arg)
			print("Range [" + arg[0]+ ',', arg[1] + "] has been added to " + words[1] + '.' )
		else: print("segment entered incorrectly")
	else: print("Incorrect name")

def Contains(words):
	if(words[1] in name_tree):
		k = argument[words[1]].get_list()
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		for i in k:
			if((i[0] == arg[0]) and (i[1] == arg[1])):
				print("True")


def Search(words):
	answer = []
	if(words[1] in name_tree):
		arr = argument[words[1]].get_list()
		for i in range(len(arr)):
			for j in range(2):
				arr[i][j] = int(arr[i][j])
		if(len(words) > 2):
			if(re.search(r'(?i)where', words[2])):
				if(re.search(r'(?i)contains_by',words[3])):
					arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
					for i in range(2):
						arg[i] = int(arg[i])
					for k in range(len(arr)):
						if((arg[0] <= arr[k][0]) and (arr[k][1] <= arg[1])):
							answer.append(arr[k])
				elif(re.search(r'(?i)intersects', words[3])):
					arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
					for i in range(2):
						arg[i] = int(arg[i])
					for k in range(len(arr)):
						if(((arg[0] <= arr[k][1]) and (arr[k][1] <= arg[1])) or ((arg[0] <= arr[k][0]) and(arr[k][0] <= arg[1]))):
							answer.append(arr[k])
				elif(re.search(r'(?i)right_of', words[3])):
					if(re.search(r'[0-9]',words[4])):
						a = int(words[4])
						for k in range(len(arr)):
							if((a <= arr[k][0]) and (a <= arr[k][1])):
								answer.append(arr[k])
				print(answer)
			else: print("WHERE is error")
		else: print(arr)

def Print(words):
	if(words[1] in name_tree):
		if (argument[words[1]] != []):
			argument[words[1]].PrintTree()
		else:
			print("<None inside>")
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
		print("Incorrect command")

while True:
    str = input('--> ')
    for command in str.split(';'):
    	if command:
            filter(command)
