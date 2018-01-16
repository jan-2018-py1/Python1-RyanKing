def draw_stars(arr):
	for i in arr:
		if isinstance(i, int):
			row = ""
			for j in range(0,i):
				row += "*"
			print row
		elif isinstance(i, str):
			row = ""
			ltr = i[0].lower()
			for j in range(0, len(i)):
				row += ltr
			print row
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
