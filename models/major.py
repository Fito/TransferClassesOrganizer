majors = {
	"Electrical Engineering and Computer Science" : "EECS",
	"Biochemical Engineering"                    	: "ENG.CHEM.BIO.B.S."
}

universities = {
	"UC Berkeley" : "UCB",
	"UC Davis"    : "UCD"
}

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

class Major():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.code = majors[name]
		self.school_code = universities[school]
		self.courses_required = {}
	
	def add_required_courses(self, transfer_from, courses_groups):
		courses = []
		for group in courses_groups:
			if len(group['courses']):
				courses.append({ group['title'] : group['courses'] })
		self.courses_required[transfer_from] = courses
	
	def courses_required_from(self, school):
		if school in self.courses_required:
			return self.courses_required[school]
		else:
			return []
	
			






