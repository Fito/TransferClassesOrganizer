try: 
	# default python should be 3
	from tkinter import *
except ImportError:
	# most likely triggered by using python 2.7 or lower
	from Tkinter import *

# Import the project files
from models.major import *
from models.user import *
from lib.assist_ninja import *
from storage import *
from views.gui import *

# create Storage manager object
storage = Storage('user_info.json')
# create AssistNinja object
ninja = AssistNinja()
# build an User object from the user_info.json file or creates a new one if file is empty
user = storage.build_from_file(User())
# create Tkinter's root
root = Tk()

# create MainWindow object, which is nested into root
m = MainWindow(root)
m.frame.pack(padx=10, pady=20)
root.title("Transfer Classes Organizer")

#create an info area, to keep the user informed of processes and errors
info_area = Label(m.frame, text='')
info_area.pack(side=TOP, fill=X)

def clear_info_area():
	# Clears the info area
	info_area.config(text="")

def inform_user_error(content):
	# Informs displays a message on the info area, in color red
	info_area.config(text=content, font=("Arial", 18, 'bold'), fg='red')
	root.update()

def inform_user_action(content):
	# Informs displays a message on the info area, in color green
	info_area.config(text=content, font=("Arial", 18, 'bold'), fg='green')
	root.update()

def save_user_data():
	# Stores the user data into the user_info.json file
	inform_user_action("Saving your data...")
	storage.store(user)
	root.destroy()

def fetch_majors_info(user):
	# Triggers our assist ninja object to fetch the majors' information
	for school in user.current_schools_codes:
		for major in user.majors:
			ninja.fetch_report(school, major.school_code, major.code, '12-13')
			classes = ninja.groups_for(major.code, major.school_code)
			major.add_required_courses(school, classes)
		
	

def add_class(school, classes_taken_list, form, classes_required_lists):
	clear_info_area()
	# Adds a class taken, both to the user and the classes list, when the 'Add' button is pressed
	item = form.entries[0].get().upper()
	for classes_list in classes_required_lists:
		classes_list.delete_item(item)
	classes_taken_list.add_to_list(form.entries[0])
	user.add_class_taken(school, item)

def delete_class(classes_taken_list):
	clear_info_area()
	# Deletes a class taken, both from the user and the classes list.
	try:
		user.remove_class_taken(classes_taken_list.current_selection())
		classes_taken_list.delete_selected_item()
	except Exception:
		inform_user_error("No item selected")

def render_classes_taken_table(table):
	# Renders the classes taken list with updated values
	# It removes the existing content content of the table
	if len(table.winfo_children()) > 1:
		for w in table.winfo_children():
			w.pack_forget()
		Label(current_table, text="Curret School:", font=('Arial', 21, 'bold')).pack(side=TOP, fill=X, pady=10)
	
	# It creates a new frame nested into the table		
	school = user.current_schools[0]
	frame = Frame(table)
	frame.pack()
	# It creates a label with the school's name and a ListFrame object that holds the classes taken
	Label(frame, text=school, font=("Arial", 18)).pack()
	list_frame = ListFrame(frame, "Classes you have taken:", user.courses_taken(school))
	# It creates a button and binds it to the delete_class function, passing to it the ListFrame object
	Button(list_frame.frame, text="Delete selected", command= lambda : delete_class(list_frame)).pack()
	list_frame.pack()
	clear_info_area()
	# If the user has not added a major yet, it creates a form for adding classes without listener lists
	if not user.has_majors():
		form = FormFrame(list_frame.frame)
		form.add_field("Add class:")
		form.add_button("Add", lambda : add_class(school, list_frame, form, []))
		form.pack()
	
	return list_frame

