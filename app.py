from Tkinter import *

class App():
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.label(frame)

main_window = Tk()
app = App(main_window)

main_window.mainloop()