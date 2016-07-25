# Revision History
# 25/07: Defined a basic structure. Read the reference of tkinter to get an overview on how it works and what you can do.



# This should be the main script where
# all the GUI elements are intialized and callback methods are set.

from tkinter import *
from Application import Application
# Create a toplevel window
# Each window has its own tcl interpreter
root=Tk()

app=Application(root)

root.mainloop()



