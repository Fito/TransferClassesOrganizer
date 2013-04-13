majors = {
	"Electrical Engineering and Computer Science" : "EECS",
	"Biochemical Engineering"                    : "ENG.CHEM.BIO.B.S."
}

universities = {
	"UC Berkeley" : "UCB",
	"UC Davis"    : "UCD"
}

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


