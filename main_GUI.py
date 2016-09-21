# Revision History (whole project)
# 25/07: Defined a basic structure. Read the reference of tkinter to get an overview on how it works and what you can do.
# 23/08: Restructured code into classes representing each main frame. Define structure according to design
# 06/09: Defined GUI for the upper left corner
# 13/09, 14/09 and 17/08: Working on parsing .json file from source pdf
# 17/09: Implemented complete interface of the TopLeftFrame + tested json parsing of the resource file
# 20/09: Worked on the ChooserFrame GUI structure. Decided for a Treeview structure. Interface to other modules still missing
# 21/09: Worked on TopRightFrame GUI. First implementation of the interface to display current subject description and content
#----------------------------------------------------------------#
# Description:
# Main script initializing all main windows

from tkinter import *

import ttk as nttk
from GUI.TopFrames.TopLeftFrame import *
from GUI.BottomFrames.ChooserFrame import *
from GUI.BottomFrames.OverviewFrame import *
from GUI.TopFrames.TopRightFrame import *





# ---------------------------- Layout constants -------------------------------------------#
ROW_SPAN=4
COL_SPAN=2

COL_SPAN_TOP_FRAME=1;
ROW_SPAN_TOP_FRAME=2

COL_SPAN_CHOOSER=1
ROW_SPAN_CHOOSER=ROW_SPAN -1

COL_SPAN_OVERVIEW=1
ROW_SPAN_OVERVIEW=2

COL_SPAN_INFO=1
ROW_SPAN_INFO=2


# ------------- Button callbacks ----------------------#
def callbackButton(action):
    if action == 1:
        print('select button clicked')
        selItem=frame_chooser.getSelectedItem();
        if selItem !=0:
            print('Selected item is:' + selItem )
    elif action == 2:
        print('delete button clicked')
    else:
        pass




#-------------------------------------------- GUI INITIALIZATION -------------------------------------------------------#

# Main "windows" window
root=Tk()

# --------------MAIN WINDOW DEFINITION------------------------ #
frame_main = nttk.Frame(root, borderwidth=2)
frame_main.pack(fill=BOTH, expand=TRUE)

# Column definition of the main frame
Grid.grid_columnconfigure(frame_main, 0, weight = 20)
Grid.grid_columnconfigure(frame_main, 1, weight = 1)
Grid.grid_columnconfigure(frame_main, 2, weight = 20)

# Row definiton of the main frame
Grid.grid_rowconfigure(frame_main, 0, weight=10)
Grid.grid_rowconfigure(frame_main, 1, weight=10)
Grid.grid_rowconfigure(frame_main, 2, weight=1)
Grid.grid_rowconfigure(frame_main, 3, weight=20)
# ------------GUI MAIN FRAMES DEFINITION-------------- #
#1 Top Left Frame initialization and placement into the main window
frame_top = TopLeftFrame(frame_main)
frame_top.grid(column=0, row=0, rowspan=ROW_SPAN_TOP_FRAME, columnspan=COL_SPAN_TOP_FRAME , sticky=N)


#2 Top Right Frame initialization and placement into the main window
frame_info = TopRightFrame(frame_main)
frame_info.grid(column=2,row=0, rowspan=ROW_SPAN_INFO, columnspan=COL_SPAN_INFO , sticky=NSEW)


#3 Bottom Left Frame
frame_chooser = ChooserFrame(frame_main)
frame_chooser.grid(column=0, row=1, rowspan=ROW_SPAN_CHOOSER, sticky=N+S+E+W)


#3 Middle Frame containing two buttons
frame_options=nttk.Frame(frame_main)
# Adding buttons to option frame
                                                # Lambda makes command associated with a function that then calls the callbackButton function
                                                # whenever executed
button_add=nttk.Button(frame_options, text=">>", command = lambda : callbackButton(1) )
button_add.pack(side=TOP)
button_delete=nttk.Button(frame_options, text="<<", command = lambda : callbackButton(2) )
button_delete.pack(side=TOP)

frame_options.grid(row=2, column=1, sticky=NSEW)



#4 Overview Frame
frame_overview = OverviewFrame(frame_main)
frame_overview.grid(column=2, row=2, rowspan=ROW_SPAN, sticky=N+S+E+W)
frame_overview.populateFrame()



#----------------------------- MAIN LOOP --------------------------------------------------------------------------#
# Start main loop
root.minsize(width=1200, height=800)
root.mainloop()



