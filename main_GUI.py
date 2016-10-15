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
#       Changed the whole geometry management - now pack manager is used for the main GUI frames. Overview Frame will be displayed in a new window!
# 05/10: Studied the drag and drop tkinter support module. Defined how the implementation will be done.
# 10/10: Implemented first parts of the drag and drop function. Started to design, define and implement the OverviewWindow. Stopped
#       at the scrollbar problem.
# 11/10: Solved problem with the scrollbar. Defined the OverviewFrame using Canvas. Added interwindow communication - subjects can be added to
#        the appropriate listbox inside the Overviewframe.
# 15/10: Implemented the deletion of items from the Overview Window Listboxes. Subjects are returned back to the Chooserframe. Deletion can be done by drag and drop.
#----------------------------------------------------------------#
# Description:
# Main script initializing all main windows
from GUI.TopFrames.TopLeftFrame import *
from Helpers.DndItem import *
from GUI.OverviewFrame.OverviewFrame import *
from GUI.TopFrames.TopRightFrame import *
import ttk as nttk
import tkinter.tix as tix
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

semester_text = ['WS 2017', 'SS  2017', 'WS 2018', 'SS  2018', 'WS 2019', 'SS  2019']
frame_overview=None
# ------------- Button callbacks ----------------------#
def show_hide_overview():
    global frame_overview
    if frame_overview is None:
        frame_overview = OverviewFrame()
        frame_overview.populateFrame()
        frame_overview.visible=1
    elif frame_overview.visible==0:
        frame_overview=None
        frame_overview=OverviewFrame()
        frame_overview.populateFrame()
        frame_overview.visible=1
    else:
        frame_overview.deiconify()
        frame_overview.rise()
def save_data(root):
    root.quit()
'''def callbackButton(action):
    if action == 1:
        print('select button clicked')
        selItem=frame_chooser.getSelectedItem();
        if selItem !=0:
            print('Selected item is:' + selItem )
    elif action == 2:
        print('delete button clicked')
    else:
        pass
'''
#-------------------------------------------- GUI INITIALIZATION -------------------------------------------------------#

# Main "windows" window
root=tix.Tk()
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
#-------- LEFT FRAME-----------
frame_left=nttk.Frame(frame_main)
frame_left.pack(side=LEFT, fill=BOTH)

import GUI.BottomFrames.ChooserFrame as CF
frame_chooser = CF.ChooserFrame(frame_left)
frame_top = TopLeftFrame(frame_left)
frame_top.pack(side=TOP, fill=Y)
frame_chooser.pack(side=TOP, fill=BOTH, expand=TRUE)
# -----------MIDDLE FRAME---------------
frame_options=nttk.Frame(frame_main)
# Adding buttons to option frame
                                                # Lambda makes command associated with a function that then calls the callbackButton function
                                                # whenever executed
#button_add=nttk.Button(frame_options, text=">>", command = lambda : callbackButton(1) )
# List of Labels displaying the semester you want to choose
semester_labels = []

for i in range(1,7):

    label=Label(master=frame_options, text = semester_text[i-1], relief=RAISED , width=8, font=('Times', '12'))
    label.id=semester_text[i-1]
    label.dnd_accept=dnd_accept
    label.dnd_enter = dnd_enter
    label.dnd_leave = dnd_leave
    label.dnd_commit = dnd_commit
    label.dnd_motion = dnd_motion
    semester_labels.append(label)
for label in semester_labels:
    label.pack(side=TOP, pady=5)
frame_options.pack(side=LEFT)


#------------ RIGHT FRAME----------------
frame_right=nttk.Frame(frame_main)
frame_right.pack(side=LEFT, fill=BOTH)


#2 Top Right Frame initialization and placement into the main window
frame_info = TopRightFrame(frame_right)
frame_info.grid(column=0,row=0, sticky=NSEW)

#-----------OVERVIEW FRAME ---------------




button_show_hide=Button(root, text="SHOW/HIDE OVERVIEW", font=('Times', '12'), relief=RAISED, command=show_hide_overview)
button_show_hide.pack()
#----------------------------- MAIN LOOP --------------------------------------------------------------------------#
root.minsize(width=1000, height=600)
root.protocol('WM_DELETE_WINDOW', lambda :save_data(root))
# Start main loop
root.mainloop()




