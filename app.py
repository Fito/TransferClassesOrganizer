try: 
	from Tkinter import *
except ImportError:
	# probably using python 3
	from tkinter import *

import models
import lib
import views

major = models.Major('Electrical Engineering and Computer Science', 'UC Davis', 'ENG.CHEM.BIO.B.S.', 'UCD')
user = models.User('Fito', '123')
user.add_current_school('LANEY')
user.add_desired_major(major)


# ninja = lib.AssistNinja()
# ninja.fetch_report(user.current_schools[0], user.majors[0].school_code, user.majors[0].assist_code, '12-13')
# ninja.extract_report_data()
# courses = ninja.courses_for(user.majors[0].assist_code, user.majors[0].school_code)
# print(courses)
# class App():
# 	def __init__(self, master):
# 		frame = Frame(master)
# 		frame.pack()
# 		self.label(frame)
# 
# main_window = Tk()
# app = App(main_window)
# 
# main_window.mainloop()