def render_classes_required_table(parent_table, classes_taken_frame):
	for school_code in user.current_schools_codes:
		for major in user.majors:
			# It creates a frame nested in the parent_table
			title_frame = Frame(parent_table)
			title_frame.pack()
			# Title with major and school name
			Label(title_frame, text=(major.name + " - " + major.school_code)).pack()
			classes_required_lists = []

			groups = major.courses_required_from(school_code)
			for group in groups:
				# each group has one key, which is the groups title
				key = group.keys()[0]
				# remove classes already taken from list of classes needed
				group[key] = [item for item in group[key] if item not in user.courses_taken(school_code)]
				
				group_frame = Frame(title_frame)
				sub_title = Label(group_frame, text=key)
				sub_title.pack()
				group_list = ListFrame(parent_table, key, group[key])
				group_list.frame.pack(side=LEFT, padx=5, anchor=N)
				# It stores the lists of classes needed so they can listen to the classes taken list
				classes_required_lists.append(group_list)
		
		# It Adds the 'add class' form, binding the classes taken lists to the classes_required_lists
		classes_taken_list = render_classes_taken_table(classes_taken_frame)
		form = FormFrame(classes_taken_list.frame)
		form.add_field("Add class:")
		form.add_button("Add", lambda : add_class(user.current_schools[0], classes_taken_list, form, classes_required_lists))
		form.pack()
	clear_info_area()

#Classes taken list is empty until school is create by add_school_handler
def add_school_handler(form, form_parent):
	clear_info_area()
	user.add_current_school(form.entries[0].get())
	form.frame.pack_forget()
	render_classes_taken_table(form_parent)

#Classes needed list is empty until major is created by add_major_handler
def add_major_handler(form, form_parent, classes_taken_frame):
	clear_info_area()
	# Error Handling
	if not len(user.current_schools):
		inform_user_error("You need to add a current school first")
		return
	name = form.entries[0].get()
	school = form.entries[1].get()
	user.add_major(Major(name, school))
	inform_user_action("Fetching information from assist.org...")
	#Ask AssistNinja for a report
	try:
		fetch_majors_info(user)
	except Exception:
		inform_user_error("Unable to connect, please check internet connection.")
		return
	inform_user_action("Information successfully retrieved.")
	form.frame.pack_forget()
	# It renders the classes required table
	render_classes_required_table(form_parent, classes_taken_frame)

# It creates an empty frame for the current school and classes taken
current_table = Frame(m.frame, padx=20, pady=20, bd=2, relief='ridge')
Label(current_table, text="Current School:", font=('Arial', 21, 'bold')).pack(side=TOP, fill=X, pady=10)
current_table.pack(side=LEFT, padx=5, anchor=N)

# If user already has a current school, just render the classes taken table
if user.has_current_school():
	classes_taken_lists = render_classes_taken_table(current_table)
else:
	# If user doesn't have a current school, display 'Add current school' form
	add_school_form = FormFrame(current_table)
	add_school_form.add_field("Add Current School:")
	add_school_form.add_button("Add", lambda : add_school_handler(add_school_form, current_table))
	add_school_form.frame.pack(side=TOP, fill=X)

# It creates an empty frame for the major and classes needed
transfer_table = Frame(m.frame, padx=20, pady=20, bd=2, relief='ridge')
Label(transfer_table, text="Majors you are pursuing:", font=('Arial', 21, 'bold')).pack(side=TOP, fill=X, pady=10)
transfer_table.pack(side=RIGHT, padx=5, anchor=N)

# If user already has a major, just render the classes needed table
if user.has_majors():
	render_classes_required_table(transfer_table, current_table)
else:
	#  If user doesn't have a major, display 'Add major' form
	add_major_form = FormFrame(transfer_table)
	Label(add_major_form.frame, text="Add Major:", font=("Arial", 18)).pack(side=TOP, fill=X)
	add_major_form.add_field("Major's name:")
	add_major_form.add_field("University offering the major:")
	add_major_form.add_button("Add", lambda : add_major_handler(add_major_form, transfer_table, current_table))
	add_major_form.frame.pack(side=TOP, fill=X)

# Call save_user_data before the main window is closed
root.protocol("WM_DELETE_WINDOW", save_user_data)

root.mainloop()








