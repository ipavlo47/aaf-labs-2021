from func import *
import re
name_tree = []
argument = {}

def Create(words):
	if not(words[1] in name_tree):
		if(re.search(r'[a-zA-Z]',words[1])):
			create_tree(argument, words[1])
			name_tree.append(words[1])
			print("Set", words[1], "has been created")
		else: print("Incorrect name")
	else: print("This name has been created")

def Insert(words):
	if(words[1] in name_tree):
		# argument.get(words[1]).append(str.split('[', 1)[1].split(']')[0].replace(',', ' ').split())
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		insert_data_to_tree(argument, words[1], arg[0], arg[1])
		print("Range [" + arg[0]+ ',', arg[1] + "] has been added to " + words[1] + '.' )
	else: print("Incorrect name")

def Contains(words):
	if(words[1] in name_tree):
		k = argument.get(words[1])[1:]
		arg = str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()
		for i in k:
			if((i[0] == arg[0]) and (i[1] == arg[1])):
				print("True")
			else: print("False")

def Search(words):
	answer = []
	if(words[1] in name_tree):
		arr = argument[words[1]][1:]
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
		pp.pprint(argument[words[1]][0])
		print(words[1])
		# pp.pprint(tree_list.get(words[1])[0])
		# print(print_tree(tree_list.get(words[1])[1:]))
		# print(print_tree(tree_list.get(words[1])[1:]))
		# contains_tree(argument, words[1])
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
