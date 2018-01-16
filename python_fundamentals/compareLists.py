def compareLists(list1, list2):
	compare = True

	if len(list1) != len(list2):
		compare = False
	else:
		for idx, item in enumerate(list1):
			if item != list2[idx]:
				compare = False

	if compare:
		print "The lists are the same."
	else:
		print "The lists are not the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareLists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareLists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareLists(list_one, list_two)
