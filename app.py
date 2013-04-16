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
# user.add_current_school("Laney")
# user.add_class_taken("Laney", "MATH 3A")
# user.add_class_taken("Laney", "MATH 3B")

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
	for school in user.current_schools_codes:
		for major in user.majors:
			ninja.fetch_report(school, major.school_code, major.code, '12-13')
			classes = ninja.groups_for(major.code, major.school_code)
			major.add_required_courses(school, classes)

def add_class(school, classes_taken_list, form, classes_required_lists):
	item = form.entries[0].get()
	for classes_list in classes_required_lists:
		classes_list.delete_item(item)
	
	classes_taken_list.add_to_list(form.entries[0])
	user.add_class_taken(school, item)

def render_classes_taken_table(table):
	print "classes taken table rendered"
	#erase list and re render with updated bindings
	if len(table.winfo_children()) > 1:
		for w in table.winfo_children()[1].winfo_children():
			w.pack_forget()
			
	school = user.current_schools[0]
	frame = Frame(table)
	frame.pack()
	Label(frame, text=school, font=("Arial", 18)).pack()
	list_frame = ListFrame(frame, "Classes you have taken:", user.courses_taken(school), True)
	list_frame.pack()
	clear_info_area()

	if not user.has_majors():
		print "No majors, so no bindings"
		form = FormFrame(list_frame.frame)
		form.add_field("Add class:")
		form.add_button("Add", lambda : add_class(school, list_frame, form, []))
		form.pack()
	
	return list_frame.frame

def render_classes_required_table(parent_table, classes_taken_frame):
	for school_code in user.current_schools_codes:
		for major in user.majors:
			title_frame = Frame(parent_table)
			title_frame.pack()
			# Title with major and school name
			Label(title_frame, text=(major.name + " - " + major.school_code)).pack()
			classes_required_lists = []

			groups = major.courses_required_from(school_code)
			for group in groups:
				key = group.keys()[0] # each group has only one key, which is the groups title
				# remove classes already taken from list of classes needed
				group[key] = [item for item in group[key] if item not in user.courses_taken(school_code)]

				group_frame = Frame(title_frame)
				sub_title = Label(group_frame, text=key)
				sub_title.pack()
				group_list = ListFrame(parent_table, key, group[key], False)
				group_list.frame.pack(side=LEFT, padx=5, anchor=N)
				classes_required_lists.append(group_list)
		
		# adding the 'add class' form
		classes_taken_list = render_classes_taken_table(classes_taken_frame)
		form = FormFrame(classes_taken_list)
		form.add_field("Add class:")
		form.add_button("Add", lambda : add_class(school, classes_taken_list, form, classes_required_lists))
		form.pack()
	clear_info_area()

#Classes taken list is empty until school is create by add_school_handler
def add_school_handler(form, form_parent):
	clear_info_area()
	user.add_current_school(form.entries[0].get())
	form.frame.pack_forget()
	render_classes_taken_table(form_parent)

def add_major_handler(form, form_parent, classes_taken_frame):
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
	render_classes_required_table(form_parent, classes_taken_frame)


current_table = Frame(m.frame, padx=20, pady=20, bd=2, relief='ridge')
Label(current_table, text="Curret School:", font=('Arial', 21, 'bold')).pack(side=TOP, fill=X, pady=10)
current_table.pack(side=LEFT, padx=5, anchor=N)

if user.has_current_school():
	classes_taken_lists = render_classes_taken_table(current_table)
else:
	add_school_form = FormFrame(current_table)
	add_school_form.add_field("Add Current School:")
	add_school_form.add_button("Add", lambda : add_school_handler(add_school_form, current_table))
	add_school_form.frame.pack(side=TOP, fill=X)
	
transfer_table = Frame(m.frame, padx=20, pady=20, bd=2, relief='ridge')
Label(transfer_table, text="Majors you are pursuing:", font=('Arial', 21, 'bold')).pack(side=TOP, fill=X, pady=10)
transfer_table.pack(side=RIGHT, padx=5, anchor=N)

if user.has_majors():
	render_classes_required_table(transfer_table, current_table)
else:
	add_major_form = FormFrame(transfer_table)
	Label(add_major_form.frame, text="Add Major:", font=("Arial", 18)).pack(side=TOP, fill=X)
	add_major_form.add_field("Major's name:")
	add_major_form.add_field("University offering the major:")
	add_major_form.add_button("Add", lambda : add_major_handler(add_major_form, transfer_table, current_table))
	add_major_form.frame.pack(side=TOP, fill=X)

root.mainloop()













