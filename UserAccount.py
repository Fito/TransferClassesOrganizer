from Tkinter import *
win=Tk()
f = Frame(win)
registration_top = Frame(win)
l = Label(win, text="Do you have an account?")

def open_new_window():
    top = Toplevel(win)
    Label(top, text="Enter your email").pack(pady=10, padx=10)
    Entry(top).pack()
    Label(top, text="Enter a password").pack(pady=10, padx=10)
    Entry(top).pack()
    b1 = Button(top, text="Sign in")
    b1.pack(pady=10, padx=10)
    
def open_registration_window():
    l.pack_forget()
    f.pack_forget()
    Label(registration_top, text="First Name").pack(pady=10, padx=10)
    Entry(registration_top).pack()
    Label(registration_top, text="Last Name").pack(pady=10, padx=10)
    Entry(registration_top).pack()
    Label(registration_top, text="Email").pack(pady=10, padx=10)
    Entry(registration_top).pack()
    Label(registration_top, text="Password").pack(pady=10, padx=10)
    Entry(registration_top).pack()
    Label(registration_top, text="Confirm password").pack(pady=10, padx=10)
    Entry(registration_top).pack()
    b2 = Button(registration_top, text="Sign up", command=makeWindow)
    b2.pack(pady=10, padx=10)
    registration_top.pack()
    
def makeWindow():
    global Username, Email
    
    registration_top.pack_forget()
    frame1 = Frame(win)
    frame1.pack()
    
    Label(frame1, text="Username").grid(row=0, column=0, sticky=W)
    Username = StringVar()
    Username = Entry(frame1, textvariable=Username)
    Username.grid(row=0, column=1, sticky=W)
    
    Label(frame1, text="Email").grid(row=1, column=0, sticky=W)
    Email = StringVar()
    Email = Entry(frame1, textvariable=Email)
    Email.grid(row=1, column=1, sticky=W)
    
    frame2 = Frame(win)
    frame2.pack()
    l = Label(frame2, text="Current School")
    l.pack()
    b1 = Button(frame2, text="Select")
    b1.pack(side=LEFT, padx=7)
    
    lb = Listbox(frame2, height=1, width=35)
    lb.pack()



b1 = Button(f, text="Sign in", command=open_new_window)
b2 = Button(f, text="Create an account", command=open_registration_window)
b1.pack(side=LEFT, padx=5)
b2.pack(side=LEFT, padx=5)
l.pack()
f.pack()
win.mainloop()