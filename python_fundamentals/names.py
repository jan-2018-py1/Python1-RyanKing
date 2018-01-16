def listStudents(students):
	for i in students:
		print i["first_name"], i["last_name"]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# listStudents(students)

def listStudents2(students):
	for key, group in students.items():
		print key
		idx = 1
		for i in group:
			name = i["first_name"] + " " + i["last_name"]
			print "{} - {} - {}".format(idx, name, len(name) - 1)
			idx += 1

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

listStudents2(users)
