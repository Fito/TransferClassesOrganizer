import json
from models.user import *
from models.major import *

class Storage():
	def __init__(self, file_name):
		self.file = file_name
	
	def encode_object(self, obj):
		if isinstance(obj, User):			
			return {'__user__'			 				: True, 
							'current_schools'				: obj.current_schools,
							'current_schools_codes' : obj.current_schools_codes,
							'majors'							 	: obj.majors,
							'classes_taken'				  : obj.classes_taken}
		elif isinstance(obj, Major):
			return {"__major__"					: True, 
							"name"						  : obj.name,					
							"school"					  : obj.school, 					
							"code" 							: obj.code,					
							"school_code"		    : obj.school_code,		
							"courses_required"  : obj.courses_required}
		raise TypeError(repr(obj) + " is not JSON serializable")
	
	def as_user(self, dct):
		if '__user__' in dct:
			user = User()
			user.current_schools = dct['current_schools']
			user.curret_schools_codes = dct['current_schools_codes']
			majors = dct['majors']
			user.majors = []		
			for major in majors:
				if '__major__' in major:
					m = Major(major["name"], major["school"])
					m.code = major['code']
					m.school_code = major['school_code']
					m.courses_required = major['courses_required']				
				user.majors.append(m)
			user.classes_taken = dct['classes_taken']
			return user
		return dct
	
	def store(self, obj):
		f = open('user_info.json', "w")
		json.dump(obj, f, default=self.encode_object)
		f.close()		

	def build_from_file(self, obj):
		f = open('user_info.json')
		if isinstance(obj, User):
			return json.load(f, object_hook=self.as_user)
		f.close()		
	
	
user = User()
user.current_schools = ['A', 'B']
major = Major("Biochemical Engineering", "UC Davis")
user.majors = [major]

storage = Storage('user_info.json')
storage.store(user)
# storage.store(major)
user = storage.build_from_file(User())
print user.majors[0].school