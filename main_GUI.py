# Revision History
# 25/07: Defined a basic structure. Read the reference of tkinter to get an overview on how it works and what you can do.
# 23/08: Restructured code into classes representing each main frame. Define structure according to design
# 06/09: Defined GUI for the upper left corner
#----------------------------------------------------------------#
# Description:
# This should be the main script where
# all the GUI elements are intialized and callback methods are set.

from tkinter import *

import ttk as nttk
from GUI.TopFrames.TopLeftFrame import *
from GUI.BottomFrames.ChooserFrame import *
from GUI.BottomFrames.OverviewFrame import *
from GUI.TopFrames.TopRightFrame import *


# Create a toplevel window
# Each window has its own tcl interpreter
root=Tk()


# Some constants for your layout
ROW_SPAN=3
COL_SPAN=2

COL_SPAN_TOP_FRAME=1;
ROW_SPAN_TOP_FRAME=1

COL_SPAN_CHOOSER=1
ROW_SPAN_CHOOSER=ROW_SPAN -1

COL_SPAN_OVERVIEW=1
ROW_SPAN_OVERVIEW=2

COL_SPAN_INFO=1
ROW_SPAN_INFO=2

# --------------Main Frame------------------------ #
frame_main = nttk.Frame(root, borderwidth=2)
frame_main.pack(fill=BOTH, expand=TRUE)

# Grid definition of the main frame
Grid.grid_columnconfigure(frame_main, 0, weight = 20)
Grid.grid_columnconfigure(frame_main, 1, weight = 1)
Grid.grid_columnconfigure(frame_main, 2, weight = 20)


Grid.grid_rowconfigure(frame_main, 0, weight=3)
Grid.grid_rowconfigure(frame_main, 1, weight=1)
Grid.grid_rowconfigure(frame_main, 2, weight=20)


# ------------GUI MAIN FRAMES DEFINITION--------------
#1 Top Left Frame
frame_top = TopLeftFrame(frame_main)
frame_top.grid(column=0, row=0, rowspan=ROW_SPAN_TOP_FRAME, columnspan=COL_SPAN_TOP_FRAME , sticky=NSEW)
frame_top.populateFrame()

#2 Top Right Frame
frame_info = TopRightFrame(frame_main)
frame_info.grid(column=2,row=0, rowspan=ROW_SPAN_INFO, columnspan=COL_SPAN_INFO , sticky=NSEW)

frame_info.populateFrame()


#3 Bottom Left Frame
frame_chooser = ChooserFrame(frame_main)
frame_chooser.grid(column=0, row=1, rowspan=ROW_SPAN_CHOOSER, sticky=N+S+E+W)
frame_chooser.populateFrame()



#3 Middle Frame containing two buttons
frame_options=nttk.Frame(frame_main)
# Adding buttons to option frame
button_add=nttk.Button(frame_options, text=">>")
button_add.pack(side=TOP)

button_delete=nttk.Button(frame_options, text="<<")
button_delete.pack(side=TOP)
# Add a column to the grid
frame_options.grid(row=1, column=1, sticky=NSEW)



#4 Overview Frame
frame_overview = OverviewFrame(frame_main)
frame_overview.grid(column=2, row=1, rowspan=ROW_SPAN, sticky=N+S+E+W)
frame_overview.populateFrame()

'''
button_toggle = nttk.Button(frame_overview, text="Toggle the left button")#, command=dummy_callback)
button_toggle.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_toggle.bind("<Button-1>", dummy_callback)

button_2 = nttk.Button(frame_chooser, text="Toggle the left button")#, command=dummy_callback)
button_2.pack(side=LEFT, expand=TRUE, fill=BOTH)
#button_2.grid(column=1, row=1, sticky=N+S+E+W)
button_2.bind("<Button-1>", dummy_callback)



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
# Start main loop
root.minsize(width=1200, height=800)
root.mainloop()

