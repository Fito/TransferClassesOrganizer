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
		frame = self.frame = Frame(parent, bd=2, relief='ridge', padx=5, pady=5)
		
		self.items_list = items_list
		self.list_and_scroll = Frame(self.frame)
		self.list_box = Listbox(self.list_and_scroll, width=20, height=5, relief='ridge')
		self.list_and_scroll.pack()                
		self.sb = Scrollbar(self.list_and_scroll, orient=VERTICAL)
		self.sb.configure(command=self.list_box.yview)
		self.list_box.configure(yscrollcommand=self.sb.set)
		
		self.title = Label(self.frame, text=title).pack(padx=10, pady=5)
		self.populate_list(self.items_list).pack(padx=10, pady=5, side=LEFT)

		if delete_button:
			Button(self.frame, text="Delete selected", command=self.delete_selected_item).pack()

	def add_scrollbar(self):
		self.sb.pack(side=RIGHT, fill=Y)
		
	def populate_list(self, items_list):
		self.list_box.delete(0, END)
		for item in items_list:
			self.list_box.insert(END, item)
		if len(items_list) > 5:
                        self.add_scrollbar()
		return self.list_box
		
	def delete_selected_item(self):
		if self.list_box.curselection():
			current = int(self.list_box.curselection()[0])
			self.items_list = remove_values_from_list(self.items_list, self.items_list[current])
			self.list_box.delete(current)
			self.populate_list(self.items_list)	
	
	def pack(self):
		self.frame.pack(padx=10, pady=10)
		
	def add_to_list(self, form_entry):
		item = form_entry.get().upper()
		self.items_list.append(item)
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
					






















