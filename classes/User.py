class User():
	def _init_(self, name, password):
		self.name = name
		self.password = password
		self.current_schools = []
		self.majors = []
		self.classes_taken = []

	def add_current_schools(self, school):
		self.current_schools.append(school)
	
	def add_desired_major(self, major, desired_school):
		self.majors.append(major + '-' + desired_school)
	
	def change_password(self, old_password, new_password):
		if self.password == old_password:
			self.password = new_password
		else:
			print('Wrong password.')
	
	