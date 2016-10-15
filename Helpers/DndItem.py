# This module contains all callbacks for the drag and drop process
import tkinter as tk
#import main_GUI as main
root = 0
target_widget=[]
semester_text = ['WS 2017', 'SS  2017', 'WS 2018', 'SS  2018', 'WS 2019', 'SS  2019']
current_source=[]

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

    # Only do something if a target has been selected
    import GUI.BottomFrames.ChooserFrame as CH
    item = CH.chosen_tree.focus()
    if item != None and item!='':
        # Ask chooser frame which subject is currently selected
        subject = CH.ChooserFrame.item_clicked(item)
        # Additionally save reference to the selected tree
        subject['Tree'] = CH.chosen_tree


    if target != None:
        # ChooserFrame
        if '20' in target.id:
            import GUI.OverviewFrame.OverviewFrame as OF
            # Find the appropriate listbox
            if OF.OverviewFrame.add_item(target.id,subject) !=0:
                # Delete the added item
                import Helpers.Statistic_module as SM
                SM.notify()
                CH.chosen_tree.delete(item)

        # OverviewFrame
        else:
            if target.id is "DEL":
                print("I will delete the selected item.")
                global current_source
                print(current_source.added_items)
                print(current_source.curselection())

                #del current_source.added_items[current_source.curselection()]
                selection = current_source.get( current_source.curselection()[0] )

                for item in current_source.added_items:
                    if item['Name'] == selection:
                       print("You will delete " + item['Name'])
                       import GUI.BottomFrames.ChooserFrame as CH
                       CH.ChooserFrame.add_item(item['Tree'],item)
                       current_source.added_items.remove(item)
                       import Helpers.Statistic_module as SM
                       SM.notify()
                current_source.delete(current_source.curselection())
    else:
        pass


    global target_widget
    target_widget['relief']=tk.RAISED

def dnd_commit(source,event):
    global target_widget
    target_widget['relief'] = tk.RAISED

