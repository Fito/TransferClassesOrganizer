<<<<<<< HEAD
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
    
=======
from tkinter import *

win = Tk()
f = Frame(win)

def open_new_window():
    
    top = Frame(f)
    top.pack()
    Label(top, text="Email").pack(pady=10, padx=10)
    Entry(top).pack()
    Label(top, text="Password").pack(pady=10, padx=10)
    Entry(top).pack()
    b1 = Button(top, text="Sign in")
    b1.pack(pady=10, padx=10)

def open_registration_window():
    f.pack_forget() #clear frame.. 
    top = Frame(win, width=100, height=100)
    top.pack(side='bottom')
    Label(top, text="First Name").pack(pady=10, padx=10)
    Entry(top).pack(anchor=W)
    Label(top, text="Last Name").pack(pady=10, padx=10)
    Entry(top).pack(anchor=E)
    Label(top, text="Email").pack(pady=10, padx=10)
    Entry(top).pack()
    Label(top, text="Password").pack(pady=10, padx=10)
    Entry(top).pack()
    Label(top, text="Confirm password").pack(pady=10, padx=10)
    Entry(top).pack()
    b2 = Button(top, text="Sign up", command=makeWindow)
    b2.pack(pady=10, padx=10)


def makeWindow () :
    global Username, Email
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

>>>>>>> 95e96a068310152c99dd2f332ddb57780d5cb97f
    Label(frame1, text="Username").grid(row=0, column=0, sticky=W)
    Username = StringVar()
    Username = Entry(frame1, textvariable=Username)
    Username.grid(row=0, column=1, sticky=W)
<<<<<<< HEAD
    
=======

>>>>>>> 95e96a068310152c99dd2f332ddb57780d5cb97f
    Label(frame1, text="Email").grid(row=1, column=0, sticky=W)
    Email = StringVar()
    Email = Entry(frame1, textvariable=Email)
    Email.grid(row=1, column=1, sticky=W)
<<<<<<< HEAD
    
    frame2 = Frame(win)
    frame2.pack()
    l = Label(frame2, text="Current School")
    l.pack()
    b1 = Button(frame2, text="Select")
    b1.pack(side=LEFT, padx=7)
    
    lb = Listbox(frame2, height=1, width=35)
    lb.pack()
