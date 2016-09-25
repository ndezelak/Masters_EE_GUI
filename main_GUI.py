# Revision History (whole project)
# 25/07: Defined a basic structure. Read the reference of tkinter to get an overview on how it works and what you can do.
# 23/08: Restructured code into classes representing each main frame. Define structure according to design
# 06/09: Defined GUI for the upper left corner
# 13/09, 14/09 and 17/08: Working on parsing .json file from source pdf
# 17/09: Implemented complete interface of the TopLeftFrame + tested json parsing of the resource file
# 20/09: Worked on the ChooserFrame GUI structure. Decided for a Treeview structure. Interface to other modules still missing
# 21/09: Worked on TopRightFrame GUI. First implementation of the interface to display current subject description and content
# 22/09: Worked on ChooserFrame dynamic filling up. Found that .json file has duplicated subjects. Came to the point that a filtered selection
#        is displayed for a given subject. Further filters and sorting TBD
# 24/09: Implemented filters for subject categories. Needed to correct some data in .json for consistency.
# 25/09: Finished subject category filters + implemented dynamic filling up of the treeviews via a helper function + small fix for filling up categories after first category has been chosen
# Changed the whole geometry management - now pack manager is used for the main GUI frames. Overview Frame will be displayed in a new window!
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
root.grid_propagate(0)
# --------------MAIN WINDOW DEFINITION------------------------ #
frame_main = nttk.Frame(root, borderwidth=2)
frame_main.pack(fill=BOTH, expand=TRUE)

# Column definition of the main frame
'''
Grid.grid_columnconfigure(frame_main, 0, minsize=500)#, weight = 20)
Grid.grid_columnconfigure(frame_main, 1, minsize=30)#, weight = 1)
Grid.grid_columnconfigure(frame_main, 2, minsize=300)#, weight = 20)
'''


# Row definiton of the main frame
'''
Grid.grid_rowconfigure(frame_main, 0, minsize=200)#, weight=10)
Grid.grid_rowconfigure(frame_main, 1, minsize=200)#, weight=10)
Grid.grid_rowconfigure(frame_main, 2, minsize=25)#, weight=1)
Grid.grid_rowconfigure(frame_main, 3, minsize=400)#, weight=20)
'''
# ------------GUI MAIN FRAMES DEFINITION-------------- #
#1 Top Left Frame initialization and placement into the main window
frame_left=nttk.Frame(frame_main)
frame_left.pack(side=LEFT, fill=BOTH)

#3 Middle Frame containing two buttons
frame_options=nttk.Frame(frame_main)
# Adding buttons to option frame
                                                # Lambda makes command associated with a function that then calls the callbackButton function
                                                # whenever executed
button_add=nttk.Button(frame_options, text=">>", command = lambda : callbackButton(1) )
button_add.pack(side=TOP)
button_delete=nttk.Button(frame_options, text="<<", command = lambda : callbackButton(2) )
button_delete.pack(side=TOP)

frame_options.pack(side=LEFT)


frame_right=nttk.Frame(frame_main)
frame_right.pack(side=LEFT, fill=BOTH)

frame_top = TopLeftFrame(frame_left)
frame_top.pack(side=TOP, fill=Y)


#2 Top Right Frame initialization and placement into the main window
frame_info = TopRightFrame(frame_right)
frame_info.grid(column=0,row=0, sticky=NSEW)


#3 Bottom Left Frame
frame_chooser = ChooserFrame(frame_left)
frame_chooser.pack(side=TOP, fill=BOTH, expand=TRUE)






#4 Overview Frame
frame_overview = OverviewFrame(frame_right)
frame_overview.grid(column=0, row=1, sticky=N+S+E+W)
frame_overview.populateFrame()



#----------------------------- MAIN LOOP --------------------------------------------------------------------------#
# Start main loop
root.minsize(width=1200, height=800)
topWindow=Toplevel()
topWindow.title("Overview Window")
topWindow.minsize(width=1000, height=600)
label=nttk.Label(topWindow, text="This is the overview window")
label.pack(side=TOP, expand=TRUE)
root.mainloop()



