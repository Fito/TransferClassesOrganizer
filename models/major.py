majors = {
	"Electical Engineering and Computer Science" : "EECS",
	"Biochemical Engineering"                    : "ENG.CHEM.BIO.B.S."
}

universities = {
	"UC Berkeley" : "UCB",
	"UC Davis"    : "UCD"
}

class Major():
	def __init__(self, name, school, assist_code, school_code):
		self.name = name
		self.school = school
		self.assist_code = assist_code
		self.classes_required = []
		self.school_code = school_code
	
	def add_required_classes(classes):
		self.classes_required += classes

