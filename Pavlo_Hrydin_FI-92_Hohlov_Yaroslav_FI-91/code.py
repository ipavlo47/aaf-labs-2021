from func import *
import re
import math
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
				arg = [int(arg[0]), int(arg[1])]
				argument[words[1]] = Node(arg)
			else:
				arg = [int(arg[0]), int(arg[1])]
				argument[words[1]].insert(arg)

		else: print("segment entered incorrectly")
	else: print("Incorrect name")

def Contains_tree(words):
	if(words[1] in name_tree):
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		arg = [int(arg[0]), int(arg[1])]
		argument[words[1]].Contains(arg)


def Search_tree(words):

	if(words[1] in name_tree):
		if(len(words) > 2):
			if(re.search(r'(?i)where', words[2])):
				if(re.search(r'(?i)contains_by',words[3])):
					arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
					arg = [int(arg[0]), int(arg[1])]
					argument[words[1]].Search(arg)
				elif(re.search(r'(?i)intersects', words[3])):
					arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
					arg = [int(arg[0]), int(arg[1])]
					argument[words[1]].Intersects(arg)
				elif(re.search(r'(?i)right_of', words[3])):
					if(re.search(r'[0-9]',words[4])):
						print(words[4])
						argument[words[1]].Search([int(words[4]), 100000])
			else: print("WHERE is error")
		else: argument[words[1]].Search([-100000, 100000])

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
		Contains_tree(words)
	elif(re.search(r'(?i)search',words[0])):
		Search_tree(words)
	elif(re.search(r'(?i)print',words[0])):
		Print(words)
	else:
		print("Incorrect command")

while True:
    str = input('--> ')
    for command in str.split(';'):
    	if command:
            filter(command)
