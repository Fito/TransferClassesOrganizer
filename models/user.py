schools = {
	"Laney" 								: "LANEY",
	"Berkeley City College" : "BERKELEY",
	"Alameda"								: "ALAMEDA",
	"Diablo Valley College" : "DIABLO"
}

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


class User():
	def __init__(self):
		self.current_schools = []
		self.current_schools_codes = []
		self.majors = []
		self.classes_taken = {}

	def add_current_school(self, school):
		self.current_schools.append(school)
		self.current_schools_codes.append(schools[school])
	
	def has_current_school(self):
		return (len(self.current_schools) > 0)
	
	def add_major(self, major_object):
		self.majors.append(major_object)
	
	def has_majors(self):
		return (len(self.majors) > 0)
	
	def add_class_taken(self, school, course):
		if school in self.classes_taken and len(self.classes_taken[school]):
			self.classes_taken[school].append(course)
		else:
			self.classes_taken[school] = [course]
	
	def remove_class_taken(self, course):
		for school in self.classes_taken.keys():
			self.classes_taken[school] = remove_values_from_list(self.classes_taken[school], course)
			
	def courses_taken(self, school_or_code):
		#school code provided
		if school_or_code in self.current_schools_codes:
			for school in self.current_schools:
				if schools[school] == school_or_code and (school in self.classes_taken.keys()):
					return self.classes_taken[school]
				else:
					return []
		#school name provided		
		elif school_or_code in self.classes_taken:
			return self.classes_taken[school_or_code]
		else:
			return []