def oddEven():
	isEven = ""
	for i in range(1, 2001):
		if i % 2 == 0:
			isEven = "even"
		else:
			isEven = "odd"
		print "Number is {}. This is an {} number.".format(i, isEven)
# oddEven()

def multiply(inList, val):
	outList = []
	for i in inList:
		outList.append(i * val)
	return outList

# listA = [2, 3, 4]
# listB = multiply(listA, 5)
# print listB

def layered_multiples(arr):
	new_array = []
	for i in arr:
		ones_array = []
		for j in range(0,i):
			ones_array.append(1)
		new_array.append(ones_array)
	return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
