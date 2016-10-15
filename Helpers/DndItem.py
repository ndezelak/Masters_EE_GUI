# This module contains all callbacks for the drag and drop process
import tkinter as tk
#import main_GUI as main
root = 0
target_widget=[]
semester_text = ['WS 2017', 'SS  2017', 'WS 2018', 'SS  2018', 'WS 2019', 'SS  2019']

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
    subject=CH.ChooserFrame.item_clicked(item)

    # If a target has been selected delete the selected item from Chooserframe and add it to the appropriate Listbox inside the Overviewframe
    if target!=None:
        print('Selected target is: ' + target.winfo_class() +"with id " + target.id )
        # Find the appropriate listbox
        import GUI.OverviewFrame.OverviewFrame as OF
        if OF.OverviewFrame.add_item(target.id,subject) !=0:
            # Delete the added item
            CH.chosen_tree.delete(item)
    global target_widget
    target_widget['relief']=tk.RAISED

def dnd_commit(source,event):
    global target_widget
    target_widget['relief'] = tk.RAISED

