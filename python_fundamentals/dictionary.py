aboutMe = {"name": "Ryan", "age": 31, "country": "USA", "language": "Python"}

def listDictionary(inDict):
	print "My name is {}.".format(inDict["name"])
	print "My age is {}.".format(inDict["age"])
	print "My country of birth is {}.".format(inDict["country"])
	print "My favorite language is {}.".format(inDict["language"])

listDictionary(aboutMe)
