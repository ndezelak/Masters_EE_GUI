# Revision History
# 25/07: Defined a basic structure. Read the reference of tkinter to get an overview on how it works and what you can do.



# This should be the main script where
# all the GUI elements are intialized and callback methods are set.

from tkinter import *
import ttk as nttk
from Application import *
# Create a toplevel window
# Each window has its own tcl interpreter
root=Tk()
style=nttk.Style()
frame = nttk.Frame(root)
frame.pack()

button_quit = nttk.Button(frame, text="Quit this shit", command=quit, width=100, state="disabled")
button_quit.pack()

button_toggle = nttk.Button(frame, text="Toggle the left button")#, command=dummy_callback)
button_toggle.pack(side=LEFT)
button_toggle.bind("<Button-1>", dummy_callback)

button_2 = nttk.Button(frame, text="Toggle the left button")#, command=dummy_callback)
button_2.pack(side=LEFT, expand=TRUE, fill=X)
button_2.bind("<Button-1>", dummy_callback)

# Listbox example
Lb1 = Listbox(frame)
Lb1.insert(1,"First value")
Lb1.insert(2,"Second value")
Lb1.insert(3,"Third value")
Lb1.pack(side=BOTTOM)

# Text
Txt1=nttk.Label(frame, text="Subjects")
Txt1.pack(side=BOTTOM)


Radio1=nttk.Radiobutton(frame, text="Option 1", value=1)
Radio1.pack()

Radio2=nttk.Radiobutton(frame, text="Option 2", value=2)
Radio2.pack()

Radio3=nttk.Radiobutton(frame, text="Option 3", value=3)
Radio3.pack()

root.mainloop()
