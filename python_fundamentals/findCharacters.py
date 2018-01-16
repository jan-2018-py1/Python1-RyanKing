def findCharacters(word_list, char):
	new_list = []
	for word in word_list:
		if char in word:
			new_list.append(word)

	print new_list

test_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
findCharacters(test_list, 'o')
