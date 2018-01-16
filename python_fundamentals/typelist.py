def typeList(inputList):
	isString = False
	isNum = False
	returnString = ""
	returnInt = 0
	listType = ""

	for i in inputList:
		if isinstance(i, str):
			isString = True
			returnString = returnString + i + ' '
		elif isinstance(i, int) or isinstance(i, float):
			isNum = True
			returnInt += i

	if isString:
		if isNum:
			listType = "mixed"
		else: listType = "string"
	elif isNum:
		listType = "integer"
	else:
		listType = "empty"

	print "The list you entered is of {} type.".format(listType)
	if isString:
		print "String: {}".format(returnString)
	if isNum:
		print "Sum: {}".format(returnInt)

l = ['magical unicorns',19,'hello',98.98,'world']

typeList(l)
typeList([4, 5, 37])
