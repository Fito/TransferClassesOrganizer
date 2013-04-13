schools = {
	"Laney" 								: "LANEY",
	"Berkeley City College" : "BERKELEY",
	"Alameda"								: "ALAMEDA",
	"Diablo Valley College" : "DIABLO"
}

class User():
	def __init__(self):
		self.current_schools = []
		self.majors = []
		self.classes_taken = []

	def add_current_school(self, school):
		self.current_schools.append(schools[school])
	
	def add_major(self, major_object):
		self.majors.append(major_object)
	
	