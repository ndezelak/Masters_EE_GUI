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


COL_SPAN_CHOOSER=1
ROW_SPAN_CHOOSER=4
COL_SPAN_OVERVIEW=1
ROW_SPAN_OVERVIEW=4
ROW_SPAN=3
COL_SPAN=2

# ***Main Frame*** (Used with the grid manager)
frame = nttk.Frame(root)
frame.pack(fill=BOTH, expand=TRUE)


# ***Left Frame***
frame_chooser = nttk.Frame(frame)
Grid.grid_columnconfigure(frame,0,weight=20)

# Used to center both control widgets
Grid.grid_rowconfigure(frame,0,weight=20)
Grid.grid_rowconfigure(frame,1,weight=1)
Grid.grid_rowconfigure(frame,2,weight=20)

frame_chooser.grid(column=0, row=0, rowspan=ROW_SPAN, sticky=N+S+E+W)

# ***Options Frame***
frame_options=nttk.Frame(frame)
Grid.grid_columnconfigure(frame,1,weight=1)
frame_options.grid(row=1, column=1, sticky=NSEW)

# ***Right Frame***
frame_overview = nttk.Frame(frame)
Grid.grid_columnconfigure(frame,2,weight=20)
frame_overview.grid(column=2, row=0, rowspan=ROW_SPAN, sticky=N+S+E+W)


# Subframe for "Hauptwahlpflicht"
frame_hauptpflicht = nttk.Frame()
txt=nttk.Label(frame_hauptpflicht, text="Some text")
txt.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_sample=nttk.Button(frame_hauptpflicht, text="Click me!")
button_sample.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Subframe for "Hauptwahl"
frame_hauptwahl = nttk.Frame()
txt=nttk.Label(frame_hauptwahl, text="Some text")
txt.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_sample=nttk.Button(frame_hauptwahl, text="Click me!")
button_sample.pack(side=LEFT, expand=TRUE, fill=BOTH)



# Notebook construction
notebook=nttk.Notebook(frame_chooser)
notebook.add(frame_hauptpflicht, text="Hauptwahlpflicht")
notebook.add(frame_hauptwahl, text="Hauptwahl")
notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)


# Adding bottons to option frame
button_add=nttk.Button(frame_options, text=">>")
button_add.pack(side=TOP)
button_delete=nttk.Button(frame_options, text="<<")
button_delete.pack(side=TOP)

# Title for the overview section
title_overview=nttk.Label(frame_overview, text="Overview")
title_overview.pack(anchor=N, expand=TRUE)

'''
button_toggle = nttk.Button(frame_overview, text="Toggle the left button")#, command=dummy_callback)
button_toggle.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_toggle.bind("<Button-1>", dummy_callback)

button_2 = nttk.Button(frame_chooser, text="Toggle the left button")#, command=dummy_callback)
button_2.pack(side=LEFT, expand=TRUE, fill=BOTH)
#button_2.grid(column=1, row=1, sticky=N+S+E+W)
button_2.bind("<Button-1>", dummy_callback)

Lb1 = Listbox(frame_chooser)
Lb1.insert(1,"First value")
Lb1.insert(2,"Second value")
Lb1.insert(3,"Third value")
Lb1.pack(side=BOTTOM)

# Text
Txt1=nttk.Label(frame_chooser, text="Subjects")
Txt1.pack(side=BOTTOM)


Radio1=nttk.Radiobutton(frame_chooser, text="Option 1", value=1)
Radio1.pack()

Radio2=nttk.Radiobutton(frame_chooser, text="Option 2", value=2)
Radio2.pack()

Radio3=nttk.Radiobutton(frame_chooser, text="Option 3", value=3)
Radio3.pack()
'''
# Listbox example


root.mainloop()
