try: 
	# default python should be 3
	from tkinter import *
except ImportError:
	# most likely triggered by using python 2.7
	from Tkinter import *

import time
from models.major import *
from models.user import *
from lib.assist_ninja import *
from views.gui import *

ninja = AssistNinja()
user = User()

root = Tk()
m = MainWindow(root)
m.frame.pack(padx=10, pady=20)
root.title("Transfer Classes Organizer")
info_area = Label(m.frame, text='')
info_area.pack(side=TOP, fill=X)

def clear_info_area():
	info_area.config(text="")

def inform_user_error(label, content):
	label.config(text=content, font=("Arial", 18), fg='red')
	root.update()

def inform_user_action(label, content):
	label.config(text=content, font=("Arial", 18), fg='green')
	root.update()

def fetch_majors_info(user):
	for school in user.current_schools:
		for major in user.majors:
			ninja.fetch_report(school, major.school_code, major.code, '12-13')
			classes = ninja.groups_for(major.code, major.school_code)
			major.add_required_courses(school, classes)

def add_school_handler(user, form):
	clear_info_area()
	user.add_current_school(form.entries[0].get())
	form.frame.pack_forget()

def add_major_handler(user, form):
	clear_info_area()
	# Error Handling
	if not len(user.current_schools):
		inform_user_error(info_area, "You need to add a current school first")
		return
	name = form.entries[0].get()
	school = form.entries[1].get()
	user.add_major(Major(name, school))
	inform_user_action(info_area, "Fetching information from assist.org...")
	#Ask assist Ninja for report
	try:
		fetch_majors_info(user)
	except Exception:
		inform_user_error(info_area, "Unable to connect, please check internet connection.")
		return
	inform_user_action(info_area, "Information successfully retrieved.")
	form.frame.pack_forget()

current_table = InformationTable(m.frame, "Current School:", TOP)
if not len(user.current_schools):
	add_school_form = FormFrame(current_table.frame)
	add_school_form.add_field("Add Current School:")
	add_school_form.add_button("Add", lambda : add_school_handler(user, add_school_form))
	add_school_form.frame.pack(side=TOP, fill=X)


transfer_table = InformationTable(m.frame, "Majors you are pursuing:", BOTTOM)
if not len(user.majors):
	add_major_form = FormFrame(transfer_table.frame)
	Label(add_major_form.frame, text="Add Major:", font=("Arial", 18)).pack(side=TOP, fill=X)
	add_major_form.add_field("Major's name:")
	add_major_form.add_field("University offering the major:")
	add_major_form.add_button("Add", lambda : add_major_handler(user, add_major_form))
	add_major_form.frame.pack(side=TOP, fill=X)

# transfer_table.add_sub_frame("UC Berkeley")
# transfer_table.add_list("UC Berkeley", "Classes you need to take:", ["MATH3C", "MATH3E", "ENG1B"], False)
# transfer_table.add_sub_frame("UC Davis")
# transfer_table.add_list("UC Davis", "Classes you need to take:", ["MATH3C", "MATH3F", "ENG1B", "ECON1A"], False)
# 
# current_table.add_sub_frame("Laney")
# current_table.add_list("Laney", "Classes you have taken:", ["MATH3A", "MATH3B", "ENG1A"], True)
# listeners = [transfer_table.lists["UC Berkeley"], transfer_table.lists["UC Davis"]]
# current_table.add_form("Add class", "Add", current_table.lists["Laney"], listeners)

root.mainloop()













