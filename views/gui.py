try: 
	# default python should be 3
	from tkinter import *
except ImportError:
	# most likely triggered by using python 2.7
	from Tkinter import *

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

class MainWindow():
	""" Main Window: Nested directly into the Tk main frame. The constructor's 
			only parameter is a parent frame """

	def __init__(self, parent):
		self.frame = Frame(parent)


class ListFrame():
	""" List Frame: Wrapper class for Tk frames that hold a title and a list. 
			The constructor's parameters are a parent frame, a title, an items list
	 		and a boolean to determine the use of a delete button """

	def __init__(self, parent, title, items_list, delete_button=True):
		frame = self.frame = Frame(parent, bd=1, relief=RAISED, padx=5, pady=5)
		self.items_list = items_list
		self.list_box = Listbox(self.frame, width=20, height=len(self.items_list), relief=SUNKEN)
		
		Label(self.frame, text=title).pack(padx=10, pady=5)
		self.populate_list(self.items_list).pack(padx=10, pady=5)
		if delete_button:
			Button(self.frame, text="Delete selected", command=self.delete_selected_item).pack()
	
	def populate_list(self, items_list):
		self.list_box.delete(0, END)
		for item in items_list:
			self.list_box.insert(END, item)
		self.list_box.config(height=len(self.items_list))
		return self.list_box
		
	def delete_selected_item(self):
		if self.list_box.curselection():
			current = int(self.list_box.curselection()[0])
			self.items_list = remove_values_from_list(self.items_list, self.items_list[current])
			self.list_box.delete(current)
			self.populate_list(self.items_list)	
	
	def pack(self):
		self.frame.pack(padx=10, pady=10)
		
	def add_to_list(self, form_entry, listeners=[]):
		item = form_entry.get().upper().replace(" ", "")
		self.items_list.append(item)
		if len(listeners): 
			for list_form in listeners:
				list_form.delete_item(item)
		form_entry.delete(0, END)
		self.populate_list(self.items_list)
	
	def delete_item(self, item):
		self.items_list = remove_values_from_list(self.items_list, item)
		self.populate_list(self.items_list)
	
	
	
class FormFrame():
	"""	Form Frame: Wrapper class for Tk frames that let the user input
			information through a form with labels and text fields. The constructor's
			only parameter is a parent frame"""

	def __init__(self, parent):
		frame = self.frame = Frame(parent)
		self.entries = []
	
	def pack(self):
		self.frame.pack(side=RIGHT)
	
	def add_field(self, title):
		Label(self.frame, text=title).pack(padx=5, pady=5)
		entry = Entry(self.frame)
		entry.pack(padx=5, pady=5)
		self.entries.append(entry)
	
	def add_button(self, title, action):
		Button(self.frame, text=title, command=action).pack(padx=5, pady=5)
	

class InformationTable():
	""" Information Table: Wrapper class for ListFrame and FormFrame classes.
			It makes it easier to organize multiple lists inside of a frame
			and add froms that relate these lists to other lists """
			
	def __init__(self, parent, title, position):
		self.frame = Frame(parent)
		self.title = Label(self.frame, text=title, font=('Arial', 24, 'bold'))
		self.title.pack(side=TOP, fill=X, pady=10)
		self.frame.pack(side=position)
		self.sub_frames = {}
		self.lists = {}

	def add_sub_frame(self, subtitle):
		single_list_frame = Frame(self.frame)
		Label(single_list_frame, text=subtitle, font=('Arial', 20)).pack()
		self.sub_frames[subtitle] = single_list_frame
		single_list_frame.pack(side=LEFT, padx=5)
		return single_list_frame

	def add_list(self, frame_title, title, items_list, delete_button):
		frame = self.sub_frames[frame_title]
		list_frame = ListFrame(frame, title, items_list, delete_button)
		list_frame.pack()
		self.lists[frame_title] = list_frame
	
	def add_form(self, title, button_name, list_frame, related_list):
		form = FormFrame(list_frame.frame)
		form.add_field(title)
		form.add_button(button_name, lambda : list_frame.add_to_list(form.entries[0], related_list))
		form.pack()
	
				






















