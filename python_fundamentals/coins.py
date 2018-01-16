import random

print "Starting the program..."
totHeads = 0
totTails = 0

for i in range(1, 5001):
	coin = round(random.random())
	if coin == 0:
		side = "heads"
		totHeads += 1
	else:
		side = "tails"
		totTails += 1
	print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far.".format(i, side, totHeads, totTails)

print "Ending the program. Thank you!"
