### A Bananagrams Assistant by Edargorter (Zachary Bowditch) (2017) ###
###    
###     Word list: words_alpha.txt (84095 words)
###     (https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt)
###
#################################################################


from sys import argv
import os

def get_alphabet_letters():
	return [chr(97 + i) for i in range(26)]

current_letters = ""
present_words = []
strings = [""]
used_words = []
title = open("title.txt", "r").read()

def print_title():
	print(title)

def help():
	print("\nHelp: help")
	print("Quit: q")
	print("Take back word: b")
	print("Use word: [word number]")
	print("New letter selection: new [ letters ]");
	print("List available words: ls")
	print("Clear screen: cls")
	print("Add letters: add [letter string]")
	print("Remove letters: rm [letter string]")
	print("Reset to current letter string: reset")
	print("Show current string: curr\n")

def remove_letters(letter_string):
	for letter in letter_string:
		for i in range(len(strings)):
			try:
				index = strings[i].index(letter)
				strings[i]  = strings[i][:index] + strings[i][index + 1:]
			except Exception:
				print("'" + letter + "' not in letter string")
				break	

def add_letters(letter_string):
	for i in range(len(strings)):
		strings[i] += letter_string

def use_word(word):
	used_words.append(word)
	new_string = ""
	letter_string = strings[-1]
	for i in range(len(letter_string)):
		if letter_string[i] in word:
			index = word.index(letter_string[i])
			word = word[:index] + word[index + 1:]
		else:
			new_string += letter_string[i]
	strings.append(new_string)

def remove_word():
	if len(used_words) == 0:
		return
	strings.pop(-1)
	used_words.pop(-1)
	present_words.pop(-1)

def get_used_words():
	words = "[ "
	for word in used_words:
		words += word + " "
	return words + "] " 

def find_word(letter_string, new_list = True):
	index = 0
	if new_list:
		present_words.append([])
	using = list(letter_string)
	letters = list(letter_string)
	alphabet_letters = get_alphabet_letters()
	while index < len(alphabet_letters):
		if alphabet_letters[index] not in letters:
			alphabet_letters.pop(index)
		else:
			index += 1
	count = 0
	for letter in alphabet_letters:
		word_sublist = open(letter + ".txt", "r").readlines()
		word_sublist = [word.rstrip() for word in word_sublist]
		for i in range(len(word_sublist)):
			word = word_sublist[i]
			word_is_in = True
			using = list(letter_string)
			if len(word) == 1:
				continue
			for word_letter in word:
				if word_letter not in using: 
					word_is_in = False
					break
				using[using.index(word_letter)] = "0"

			if word_is_in:
				present_words[-1].append(word)
				count += 1
	present_words[-1].sort(key=len)

def get_links():
	present_words.append([])
	for letter in used_words[-1]:
		find_word(strings[-1] + letter, False)
	present_words[-1] = list(set(present_words[-1]))	
	present_words[-1].sort(key=len)

def list_words():
	if len(present_words) == 0:
		return
	for i in range(len(present_words[-1])):
		print(str(i) + " " + present_words[-1][i] + " (" + str(len(present_words[-1][i])) + ")")

def new_session(new_string):
	global strings
	global used_words
	global present_words
	strings = [new_string]
	used_words = []
	present_words = []
	find_word(new_string)

def get_strings():
	if len(strings) == 0:
		return ""
	return strings[-1]

if len(argv) > 1:
	letters = argv[1]
	strings[-1] += letters
	find_word(letters)

print_title()
while 1:
	inp = input(get_strings() + " " + get_used_words() + "Command: ")
	inp = inp.split(" ")
	if len(inp[0]) == 0:
		continue
	if inp[0][0] == "q":
		break
	if inp[0][0] == "h":
		help()
	elif inp[0] == "ls":
		list_words()
	elif inp[0] == "cls":
		os.system("clear")
	elif inp[0] == "add" and len(inp) > 1:
		if len(inp[1]) == 0:
			print("\nPlease include letter string.\n")
		else:
			add_letters(inp[1])
		print("use 'reset' to find words in new letter string.")
	elif inp[0] == "rm" and len(inp) > 1:
		if len(inp[1]) == 0:
			print("\nPlease include letter string.\n")
		else:
			remove_letters(inp[1])
		print("use 'reset' to find words in new letter string.")
	elif inp[0] == "reset":
		new_session(strings[0])
	elif inp[0] == "curr":
		print("\n" + strings[0] + "\n")
	elif inp[0] == "htop":
		os.system("htop")
	elif inp[0].isdigit():
		index = int(inp[0])
		if index >= 0 and index < len(present_words[-1]):
			print(present_words[-1][index])
			use_word(present_words[-1][index])
			get_links()
		else:
			print("\nIndex out of range.\n")
	elif inp[0] == "b":
		remove_word()
	elif inp[0] == "title":
		print_title()	
	elif inp[0] == "new" and len(inp) > 1:
		if len(inp[1]) == 0:
			print("\nPlease include letter string.\n")
		else:
			new_session(inp[1])
	else:
		print("Invalid command.")
