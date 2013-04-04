class User():
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.current_schools = []
		self.majors = []
		self.classes_taken = []

	def add_current_school(self, school):
		self.current_schools.append(school)
	
	def add_desired_major(self, major_object):
		self.majors.append(major_object)
	
	def change_password(self, old_password, new_password):
		if self.password == old_password:
			self.password = new_password
		else:
			print('Wrong password.')
	
	