=======

    frame2 = Frame(win)
    frame2.pack()
    l = Label(frame2, text="Current College")
    l.pack()
    b1 = Button(frame2, text="Select")
    b1.pack(side=LEFT, padx=7)

    lb = Listbox(frame2, height=3, width=35)
    lb.pack()
    lb.insert(END, "Allan Hancock College")
    lb.insert(END, "American River College")
    lb.insert(END, "Antelope Valley College")
    lb.insert(END, "Bakersfield College")
    lb.insert(END, "Barstow Community College")
    lb.insert(END, "Butte College")
    lb.insert(END, "Cabrillo College")
    lb.insert(END, "Berkeley City College")
    lb.insert(END, "Laney")
    lb.insert(END, "Alameda")
    lb.insert(END, "Merit")
    sb = Scrollbar(frame2, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    sb.configure(command=lb.yview)
    lb.configure(yscrollcommand=sb.set)
    lb.pack(side=LEFT, fill=BOTH, expand=1)

    frame3 = Frame(win)
    frame3.pack()
    l = Label(frame3, text="Transfer to")
    l.pack()
    b1 = Button(frame3, text="Select")
    b1.pack(side=LEFT, padx=7)

    lb = Listbox(frame3, height=3)
    lb.pack()
    lb.insert(END, "California Maritime Academy")
    lb.insert(END, "California Polytechnic University, Pomona")
    lb.insert(END, "California Polytechnic University, San Luis Obispo")
    lb.insert(END, "California State University, Bakersfield")
    lb.insert(END, "California State University, Channel Islands")
    lb.insert(END, "California State University, Chico")
    lb.insert(END, "California State University, Dominguez Hills")
    lb.insert(END, "California State University, East Bay")
    lb.insert(END, "California State University, Fresno")
    lb.insert(END, "California State University, Fullerton")
    lb.insert(END, "California State University, Long Beach")
    lb.insert(END, "California State University, Los Angeles")
    lb.insert(END, "California State University, Monterey Bay")
    lb.insert(END, "California State University, Northridge")
    lb.insert(END, "California State University, Sacramento")
    lb.insert(END, "California State University, San Bernardino")
    lb.insert(END, "California State University, San Marcos")
    lb.insert(END, "California State University, Stanislaus")
    lb.insert(END, "Humboldt State University")
    lb.insert(END, "San Diego State University")
    lb.insert(END, "Sonoma State University")
    lb.insert(END, "UC Davis School of Veterinary Medicine")
    lb.insert(END, "UCSF School of Dentistry")
    lb.insert(END, "UCSF School of Pharmacy")
    lb.insert(END, "University of California, Berkeley")
    lb.insert(END, "University of California, Davis")
    lb.insert(END, "University of California, Irvine")
    lb.insert(END, "University of California, Los Angeles")
    lb.insert(END, "University of California, Merced")
    lb.insert(END, "University of California, Riverside")
    lb.insert(END, "University of California, San Diego")
    lb.insert(END, "University of California, Santa Barbara")
    lb.insert(END, "University of California, Santa Cruz")
    sb = Scrollbar(frame3, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    sb.configure(command=lb.yview)
    lb.configure(yscrollcommand=sb.set)
    lb.pack(side=LEFT, fill=BOTH, expand=1)

    frame4 = Frame(win)
    frame4.pack()
    l = Label(frame4, text="Major")
    l.pack()
    b1 = Button(frame4, text="Select")
    b1.pack(side=LEFT, padx=7)

    lb = Listbox(frame4, height=3)
    lb.pack()
    lb.insert(END, "Bioengineering, Lower Division B.S.")
    lb.insert(END, "Bioengineering/Materials Science and Engineering, Lower Division B.S.")
    lb.insert(END, "Chemical Biology, Lower Division B.S.")
    lb.insert(END, "Chemical Engineering & Materials Science & Engineering, Lower Division B.S.")
    lb.insert(END, "Chemical Engineering & Nuclear Engineering, Lower Division B.S.")
    lb.insert(END, "California State University, Chico")
    lb.insert(END, "California State University, Dominguez Hills")
    lb.insert(END, "California State University, East Bay")
    lb.insert(END, "California State University, Fresno")
    lb.insert(END, "California State University, Fullerton")
    lb.insert(END, "California State University, Long Beach")
    lb.insert(END, "California State University, Los Angeles")
    lb.insert(END, "California State University, Monterey Bay")
    lb.insert(END, "California State University, Northridge")
    lb.insert(END, "California State University, Sacramento")
    lb.insert(END, "California State University, San Bernardino")
    lb.insert(END, "California State University, San Marcos")
    lb.insert(END, "California State University, Stanislaus")
    lb.insert(END, "Humboldt State University")
    lb.insert(END, "San Diego State University")
    lb.insert(END, "Sonoma State University")
    lb.insert(END, "UC Davis School of Veterinary Medicine")
    lb.insert(END, "UCSF School of Dentistry")
    lb.insert(END, "UCSF School of Pharmacy")
    lb.insert(END, "University of California, Berkeley")
    lb.insert(END, "University of California, Davis")
    lb.insert(END, "University of California, Irvine")
    lb.insert(END, "University of California, Los Angeles")
    lb.insert(END, "University of California, Merced")
    lb.insert(END, "University of California, Riverside")
    lb.insert(END, "University of California, San Diego")
    lb.insert(END, "University of California, Santa Barbara")
    lb.insert(END, "University of California, Santa Cruz")
    sb = Scrollbar(frame4, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    sb.configure(command=lb.yview)
    lb.configure(yscrollcommand=sb.set)
    lb.pack(side=LEFT, fill=BOTH, expand=1)
>>>>>>> 95e96a068310152c99dd2f332ddb57780d5cb97f



b1 = Button(f, text="Sign in", command=open_new_window)
b2 = Button(f, text="Create an account", command=open_registration_window)
<<<<<<< HEAD
b1.pack(side=LEFT, padx=5)
b2.pack(side=LEFT, padx=5)
l.pack()
f.pack()
win.mainloop()
=======
b1.pack(side=LEFT, padx=5, pady=5)
b2.pack(side=LEFT, padx=5, pady=5)
l = Label(win, text="Do you have an account?")
l.pack()
f.pack()




>>>>>>> 95e96a068310152c99dd2f332ddb57780d5cb97f
