try: 
	# default python should be 3
	from tkinter import *
except ImportError:
	# most likely triggered by using python 2.7
	from Tkinter import *

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


class ListFrame():
	""" List Frame: Wrapper class for Tk frames that hold a title and a list. 
			The constructor's parameters are a parent frame, a title, and an items list """

	def __init__(self, parent, title, items_list):
	  # It creates a frame inside the provided parent
	  # It creates a frame for a scrollbar and a listbox
	  # It packs the listbox
	  # It calls the populate_list method
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
		
	def add_scrollbar(self):
	  # It packs the scrollbar
		self.sb.pack(side=RIGHT, fill=Y)
		
	def populate_list(self, items_list):
	  # It add the items passed into the listbox
		self.list_box.delete(0, END)
		for item in items_list:
			self.list_box.insert(END, item)
		if len(items_list) > 5:
                        self.add_scrollbar()
		return self.list_box
		
	def delete_selected_item(self):
	  # It removes the currently selected item form the listbox
		if self.list_box.curselection():
			current = int(self.list_box.curselection()[0])
			self.items_list = remove_values_from_list(self.items_list, self.items_list[current])
			self.list_box.delete(current)
			self.populate_list(self.items_list)
	
	def current_selection(self):
	  # It returns the currently selected item
		return self.items_list[int(self.list_box.curselection()[0])]
	
	def pack(self):
		self.frame.pack(padx=10, pady=10)
		
	def add_to_list(self, form_entry):
	  # It adds the item in the passed form_entry to the listbox
		item = form_entry.get().upper()
		self.items_list.append(item)
		form_entry.delete(0, END)
		self.populate_list(self.items_list)
	
	def delete_item(self, item):
	  # It deletes a passed item from the listbox
		self.items_list = remove_values_from_list(self.items_list, item)
		self.populate_list(self.items_list)
	
	
	
class FormFrame():
	"""	Form Frame: Wrapper class for Tk frames that let the user input
			information through a form with labels and text fields. The constructor's
			only parameter is a parent frame"""

	def __init__(self, parent):
	  # It creates a frame inside the passed parent
		frame = self.frame = Frame(parent)
		self.entries = []
	
	def pack(self):
		self.frame.pack(side=RIGHT)
	
	def add_field(self, title):
	  # It adds a label and an entry to the parent frame
		Label(self.frame, text=title).pack(padx=5, pady=5)
		entry = Entry(self.frame)
		entry.pack(padx=5, pady=5)
		self.entries.append(entry)
	
	def add_button(self, title, action):
	  # It adds a button to the frame, and binds the passed action to it
		Button(self.frame, text=title, command=action).pack(padx=5, pady=5)
					






















