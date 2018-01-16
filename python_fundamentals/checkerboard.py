for i in range(8):
	row = ""
	for j in range(8):
		if (i + j) % 2 == 0:
			row += "*"
		else:
			row += " "
	print row
