class Major():
	def _init_(self, name, school, assist_code):
		self.name = name
		self.school = school
		self.assist_code = assist_code
		self.classes_required = []
	
	def add_required_classes(classes):
		self.classes_required += classes
