for i in range(1, 1000, 2): # selects odds from 1 to 1000
	print i

for i in range(5, 1000000, 5): # selects multiples of 5 from 5 to 1,000,000
	print i

a = [1, 2, 5, 10, 255, 3]

total = 0   		#initializes total as 0, then adds each element to the running total
for i in a:
	total += i
print total

total_new = 0   	#starts a new total at 0, this time to get the total and take an average
for i in a:
	total_new += i
avg = total_new / len(a)   	#calculates the average
print avg
