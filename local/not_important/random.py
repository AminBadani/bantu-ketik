import os, re, threading;
from modular import open_txt_different_python_file;

# this is wrong, only for testing variable mutation
# test_result - sat, 22 feb (8:34 pm) = variable mutation does not works when called as a parameter(?)
# better to call the function inside the variable
# WORDS = [];

# problem = txt file does not exists when being run of different directory
WORDS = open_txt_different_python_file('dataset_eng.txt');

# check and return all words that have substring
# https://en.wikipedia.org/wiki/Substring
# Math String algorithm
def match_substring():
	is_repeat = True;
	while is_repeat: 
		user_input = input('Write a single word: ');
		pattern = re.compile(user_input);
		words_by_pattern = [item for item in WORDS if user_input in item];
		# words_by_pattern = [item for item in WORDS if pattern.match(item)];

		for word in words_by_pattern:
			print(word)

		if (input('Repeat? (y/n) ') == 'n' ): break
		os.system('clear');

# check if a word is anagram with another word
# https://wl.vern.cc/wiki/Anagram?lang=en 
def is_anagram(word1, word2):
	print(sorted(word1), sorted(word2));
	return sorted(word1) == sorted(word2);

# split string to an array and compare every splitted string
def split_compare_string(input_str: str):
	# split the string to become words
	splitted_string = input_str.split(' ')
	print(splitted_string)

	# compare every words in splitted string one by one with words from dataset
	for input_word in splitted_string:
		# loop every words in dataset
		for suggested_word in WORDS:
			if (sorted(input_word) == sorted(suggested_word)):
				print('Do you mean ' + input_word + ' with "' + suggested_word + '"')


	return str

# open txt file and store it on a variable
def open_txt(file_name: str, stored_var: str = ''):
	# stored_var = '';
	with open(file_name, 'r') as file:
		stored_var = file.read().replace('\n', ' ').split(' ')
	print(stored_var)
	return stored_var

# for random test
def test_func():
	# myvar = input('Write your string: ');
	# threading.Timer(1.0, my_function).start();
	print('hello');
	# print(myvar + ' world');
	# os.system('clear')


# split_compare_string('holle world my nmea is amin')
# open_txt('dataset_eng.txt')