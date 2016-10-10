# This module contains all callbacks for the drag and drop process
# TODO: Callbacks to implement
#               dnd_enter so that you can intialize a canvas that will be drawn
#               dnd_motion so that you can redraw the canvas
#               dnd_leave so that you can delete the canvas
#               dnd_end so that you can delete the subject from the list and display it in the overview widget
import tkinter as tk
root = 0
target_widget=[]
def initialize_dnd_helpers(real_root):
    global root
    root = real_root
def dnd_accept(source, event):
    global current_source
    current_source = source
    #Return the widget that is currently at the mouse position
    x, y = event.x_root, event.y_root
    global root
    global target_widget
    target_widget = root.winfo_containing(x, y)
    target_widget['relief']=tk.SUNKEN
    return target_widget
def dnd_motion(source, event):
    print("Mouse is moving")
def dnd_enter(source,event):
    print('New widget has been entered')
    return 1
def dnd_leave( source, event):
    global target_widget
    target_widget['relief']=tk.RAISED
    print('Widget has been left')

def dnd_end(target, event):
    print('End of the drag and drop process')
    # Render the content and description frames
    import GUI.BottomFrames.ChooserFrame as CH
    item = CH.chosen_tree.focus()
    CH.ChooserFrame.item_clicked(item)
    # If a target has been selected delete the selected item
    if target!=None:
        print('Selected target is: ' + target.winfo_class() +"with id " + target.id )
    global target_widget
    target_widget['relief']=tk.RAISED
def dnd_commit(source,event):
    print(' I will be commited by a '+ source.winfo_class())
    source.delete(source.focus())
    global target_widget
    target_widget['relief'] = tk.RAISED

