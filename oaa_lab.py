import re
name = []
argument = {}
def filter(str):
	"""Create"""
	words = re.findall(r'\S+', str)
	if(re.search(r'[cC][rR][eE][aA][tT][eE]',words[0])):
		if(re.search(r'[a-zA-Z_]',words[1]) and not(words[1] in name)):
			name.append(words[1])
			argument.update({words[1]: []})
			print(argument)
		else: print("incorrect name")
	else:
		print("invalid syntax")

	"""Insert"""
	if(re.search(r'[iI][nN][sS][eE][rR][tT]',words[0])):
		if(words[1] in name):
			argument.get(words[1]).append(str.split('[', 1)[1].split(']')[0].replace(',', ' ').split())
			print(argument)
	if(re.search(r'[cC][oO][nN][tT][aA][iI][nN][sS]',words[0])):
		if(words[1] in argument):
			k = argument.get(words[1])
			for i in k:
				if(i == str.split('[', 1)[1].split(']')[0].replace(',', ' ').split()):
					print("True")
				else:
					print("False")

while True:
    str = input('--> ')
    for command in str.split(';'):
    	if command:
            filter(command)
